import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.set_page_config(page_title="대전 서구 음식점 분류·추천", layout="wide")

st.title("🍽️ 대전 서구 음식점 분류 및 추천 시스템")
st.write("엑셀 파일을 업로드하면 음식점을 자동으로 한식/양식/중식/일식으로 분류한 뒤 시각화하고 랜덤 추천합니다!")

# ---------------------------
# 1. 파일 업로드
# ---------------------------
uploaded = st.file_uploader("📂 엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded:
    df = pd.read_excel(uploaded)

    st.success("파일이 성공적으로 업로드되었습니다!")

    # ------------------------------------------------------
    # 2. 음식점 분류 로직
    # ------------------------------------------------------
    # 분류 기준 키워드
    korean_keywords = ["한식", "백반", "고기", "국밥", "칼국수", "한우", "족발", "보쌈"]
    western_keywords = ["양식", "스테이크", "피자", "파스타", "버거", "브런치"]
    chinese_keywords = ["중식", "짜장", "짬뽕", "탕수육", "중화요리"]
    japanese_keywords = ["일식", "초밥", "돈카츠", "라멘", "회"]

    def classify(name):
        name = str(name)

        if any(k in name for k in korean_keywords):
            return "한식"
        if any(k in name for k in western_keywords):
            return "양식"
        if any(k in name for k in chinese_keywords):
            return "중식"
        if any(k in name for k in japanese_keywords):
            return "일식"
        return "기타"

    df["업종분류"] = df["업소명"].apply(classify)

    # ------------------------------------------------------
    # 3. Plotly 시각화
    # ------------------------------------------------------
    st.subheader("📊 업종별 음식점 분포 (인터랙티브)")

    count_df = df["업종분류"].value_counts().reset_index()
    count_df.columns = ["업종", "개수"]

    fig = px.bar(
        count_df,
        x="업종",
        y="개수",
        title="업종별 음식점 수",
        text="개수"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------------
    # 4. 업종 선택 → 랜덤 4개 추천
    # ------------------------------------------------------
    st.subheader("🎯 업종별 랜덤 음식점 4개 추천")

    category = st.selectbox("업종을 선택하세요", ["한식", "양식", "중식", "일식"])

    filtered = df[df["업종분류"] == category]

    if len(filtered) == 0:
        st.warning("해당 업종의 음식점이 없습니다.")
    else:
        sample = filtered.sample(4) if len(filtered) >= 4 else filtered
        st.write(f"### 📌 **{category} 추천 음식점**")
        st.table(sample[["업소명", "도로명주소", "전화번호"]])

