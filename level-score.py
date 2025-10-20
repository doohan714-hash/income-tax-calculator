score = int(input("점수를 입력하세요: "))

if score >= 90:
    level = "A등급"
elif score >= 80:
    level = "B등급"
elif score >= 70:
    level = "C등급"
elif score >= 60:
    level = "D등급"
else:
    level = "F등급"

print(f"입력한 점수: {score}점 → 등급: {level}")
