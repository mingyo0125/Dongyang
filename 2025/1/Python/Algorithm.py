# ✅ 2. 가변 인자와 키워드 인자 (ch06)
# 문제:
# 학생의 이름과 과목별 점수를 키워드 인자로 받아 평균을 구하는 함수 calculate_avg(name, **scores)를 작성하시오.
# 예시: calculate_avg("홍길동", math=90, english=85, science=92)

def calculate_avg(name, **scores):
    return {name: sum(scores.values) / len(scores)}

# ✅ 3. 리스트 컴프리헨션 (ch08)
# 문제:
# 1부터 100까지의 숫자 중 3의 배수만 제곱하여 리스트로 생성하는 컴프리헨션을 작성하시오.

li = [x**2 for x in range(1, 100) if x % 3 == 0]

# ✅ 4. 중첩 리스트 컴프리헨션 (ch08)
# 문제:
# 3행 4열의 2차원 리스트를 생성하되, 각 요소는 "i*j"의 값을 갖도록 리스트 컴프리헨션을 사용하시오.

# 이차원 리스트는 안 배워서 패스
# 근데 답은 주셈

# ✅ 5. 제너레이터 함수 (ch08)
# 문제:
# 1부터 n까지의 홀수를 차례로 생성하는 제너레이터 함수 prime_generator(n)를 작성하시오.

def prime_generator(n):
    for i in range(1, n):
        if i % 2 != 0:
            yield i

ge = prime_generator(10)
for i in range(10):
    print(prime_generator(i))

# ✅ 6. 구조적 패턴 매칭 (ch09)
# 문제:
# 아래 리스트의 항목을 하나씩 검사해 이름이 "홍길동" 또는 "김철수"일 경우 "한국인"을 출력하고, "John"일 경우 "외국인"을 출력하는 코드를 match-case 구문으로 작성하시오.

names = ["홍길동", "John", "김철수", "Anna"]

for name in names:
    match name:
        case "홍길동" | "김철수":
            print("한국인")
        case "John" | "Anna":
            print("외국인")

# python
# 복사
# 편집
# names = ["홍길동", "John", "김철수", "Anna"]
# ✅ 7. 타입 힌트 적용 함수 (ch09)
# 문제:
# 다음 요구사항을 만족하는 함수를 작성하시오.

# 함수명: multiply

# 인자: 정수형 두 개

# 반환값: 정수형 곱셈 결과
# → 함수 정의 시 타입 힌트를 적용하시오.
from typing import Union

def multiply(v1: int, v2: int) -> int:
    return v1 * v2


# ✅ 8. 예외 처리 (ch10)
# 문제:
# 사용자로부터 두 개의 정수를 입력받아 나눗셈 결과를 출력하는 프로그램을 작성하시오.
# 단, 0으로 나누는 경우를 예외 처리하여 "0으로 나눌 수 없습니다"를 출력하시오.

input_value1 = int(input())
input_value2 = int(input())
try:
    print(input_value1 / input_value2)
except ValueError as v:
    print("0으로 나눌 수 없습니다")

# ✅ 9. 파일 입출력 (텍스트) (ch10)
# 문제:
# 사용자에게 여러 줄의 문자열을 입력받아 "output.txt" 파일에 저장하시오.
# 그 후 해당 파일을 읽어 출력하는 프로그램을 작성하시오.


# 모름

# ✅ 10. pickle 모듈을 활용한 바이너리 파일 입출력 (ch10)
# 문제:
# 아래 딕셔너리를 pickle 모듈을 이용해 "data.pkl"로 저장하고, 다시 불러와 출력하시오.


filename = "example.txt"

# 사용자 입력을 받아 파일에 저장
with open(filename, "w", encoding="utf-8") as f:
    while True:
        line = input("저장할 내용을 입력하세요 (끝내려면 '끝' 입력): ")
        if line == "끝":
            break
        f.write(line + "\n")  # 줄바꿈 포함해서 저장

print(f"{filename} 파일에 저장 완료.")