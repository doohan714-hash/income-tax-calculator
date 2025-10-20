# streamlit_app.py
import streamlit as st

# 앱 기본 설정
st.set_page_config(page_title="소득·세금 계산기", page_icon="💰")

st.title("💰 소득 수준별 세금 계산기")
st.caption("초고소득층 50% / 고소득층 40% / 중간소득층 20% / 저소득층 5%")

# 사용자 입력
income = st.number_input("소득(원)을 입력하세요:", min_value=0, step=100000, value=85000000)

# 계산 버튼
if st.button("세금 계산하기"):
    # 소득 수준 및 세금 계산
    if income < 20000000:
        level = "저소득층"
        tax = income * 0.05
    elif income < 50000000:
        level = "중간소득층"
        tax = income * 0.20
    elif income < 100000000:
        level = "고소득층"
        tax = income * 0.40
    else:
        level = "초고소득층"
        tax = income * 0.50

    # 결과 표시
    st.success(f"소득 수준: **{level}**")
    st.metric("예상 세금", f"{int(tax):,} 원", help=f"세율: {int((tax/income)*100)}%")
else:
    st.info("좌측에 소득을 입력하고 버튼을 눌러주세요 💡")
