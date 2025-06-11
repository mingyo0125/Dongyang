import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils import Prints

# defaultDic
Prints.PrintLine("Default Dict")
from collections import defaultdict

counter = defaultdict(int)
counter["apple"] += 1
print(counter["apple"]) # 1

words = defaultdict(list)
words['fruit'].append('apple')
print(words)  # {'fruit': ['apple']}


by_letter = {}
word = "apple"
letter = word[0]

# letter라는 키가 있으면 해당 키의 값에 word를 추가하고,
# 없으면 새로운 리스트를 만들어서 word를 추가한다.
by_letter.setdefault(letter, []).append(word)
print(by_letter)  # {'a': ['apple']}


# numpy random
Prints.PrintLine("Numpy Random")
import numpy as np

print(np.random.rand(2, 3))           # 2x3 배열, 0~1 실수
print(np.random.randint(1, 10, 5))    # 1~9 사이 정수 5개


# match-case
Prints.PrintLine("Match Case")
value = [1, 2, 3]

match value:
    case [1, 2, 3]:
        print("정확히 [1, 2, 3]과 일치!")
    case [1, 2, *rest]:
        print("나머지:", rest)
    case _:
        print("일치 없음")

# 조건부 match-case
person = ("호날두", 20) 
match person:
    case (name, age) if age >= 18:
        print(f"{name}은 성인입니다.")
    case (name, age):
        print(f"{name}은 미성년자입니다.")


# 좌표패턴
Prints.PrintLine("좌표 패턴")
point = (0, 3)

match point:
    case (0, 0):
        print("원점입니다.")
    case (0, y):
        print(f"Y축 위의 점입니다. y = {y}")
    case (x, 0):
        print(f"X축 위의 점입니다. x = {x}")
    case (x, y):
        print(f"일반 좌표: ({x}, {y})")


# 타입 힌트
Prints.PrintLine("타입 힌트")
name: str = "Alice"
score: float = 95.5
tags: list[str] = ["python", "coding"]

# Union, Optional
Prints.PrintLine("Union과 Optional")
from typing import Union, Optional

value: Union[int, str] = "hello"
maybe_name: Optional[str] = None

def process_value(value: Union[int, str]) -> None:
    match value:
        case int():
            print(f"정수 처리: {value}")
        case str():
            print(f"문자열 처리: {value}")
        case _:
            print(f"{type(value)}은 지정되지 않은 타입입니다.")


# Callable
Prints.PrintLine("Callable")
from typing import Callable

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

print(apply(lambda a, b: a + b, 3, 4))  # 7
# 다른 자료형도 가능
print(apply(lambda a, b: a + b, "가나다라", "마바사"))  # 가나다라마바사



# 문제
Prints.PrintLine("문제")

Prints.PrintLine("문제 1")
#주어진 단어 리스트를 첫 글자 기준으로 그룹핑하세요.

words = ["apple", "avocado", "banana", "blueberry", "cherry"]

# defaultdict를 사용해 첫 글자 기준으로 단어들을 분류하세요.
# 결과 예시:
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

grouped_words = defaultdict(list)
for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)
print(dict(grouped_words))

Prints.PrintLine("문제 2")
#사칙연산 기호에 따라 계산을 수행하세요.
expr = ("*", 5, 3)

# match-case를 이용해 +, -, *, / 연산 처리
# 결과: 15

match expr:
    case ("+", a, b):
        result = a + b
    case ("-", a, b):
        result = a - b
    case ("*", a, b):
        result = a * b
    case ("/", a, b) if b != 0:
        result = a / b
    case _:
        result = None
print(f"결과: {result}")


# 정수 리스트를 받아 평균을 반환하는 함수 average()를 작성하세요.
# 입력: list[int]
# 출력: float

def average(nums: list[int]) -> float:
    sum_value = sum(nums)
    count = len(nums)
    return sum_value / count if count > 0 else 0.0

print(average([1, 2, 3, 4, 5]))  # 3.0


#add, mul 함수를 정의하고 apply 함수에서 받아 사용해보세요.

# 두 개의 연산 함수 add, mul 정의
# apply라는 함수에서 인자로 받아서 결과 출력

def add(x: int, y: int) -> int:
    return x + y

def mul(x: int, y: int) -> int:
    return x * y

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

print(apply(add, 5, 3))  # 8
print(apply(mul, 5, 3))  # 15

