won, ex_rate = 2500000, 1430.8;

### 1. 문자열 포맷팅
print("{} 원은 ${}달러 입니다.".format(won, won/ex_rate));
print("{:12d} 원은 ${:0.3f}달러 입니다.".format(won, won/ex_rate));
print("{1:} 원은 ${0:}달러 입니다.".format(won, won/ex_rate));

### 2. f-string
print(f"{won} 원은 ${won/ex_rate}달러 입니다.");

### 3. % 포맷팅
print("%d 원은 $%0.2f달러 입니다." % (won, won/ex_rate));

### ------------------------------------------------------------------------

### 5. 힘수

def Method():
    return 10;

def CToF(c):
    return c * 9/5 + 32;

def FToC(f):
    return (f - 32) * 5/9;

celsius = float(input("섭씨 온도를 입력하세요: "));
print(f"섭씨 {celsius}도는 화씨 {CToF(celsius)}도 입니다.");

### 6. lamda 함수
(lambda: print("Lambda 함수는 이름이 없는 함수입니다."))();
func1 = lambda x: x * 9/5 + 32;
print(f"섭씨 {celsius}도는 화씨 {func1(celsius)}도 입니다.");

mul = lambda x, y: x * y;
x,y = int(input()), int(input());
print(f"{x} * {y} = {mul(x, y)}");

pl = {("basic", 1964, 5), ("java", 1995, 2), ("kotlin", 2016, 7), ("python", 1991, 1), ("C", 1972, 3)};
print(sorted(pl, key = lambda year: year[1]));

### ------------------------------------------------------------------------

### 7. if 조건문

### ------------------------------------------------------------------------

### 8. for 반복문
print("for 반복문");
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i * j}");


### ------------------------------------------------------------------------

### 8. while 반복문
start = 1;
num = start;
end = 10;
print("while 반복문");
while (num <= end):
    print(f"2 * {num} = {2 * num}");
    num += 1;