import streamlit as st
st.title('나의 첫 웹 서비스 만들기')
현아=st.text_input('이름을 입력하세요:')
if st.button('인사말 생성'):
  st.write(현+'님! 안녕하세요')
  st.balloons()
st.warning('방가')
st.error('정말 반가워요')
st.balloons()
