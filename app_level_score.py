# streamlit_app.py
import streamlit as st
from level_score import classify_level  # 파일명이 level-score.py면 모듈명은 level_score

st.set_page_config(page_title="등급 분류기", page_icon="🏷️")

st.title("🏷️ 점수 → 등급 분류기")
st.caption("점수를 입력하면 A~F 등급을 보여줍니다.")

score = st.number_input("점수 입력", min_value=0, max_value=100, value=82, step=1)

if st.button("분류하기"):
    level = classify_level(int(score))
    st.success(f"등급: **{level}**")
