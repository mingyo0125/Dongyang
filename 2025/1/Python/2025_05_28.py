from Utils import Prints

# 리스트 컴프리헨션(type: list)
Prints.PrintLine("리스트 컴프리헨션")
# 리스트 컴프리헨션을 사용하여 1부터 10까지의 제곱수를 구하는 코드
squares = [x**2 for x in range(1, 11)]
# 리스트 컴프리헨션을 사용하여 1부터 10까지의 짝수만 구하는 코드
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Squares:", squares)

getLetter = lambda x: "짝수" if x % 2 == 0 else "홀수"
_list = ["짝수" if x % 2 == 0 else "홀수" for x in range(1, 11)]
list2 = [getLetter(x) for x in range(1, 11)]
aa = lambda i : ["짝수" if x % 2 == 0 else "홀수" for x in range(1, i)]
print(aa(15))

# 딕셔너리 컴프리헨션 (type: dict)
Prints.PrintLine("딕셔너리 컴프리헨션")
# 딕셔너리 컴프리헨션을 사용하여 1부터 10까지의 제곱수를 구하는 코드
squares_dict = {x: x**2 for x in range(1, 11)}
print("Squares Dictionary:", squares_dict)


# 매핑 (type: map)
Prints.PrintLine("매핑")

add = lambda x, y: x + y
mapping = list(map(add, range(1, 11), range(11, 21)))
print("Mapped Values:", mapping)

# filter (type: filter)
Prints.PrintLine("필터")
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x >= 5, list_2))
print("Filtered List (Even Numbers):", filtered_list)

# generator (이터레이터의 한 종류) (type: generator)
# 반복가능 객체인 이터레이터를 만들어주는 함수
# return 문 대신 yield 문을 사용하여 값을 하나씩 반환
Prints.PrintLine("제너레이터")

def generator_example(n):
    for i in range(n):
        yield i

gen = generator_example(10)
while True:
    try:
        print(f"Generator Values: {next(gen)}")
    except StopIteration:
        break


# 제너레이터 표현식(type: generator)
Prints.PrintLine("제너레이터 표현식")

gen_expr = (x*1 for x in range(1, 11))
while True:
    try:
        print(f"Generator Expression Values: {next(gen_expr)}")
    except StopIteration:
        break


Prints.PrintLine("리스트와 제너레이터의 차이점")
# 심화 학습: 리스트와 제너레이터의 생성 시간과 메모리 사용 비교 
import time
import sys

# 시간 측정 함수
def measure_time_and_size(expression):
    start_time = time.time()
    obj = expression()
    elapsed_time = time.time() - start_time
    return elapsed_time, sys.getsizeof(obj)

# 리스트 컴프리헨션과 제너레이터 컴프리헨션 비교
list_time, list_size = measure_time_and_size(lambda: [x for x in range(1000000)])
gen_time, gen_size = measure_time_and_size(lambda: (x for x in range(1000000)))

# 결과 출력
print(f"리스트 컴프리헨션 - 시간: {list_time:.6f}초, 메모리: {list_size}바이트")
print(f"제너레이터 컴프리헨션 - 시간: {gen_time:.6f}초, 메모리: {gen_size}바이트")


students = {
    "Kim": [85, 90, 92],
    "Lee": [60, 65, 70],
    "Park": [75, 80, 82],
    "Choi": [50, 45, 60]
}


# 딕셔너리 컴프리헨션을 사용하여 학생들의 평균 점수를 계산하고, 70점 이상인 학생들만 필터링
student_dict = {name: sum(scores) / len(scores) for name, scores in students.items() if sum(scores) / len(scores) >= 70}
for name, avg in student_dict.items():
    print(f"{name}: {avg}")


# 리스트 컴프리헨션을 사용하여 단어의 길이가 4 이상인 단어를 대문자로 변환
input_text = input()
words = input_text.split()
word_lengths = [x.upper() for x in words if len(x) >= 4]
print(word_lengths)
