# streamlit_app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="소득·세금 계산기", page_icon="💰")
st.title("💰 소득 수준별 세금 계산기")
st.caption("초고소득층 50% · 고소득층 40% · 중간소득층 20% · 저소득층 5% (예시 세율)")

# 세율표(예시)
brackets = [
    {"소득 수준": "저소득층", "소득 구간(원)": "0 ~ 19,999,999", "세율": 0.05},
    {"소득 수준": "중간소득층", "소득 구간(원)": "20,000,000 ~ 49,999,999", "세율": 0.20},
    {"소득 수준": "고소득층", "소득 구간(원)": "50,000,000 ~ 99,999,999", "세율": 0.40},
    {"소득 수준": "초고소득층", "소득 구간(원)": "100,000,000 이상", "세율": 0.50},
]
df = pd.DataFrame(brackets)
df_display = df.copy()
df_display["세율"] = (df_display["세율"] * 100).astype(int).astype(str) + "%"

st.subheader("📊 세율표 (예시)")
st.table(df_display)

def classify_and_tax(income: int):
    if income < 20_000_000:
        level, rate = "저소득층", 0.05
    elif income < 50_000_000:
        level, rate = "중간소득층", 0.20
    elif income < 100_000_000:
        level, rate = "고소득층", 0.40
    else:
        level, rate = "초고소득층", 0.50
    tax = int(income * rate)
    return level, rate, tax

st.subheader("🧮 계산기")
income = st.number_input("소득(원)을 입력하세요", min_value=0, step=100_000, value=75_000_000, format="%d")

if st.button("세금 계산하기"):
    level, rate, tax = classify_and_tax(int(income))
    st.success(f"소득 수준: **{level}**")
    st.metric("예상 세금", f"{tax:,} 원", help=f"적용 세율: {int(rate*100)}%")
    st.caption("※ 본 예시는 학습용이며 실제 세법과 다를 수 있습니다.")
