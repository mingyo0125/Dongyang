from Utils import Prints

Prints.PrintLine("오퍼레이터")
from operator import add, sub, mul, truediv

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

def operation():
    op1 = input("첫 번째 숫자(피연산자)를 입력하세요: ")
    operator = input("연산자를 입력하세요: ")
    op2 = input("두 번째 숫자(피연산자)를 입력하세요: ")

    try:
        result = operators[operator](float(op1), float(op2))
        if isinstance(result, float):
            print(f"결과: {result:.2f}")
        else:
            print(f"결과: {result}")
    except ValueError:
        print("잘못된 입력입니다.")

# import 했을때는 실행 안 되고 직접 실행해야 실행됨
# if __name__ == "__main__":
#     operation()


Prints.PrintLine("Default Dict")
# 딕셔너리와 유사하지만 초기값을 가지는 딕셔너리
from collections import defaultdict
int_dict = defaultdict(int)
print("초기값이 0인 int_dict:", int_dict["a"])

int_dict2 = defaultdict(lambda: 100)
print("초기값이 100인 int_dict2:", int_dict2["a"])


words = ["하늘색", "하수도", "하도급", "구경꾼", "구청직원", "날개", "날계란"]
dict_list = defaultdict(list)
for word in words:
    first_letter = word[0]
    dict_list[first_letter].append(word)

# 글자수 세기
int_count = defaultdict(int)
st = "mississippi"
for char in st:
    int_count[char] += 1

print("문자 빈도 수:", dict(int_count))


Prints.PrintLine("Random Module")
import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개의 숫자를 랜덤하게 선택
    return random.sample(range(1, 46), 6)

def check_lotto_numbers(user_numbers, lotto_numbers):
    # 사용자가 입력한 번호와 로또 번호를 비교
    matched_numbers = set(user_numbers) & set(lotto_numbers)
    return len(matched_numbers), matched_numbers

def lotto_simulation():
    user_input = input("로또 번호 6개를 입력하세요 (1-45 사이의 숫자, 공백으로 구분): ")
    user_numbers = list(map(int, user_input.split()))
    print(f"사용자 입력 번호: {user_numbers}")
    lotto_numbers = generate_lotto_numbers()
    print(f"로또 번호: {lotto_numbers}")
    
    matched_count, matched_numbers = check_lotto_numbers(user_numbers, lotto_numbers)
    print(f"맞춘 번호 개수: {matched_count}, 맞춘 번호: {matched_numbers}")


#lotto_simulation()


# switch-case 문
Prints.PrintLine("Match")

def simple_match(x):
    match x:
        case 1:
            return "One"
        case 2:
            return "Two"
        
def coordinate(point):
    match point:
        case (0, 0):
            return "zero point"
        