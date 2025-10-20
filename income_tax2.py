# 소득(income)과 세금(tax) 변수 선언
income = 85000000   # 예: 8,500만 원
tax = 0              # 세금 초기값

# 소득 수준 분류 및 세금 계산
if income < 20000000:
    level = "저소득층"
    tax = income * 0.05   # 5% 세율
elif income < 50000000:
    level = "중간소득층"
    tax = income * 0.20   # 20% 세율
elif income < 100000000:
    level = "고소득층"
    tax = income * 0.40   # 40% 세율
else:
    level = "초고소득층"
    tax = income * 0.50   # 50% 세율

# 결과 출력
print("소득:", format(income, ","), "원")
print("소득 수준:", level)
print("예상 세금:", format(int(tax), ","), "원")
