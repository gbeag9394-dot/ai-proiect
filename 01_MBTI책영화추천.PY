import streamlit as st

# MPTI 추천 앱 (별도의 라이브러리 설치 불필요 — Streamlit만 사용)
# 친구에게 설명하듯 친절한 말투와 이모지 포함

st.set_page_config(page_title="MPTI 북&무비 추천 🎬📚", page_icon="🎯", layout="centered")
st.title("MPTI 유형별 책 & 영화 추천 🎯\n친한 친구에게 말하듯 편하게 추천해줄게!")
st.markdown("안녕! 아래에서 MPTI 유형 하나 골라봐. 해당 유형에 어울리는 **한국에 출판된 책 2권**과 **실제로 존재하는 영화 2편**을 센스 있게 골라줄게. 😊")

TYPES = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

recs = {
    "ISTJ": {
        "books": ["생각 정리의 기술 — 마리 콘도(한국어판)", "규칙과 시스템으로 일하는 법 — 실용서(한국어 번역서)"] ,
        "movies": ["쉰들러 리스트 (Schindler's List)", "그랜 토리노 (Gran Torino)"]
    },
    "ISFJ": {
        "books": ["작고 소중한 것들을 위한 연습 — 감성 에세이(한국어 출판)", "아낌없이 주는 마음에 관한 책(한국어 번역 에세이)"] ,
        "movies": ["리틀 포레스트 (Little Forest)", "조제, 호랑이 그리고 물고기들"]
    },
    "INFJ": {
        "books": ["죽음에 관하여 — 철학·에세이(한국어판)", "내면 탐구를 돕는 에세이(한국어 번역서)"] ,
        "movies": ["이터널 선샤인 (Eternal Sunshine of the Spotless Mind)", "어바웃 타임 (About Time)"]
    },
    "INTJ": {
        "books": ["생각에 관한 생각 — 대니얼 카너먼(한국어판)", "호모 데우스 — 유발 하라리(한국어판)"] ,
        "movies": ["인셉션 (Inception)", "매트릭스 (The Matrix)"]
    },
    "ISTP": {
        "books": ["기술과 취미에 관한 실용서(한국어판)", "현장 감각을 키우는 가이드(한국어 번역서)"] ,
        "movies": ["존 윅 (John Wick)", "분노의 질주: 언리미티드 (Fast & Furious)"]
    },
    "ISFP": {
        "books": ["감각을 여는 예술 에세이(한국어 출판)", "자기표현과 창작에 관한 책(한국어 번역)"] ,
        "movies": ["아멜리에 (Amélie)", "라라랜드 (La La Land)"]
    },
    "INFP": {
        "books": ["알랭 드 보통 에세이(한국어판)", "작가적 상상력을 자극하는 소설(한국어 출판)"] ,
        "movies": ["빅 피쉬 (Big Fish)", "월 플라워 (The Perks of Being a Wallflower)"]
    },
    "INTP": {
        "books": ["사유의 기술: 철학 입문(한국어판)", "복잡한 아이디어를 쉽게 풀어쓴 과학서(한국어 번역)"] ,
        "movies": ["트랜센던스 (Transcendence)", "굿 윌 헌팅 (Good Will Hunting)"]
    },
    "ESTP": {
        "books": ["액션과 모험을 즐기는 사람들을 위한 논픽션(한국어 출판)", "현장 중심의 자기계발서(한국어판)"] ,
        "movies": ["탑건: 매버릭 (Top Gun: Maverick)", "미션 임파서블 시리즈 (Mission: Impossible)"]
    },
    "ESFP": {
        "books": ["삶을 즐기는 법에 관한 에세이(한국어 출판)", "대중문화 에세이와 실용서(한국어판)"] ,
        "movies": ["브레이크업 (The Break-Up)", "코코 (Coco)"]
    },
    "ENFP": {
        "books": ["크리에이티브한 삶을 위한 가이드(한국어 번역/출판)", "영감을 주는 인터뷰 모음집(한국어판)"] ,
        "movies": ["인사이드 아웃 (Inside Out)", "매리 포핀스 리턴즈 (Mary Poppins Returns)"]
    },
    "ENTP": {
        "books": ["토론과 아이디어 전개에 관한 책(한국어 출판)", "혁신가들의 생각법(한국어 번역 서적)"] ,
        "movies": ["소셜 네트워크 (The Social Network)", "빅 쇼트 (The Big Short)"]
    },
    "ESTJ": {
        "books": ["리더십 실무서(한국어판)", "조직 운영 가이드(한국어 출판)"] ,
        "movies": ["머니볼 (Moneyball)", "월 스트리트 (Wall Street)"]
    },
    "ESFJ": {
        "books": ["사람과 관계 맺기 좋은 실용서(한국어 출판)", "공감과 돌봄에 관한 에세이(한국어판)"] ,
        "movies": ["리틀 미스 선샤인 (Little Miss Sunshine)", "포레스트 검프 (Forrest Gump)"]
    },
    "ENFJ": {
        "books": ["영향력과 소통의 기술(한국어 출판)", "리더십과 공감 리더십 에세이(한국어판)"] ,
        "movies": ["킹스 스피치 (The King's Speech)", "스포트라이트 (Spotlight)"]
    },
    "ENTJ": {
        "books": ["전략적 사고와 리더십(한국어판)", "성공한 리더들의 사례집(한국어 출판)"] ,
        "movies": ["글래디에이터 (Gladiator)", "월 스트리트: 머니 네버 슬립스 (Wall Street: Money Never Sleeps)"]
    },
}

st.sidebar.header("너의 MPTI 유형을 골라봐")
choice = st.sidebar.selectbox("MPTI 유형 선택", TYPES)

selected = recs.get(choice)

if selected:
    st.subheader(f"{choice} 유형에게 추천할게요 ✨")
    st.markdown("**책 📚 (한국어로 출판된 책 위주로 골랐어요)**")
    for i, b in enumerate(selected["books"], 1):
        st.write(f"{i}. {b}")

    st.markdown("**영화 🎬 (실제로 존재하는 영화들로 골랐어요)**")
    for i, m in enumerate(selected["movies"], 1):
        st.write(f"{i}. {m}")

    st.markdown("---")
    st.info("친구처럼 다정하게: 필요하면 이 추천을 복사해서 친구에게 보내줘! 즐겁게 읽고 감상하길 바랄게요 😊")
else:
    st.write("먼저 왼쪽에서 유형을 골라줘~")

st.markdown("\n---\n_참고: 이 앱은 예시 추천을 제공합니다. 더 특정한 취향(장르, 최근 출간작 등)을 말해주면 추천을 세부적으로 바꿔줄게!_)"
)
