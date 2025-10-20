# level-score.py
def classify_level(score: int) -> str:
    if score >= 90:
        return "A등급"
    elif score >= 80:
        return "B등급"
    elif score >= 70:
        return "C등급"
    elif score >= 60:
        return "D등급"
    else:
        return "F등급"

if __name__ == "__main__":
    # 콘솔에서 테스트할 때만 실행
    score = int(input("점수를 입력하세요: "))
    level = classify_level(score)
    print(f"입력한 점수: {score}점 → 등급: {level}")
