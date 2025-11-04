import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MPTI 진로 추천기 🎯", page_icon="💫", layout="centered")

# --- 헤더 ---
st.title("🎓 MPTI 진로 추천기")
st.markdown("안녕! 👋 네 MPTI 유형을 알려주면, 그에 맞는 진로를 추천해줄게 💡")

# --- MBTI 목록 ---
mpti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# --- 유형별 진로 추천 딕셔너리 ---
career_recommendations = {
    "INTJ": "🧠 전략가형! 데이터 분석가나 연구원 어때?",
    "INTP": "💡 아이디어 뱅크형! 개발자나 발명가에 딱이야!",
    "ENTJ": "🚀 리더형! CEO, 기획자, 관리자에 찰떡이야!",
    "ENTP": "🎤 토론왕! 창업가나 마케팅 기획자가 어울려!",
    "INFJ": "🌱 이상주의자! 심리상담가나 사회복지사 추천!",
    "INFP": "🎨 감성파! 작가,
