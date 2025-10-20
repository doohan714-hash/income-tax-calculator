# streamlit_app.py
import streamlit as st

def classify_and_tax(income: int):
    """요청하신 세율 규칙 적용:
       - < 2천만: 5%
       - < 5천만: 25%
       - < 1억:   50%
       - 그 이상: 35% (유지)
    """
    if income < 20_000_000:
        level, rate = "저소득층", 0.05
    elif income < 50_000_000:
        level, rate = "중간소득층", 0.25
    elif income < 100_000_000:
        level, rate = "고소득층", 0.50
    else:
        level, rate = "최고소득층", 0.35
    tax = int(income * rate)
    return level, rate, tax

st.set_page_config(page_title="소득·세금 계산기", page_icon="💰")
st.title("💰 소득·세금 계산기")

income = st.number_input(
    "소득(원) 입력", min_value=0, value=55_000_000, step=100_000, format="%d"
)

if st.button("계산하기"):
    level, rate, tax = classify_and_tax(income)
    st.success(f"소득 수준: {level}")
    st.metric("예상 세금", f"{tax:,} 원", help=f"적용 세율: {int(rate*100)}%")
    st.caption("※ 예시 세율이며 실제 세법과 다를 수 있습니다.")
