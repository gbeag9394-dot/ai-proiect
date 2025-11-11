# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Seoul Top10 (Folium)", layout="wide")

st.title("🗺️ Seoul — Top 10 Tourist Spots (for Foreign Visitors)")
st.markdown(
    "Folium 지도로 외국인들에게 인기 있는 서울 주요 관광지 Top10을 표시합니다. "
    "마커를 클릭하면 간단한 설명과 링크(있을 경우)를 볼 수 있어요."
)

# Top 10 명소 목록 (이름, 위도, 경도, 설명, optional link)
places = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.579615,
        "lon": 126.977041,
        "desc": "조선 왕조의 대표적 궁궐 — 수문장 교대식 등 볼거리.",
        "url": "http://english.cha.go.kr/english/"
    },
    {
        "name": "Changdeokgung Palace & Huwon (창덕궁과 후원)",
        "lat": 37.579388,
        "lon": 126.991052,
        "desc": "유네스코 세계문화유산으로 유명한 궁궐과 비밀의 정원(후원).",
        "url": "http://english.cha.go.kr/english/"
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.582604,
        "lon": 126.983036,
        "desc": "전통 한옥이 보존된 마을, 사진 스팟과 골목 산책 추천.",
        "url": "https://english.visitseoul.net/attractions/Bukchon-Hanok-Village_/1712"
    },
    {
        "name": "N Seoul Tower (N서울타워) - Namsan",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 전경을 한눈에 볼 수 있는 전망 명소.",
        "url": "https://www.nseoultower.co.kr/eng/"
    },
    {
        "name": "Myeongdong (명동 쇼핑거리)",
        "lat": 37.563668,
        "lon": 126.986033,
        "desc": "한국 뷰티/패션 쇼핑의 메카, 길거리 음식도 유명.",
        "url": "https://english.visitseoul.net/shopping/Myeongdong_/99"
    },
    {
        "name": "Hongdae / Hongik University Area (홍대)",
        "lat": 37.556263,
        "lon": 126.925157,
        "desc": "젊음의 문화, 스트리트 퍼포먼스, 카페와 활기찬 밤문화.",
        "url": "https://english.visitseoul.net/where-to-go/Hongdae_/54"
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.574015,
        "lon": 126.984749,
        "desc": "전통 공예품과 찻집이 많은 문화 상점가.",
        "url": "https://english.visitseoul.net/shopping/Insadong_/103"
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문)",
        "lat": 37.566295,
        "lon": 127.009310,
        "desc": "건축·패션·전시가 어우러진 디자인 랜드마크.",
        "url": "http://www.ddp.or.kr/english/"
    },
    {
        "name": "Gwangjang Market (광장시장)",
        "lat": 37.570028,
        "lon": 127.007518,
        "desc": "전통 시장의 길거리 음식(비빔밥/빈대떡 등)이 인기.",
        "url": "https://english.visitseoul.net/eat/Gwangjang-Market_/118"
    },
    {
        "name": "Hangang River — Yeouido Hangang Park (한강 여의도)",
        "lat": 37.526013,
        "lon": 126.932615,
        "desc": "한강 공원에서 피크닉, 자전거, 야경(반포대교 무지개분수) 추천.",
        "url": "https://english.visitseoul.net/parks/Hangang-Park_/97"
    },
]

# 기본 맵(서울 중심)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for p in places:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}"
    if p.get("url"):
        popup_html += f"<br><a href='{p['url']}' target='_blank'>More info</a>"
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

# 클러스터를 원하면 아래 주석을 해제하고 MarkerCluster 사용
# from folium.plugins import MarkerCluster
# cluster = MarkerCluster().add_to(m)
# for p in places:
#     folium.Marker(location=[p["lat"], p["lon"]], popup=p["name"]).add_to(cluster)

# Streamlit에 표시
with st.expander("🗺️ 지도 옵션"):
    center_lat = st.number_input("초기 중심 위도", value=37.5665, format="%.6f")
    center_lon = st.number_input("초기 중심 경도", value=126.9780, format="%.6f")
    zoom = st.slider("초기 줌 레벨", min_value=10, max_value=16, value=12)
    if st.button("지도 재설정"):
        m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom)
        for p in places:
            popup_html = f"<b>{p['name']}</b><br>{p['desc']}"
            if p.get("url"):
                popup_html += f"<br><a href='{p['url']}' target='_blank'>More info</a>"
            folium.Marker(
                location=[p["lat"], p["lon"]],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=p["name"],
                icon=folium.Icon(color="blue", icon="info-sign"),
            ).add_to(m)

# Folium map 렌더링 (streamlit-folium)
st_data = st_folium(m, width="100%", height=650)

# 오른쪽 패널에 간단 목록
with st.sidebar:
    st.header("🏷️ Top 10 명소")
    for i, p in enumerate(places, start=1):
        st.markdown(f"**{i}. {p['name']}**  \n{p['desc']}  \n")
    st.markdown("---")
    st.markdown("데이터 출처(예시): VisitKorea, VisitSeoul, Tripadvisor 등. :contentReference[oaicite:1]{index=1}")

st.markdown("### 사용법")
st.markdown("- `requirements.txt` 확인 후 설치하세요: `pip install -r requirements.txt`")
st.markdown("- 로컬 실행: `streamlit run app.py`")
