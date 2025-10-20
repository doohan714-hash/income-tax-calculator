# 소득과 세금 변수 선언
income = 55000000   # 소득 (예: 5,500만 원)
tax = 0              # 세금 변수 초기화

# 소득 수준 분류 및 세금 계산
if income < 20000000:
    level = "저소득층"
    tax = income * 0.05   # 5% 세율
elif income < 50000000:
    level = "중간소득층"
    tax = income * 0.25   # 25% 세율
elif income < 100000000:
    level = "고소득층"
    tax = income * 0.50   # 50% 세율
else:
    level = "최고소득층"
    tax = income * 0.35   # 35% 세율 (선택적으로 유지)

# 결과 출력
print("소득:", income, "원")
print("소득 수준:", level)
print("예상 세금:", format(int(tax), ","), "원")
