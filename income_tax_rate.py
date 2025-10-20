# 소득(income)과 세금(tax) 변수 선언
income = 75000000   # 예: 7,500만 원
tax = 0              # 세금 초기화

# 소득 수준 분류 및 세금 계산
if income < 20000000:
    level = "저소득층"
    tax = income * 0.05   # 5%
elif income < 50000000:
    level = "중간소득층"
    tax = income * 0.20   # 20%
elif income < 100000000:
    level = "고소득층"
    tax = income * 0.40   # 40%
else:
    level = "초고소득층"
    tax = income * 0.50   # 50%

# 결과 출력
print("===== 💰 소득 수준 분류 결과 =====")
print(f"소득: {income:,} 원")
print(f"소득 수준: {level}")
print(f"적용 세율: {int((tax / income) * 100)}%")
print(f"예상 세금: {int(tax):,} 원")
