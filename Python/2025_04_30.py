import Utils

# 매개변수에 기본값을 설정할 수 있다
def Add(a = 1, b = 2):
    return a + b

Utils.PrintLine("클로저")
# 클로저
# 클로저는 함수 안에 정의된 함수를 의미한다
# 클로저는 외부 함수의 변수를 기억하기 때문에
# 외부 함수의 변수를 변경할 수 없다
def Calculator():
    total = 0
    def add(x):
        nonlocal total
        total += x
        return total
    return add
CalculatorIns = Calculator()
print(CalculatorIns(1)) # 1;
print(CalculatorIns(2)) # 3


Utils.PrintLine("키워드 인자")
# 키워드 인자
def Sub(a, b):
    return a - b
# 키워드 인자는 순서에 상관없이 전달할 수 있다
print(Sub(2, 1)) # 1
print(Sub(b = 2, a = 1)) # -1
# 위치 인자와 키워드 인자는 혼합해서 사용 가능하다.
print(Sub(1, b = 2)) # -1


Utils.PrintLine("가변 인자")
# 매개변수에 *을 붙이면 가변인자 (C# params)
# 가변인자는 튜플로 변환되어 전달됨
def Variable_length_args(*args):
    return sum(args)

# 가변 키워드 인자
# 가변 키워드 인자는 딕셔너리로 변환되어 전달됨
def Variable_length_args2(**kwargs):
    return kwargs

print(Variable_length_args(1, 2, 3)) # 6
print(Variable_length_args2(a = 1, b = 2)) # {'a': 1, 'b': 2}



Utils.PrintLine("예제")
orders = []

def add_order(int, *options, **special_requests):
    global orders
    order = {
        'int': int,
        'options': options,
        'special_requests': special_requests
    }
    orders.append(order)

def display_orders():
    global orders
    for i, order in enumerate(orders, 1):
        print(f"주문 {i}: ")
        print(f"항목: {order["item"]}")
        if order["options"]:
            print("옵션: ", ", ".join(order["options"]))
        if order["special_requests"]:
            print("특별 요청: ")
            for key, value in order["special_requests"].items():
                print(f"{key}: {value}")
        print("\n")

add_order("햄버거", "치즈 추가", "양상추 추가", extra_sauce="매운 소스")


Utils.PrintLine("Unpacking(압축 풀기) 연산자 *")

lst1 = [1,2]
lst2 = [3,4]
lst3 = [5,6]

# 리스트를 압축 풀기
# 압축 풀기 연산자 *을 사용하면 리스트를 압축 풀 수 있다
lst4 = [*lst1, *lst2, *lst3]
print(lst4) # [1, 2, 3, 4, 5, 6]

# 문자열 분해
s1 = [*"Hello"] # ['H', 'e', 'l', 'l', 'o']
    
# 대입 연산자 좌변에 *를 사용할 경우
# 대입 연산자 좌변에 *을 사용하면 나머지 요소를 리스트로 받을 수 있다
*a, b, c = lst4
print(f"a: {a}, b: {b}, c: {c}")