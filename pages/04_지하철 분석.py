import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 로드
df = pd.read_csv("sune.csv", encoding="cp949")

# 페이지 제목
st.title("📊 서울 지하철 승하차 데이터 시각화 (2025년 10월)")

# 날짜 선택 (2025년 10월 중 하루)
selected_date = st.date_input(
    "📅 날짜를 선택하세요 (2025년 10월)",
    value=pd.to_datetime("2025-10-01"),
    min_value=pd.to_datetime("2025-10-01"),
    max_value=pd.to_datetime("2025-10-31")
)

# 호선 선택
lines = sorted(df["노선명"].unique())
selected_line = st.selectbox("🚇 호선을 선택하세요", lines)

# 날짜 변환
selected_date_str = selected_date.strftime("%Y%m%d")

# 데이터 필터링
filtered = df[
    (df["사용일자"].astype(str) == selected_date_str) &
    (df["노선명"] == selected_line)
].copy()

# 승하차 합산 컬럼 추가
filtered["총승하차"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 상위 10개 역
top10 = filtered.sort_values("총승하차", ascending=False).head(10)

# 색상 설정 (1등 빨강, 나머지 파랑 → 점점 연해짐)
colors = ["red"] + ["rgba(0, 0, 255, {:.2f})".format(1 - i * 0.1) for i in range(1, 10)]

# Plotly 그래프 생성
fig = go.Figure(
    data=[
        go.Bar(
            x=top10["역명"],
            y=top10["총승하차"],
            marker=dict(color=colors)
        )
    ]
)

fig.update_layout(
    title=f"🚉 {selected_date_str} / {selected_line} 승하차 합계 TOP 10",
    xaxis_title="역명",
    yaxis_title="승하차 총합",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
