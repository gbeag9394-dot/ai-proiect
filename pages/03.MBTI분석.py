# streamlit_mbti_plotly_app.py
# ---------------------------------------------
# 사용법:
# 1) 이 파일을 'app.py'로 저장합니다.
# 2) Streamlit Cloud(또는 로컬)에서 실행합니다.
# 3) 동일 폴더에 'countriesMBTI_16types.csv' 파일을 두세요 (/mnt/data에 이미 업로드된 경우 해당 경로로 수정 필요).
#
# requirements.txt 내용 (Streamlit Cloud에 함께 올리세요):
# streamlit
# pandas
# plotly
# ---------------------------------------------

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title='Country MBTI Explorer', layout='wide')

st.title('🌍 Country MBTI Explorer — 국가별 MBTI 비율 시각화')
st.markdown('사이드바에서 국가를 선택하면 해당 국가의 16가지 MBTI 비율을 **인터랙티브한 Plotly 막대그래프**로 보여줍니다.')

# 데이터 로드
DEFAULT_PATH = '/mnt/data/countriesMBTI_16types.csv'
path = DEFAULT_PATH if os.path.exists(DEFAULT_PATH) else st.file_uploader('CSV 파일 업로드', type=['csv'])

if isinstance(path, str):
    df = pd.read_csv(path)
else:
    if path is None:
        st.warning('데이터 파일을 업로드하거나 /mnt/data에 countriesMBTI_16types.csv가 있어야 합니다.')
        st.stop()
    df = pd.read_csv(path)

# 기대하는 컬럼들 체크
expected_mbti = ['INFJ','ISFJ','INTP','ISFP','ENTP','INFP','ENTJ','ISTP','INTJ','ESFP','ESTJ','ENFP','ESTP','ISTJ','ENFJ','ESFJ']
missing = [c for c in expected_mbti if c not in df.columns]
if missing:
    st.error(f'다음 MBTI 컬럼이 데이터에 없습니다: {missing}')
    st.stop()

countries = df['Country'].astype(str).tolist()

# 사이드바 컨트롤
st.sidebar.header('컨트롤')
selected_country = st.sidebar.selectbox('국가 선택', countries)
show_table = st.sidebar.checkbox('원본 테이블 보기', value=False)

# 선택한 국가의 행
row = df[df['Country'].astype(str) == selected_country]
if row.empty:
    st.error('선택한 국가의 데이터가 존재하지 않습니다.')
    st.stop()

# MBTI 값 추출 및 정렬
mbti_vals = row[expected_mbti].iloc[0].astype(float)
mbti_series = pd.Series(mbti_vals.values, index=expected_mbti)
mbti_sorted = mbti_series.sort_values(ascending=False)

# 색상 생성 함수: 1등 빨(#e63946), 2등 파(#1d4ed8), 나머지는 파->빨 그라데이션
def hex_from_rgb(r,g,b):
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

red = (230,57,70)    # #e63946
blue = (29,78,216)   # #1d4ed8

# prepare colors list aligned with expected_mbti order
colors = []
max_idx = mbti_series.idxmax()
second_idx = mbti_series.drop(max_idx).idxmax()

# For interpolation, use min and max among the "others" (exclude top1, top2) to scale
others = mbti_series.drop([max_idx, second_idx])
if not others.empty:
    others_min = others.min()
    others_max = others.max()
else:
    others_min = others_max = 0.0

for k in expected_mbti:
    v = mbti_series[k]
    if k == max_idx:
        colors.append(hex_from_rgb(*red))
    elif k == second_idx:
        colors.append(hex_from_rgb(*blue))
    else:
        # when others_max == others_min, fallback to midpoint
        if others_max - others_min <= 1e-9:
            t = 0.5
        else:
            t = (v - others_min) / (others_max - others_min)
            t = max(0.0, min(1.0, t))
        # interpolate blue -> red by t (0 -> blue, 1 -> red)
        r = blue[0] + (red[0] - blue[0]) * t
        g = blue[1] + (red[1] - blue[1]) * t
        b = blue[2] + (red[2] - blue[2]) * t
        colors.append(hex_from_rgb(r,g,b))

# Build Plotly bar chart
fig = go.Figure(go.Bar(
    x=expected_mbti,
    y=mbti_series[expected_mbti],
    marker_color=colors,
    text=mbti_series[expected_mbti].round(2).astype(str) + '%',
    textposition='auto',
))

fig.update_layout(
    title=f'{selected_country} — MBTI 분포 (상위: {max_idx} / 차상위: {second_idx})',
    xaxis_title='MBTI 유형',
    yaxis_title='비율',
    yaxis=dict(range=[0, mbti_series.max()*1.15]),
    template='plotly_white',
    hovermode='closest',
)

# 레이아웃: 왼쪽 그래프, 오른쪽 요약
col1, col2 = st.columns([3,1])
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.subheader('요약')
    st.markdown(f'- 선택 국가: **{selected_country}**')
    st.markdown(f'- 1등: **{max_idx}** ({mbti_series[max_idx]}%)')
    st.markdown(f'- 2등: **{second_idx}** ({mbti_series[second_idx]}%)')
    st.markdown('---')
    st.write('상위 3개 유형:')
    for i, (k,v) in enumerate(mbti_sorted.head(3).items(), start=1):
        st.write(f'{i}. {k} — {v}%')

if show_table:
    st.subheader('원본 데이터 (선택한 국가)')
    st.dataframe(row.T.rename(columns={row.index[0]: '값'}))

st.markdown('---')
st.caption('파일: app.py — Streamlit Cloud에 업로드하고 requirements.txt를 함께 배포하세요.')
