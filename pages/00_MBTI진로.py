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
    "INFP": "🎨 감성파! 작가, 디자이너, 예술가 느낌이야~",
    "ENFJ": "🤝 따뜻한 리더! 교사, HR, 멘토 어때?",
    "ENFP": "🔥 열정가득! 콘텐츠 크리에이터나 이벤트 플래너 찰떡!",
    "ISTJ": "📋 현실주의자! 회계사, 공무원, 관리자 추천!",
    "ISFJ": "💞 세심한 조력자! 간호사, 교사, 사회복지사 어울려~",
    "ESTJ": "🏢 조직형 리더! 관리자, 경영자, 프로젝트 매니저 굿!",
    "ESFJ": "🌸 사교적인 헬퍼! 서비스직이나 상담사 추천!",
    "ISTP": "🔧 실용주의자! 엔지니어, 정비사, 프로그래머 어때?",
    "ISFP": "🎵 예술혼 가득! 디자이너, 플로리스트, 음악가 좋을 듯!",
    "ESTP": "⚡ 모험가형! 영업직이나 창업가로도 잘 맞아!",
    "ESFP": "🎉 분위기 메이커! 배우, 진행자, 이벤트 플래너 최고!"
}

# --- 사용자 입력 ---
selected_type = st.selectbox("👉 자신의 MPTI 유형을 선택해봐!", mpti_types)

# --- 버튼 누르면 결과 출력 ---
if st.button("🔍 진로 추천받기!"):
    st.success(f"{career_recommendations.get(selected_type, '알 수 없는 유형이에요 🤔')}")
    st.balloons()
else:
    st.info("아래에서 유형을 선택하고 버튼을 눌러봐! 💬")

# --- 푸터 ---
st.markdown("---")
st.caption("💫 만든이: 친구 같은 챗 | 더 많은 예시는 👉 [gptonline.ai/ko](https://gptonline.ai/ko/)")
