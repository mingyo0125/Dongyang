#if 문
a = 10;
if(a > 5):
    print("a is greater than 5");
else:
    print("a is less than or equal to 5");


# and or not
condition1 = True;
condition2 = False;

if(condition1 and condition2):
    print("Both conditions are True");
elif(condition1 or condition2):
    print("At least one condition is True");
elif(not condition1):
    print("condition1 is False");


# for 문
for i in range(5):
    print(i);

countries = ["Korea", "USA", "China"];
for country in countries:
    print(country);


# while 문
i = 0;
while(i < 5):
    print(i);
    i += 1;


# random
import random;
print(random.randint(1, 10)); # 1 ~ 10


# list
fruits = ["apple", "banana", "cherry"];
print(fruits[0]); # apple
print(fruits[1]); # banana
print(fruits[2]); # cherry
print(fruits[-1]); # cherry

# 튜플과 다르게 리스트는 변경 가능
fruits[0] = "orange"; # apple -> orange
print(fruits); # ['orange', 'banana', 'cherry']

# list slicing
print(fruits[0:2]); # ['orange', 'banana']

# list 연결
fruits2 = ["kiwi", "mango"];
fruits3 = fruits + fruits2; # ['orange', 'banana', 'cherry', 'kiwi', 'mango']

# orange 제거
del fruits3[0]; # ['banana', 'cherry', 'kiwi', 'mango']


# tuple
# 튜플은 변경 불가능한 리스트
fruits = ("apple", "banana", "cherry");
print(fruits[0]); # apple
print(fruits[1]); # banana
print(fruits[2]); # cherry
print(fruits[-1]); # cherry


# dictionary
# key-value 쌍으로 이루어진 데이터 구조
fruits = {"apple": 100, "banana": 200, "cherry": 300};

print(fruits["apple"]); # 100
fruits["banana"] = 150; # banana의 값을 200 -> 150으로 변경

del fruits["banana"]; # banana 삭제


# set
# 중복을 허용하지 않는 데이터 구조
# 순서가 없고, 인덱스가 없음
fruits = {"apple", "banana", "cherry"};
print(fruits); # {'banana', 'cherry', 'apple'}
fruits.add("orange") # {'banana', 'cherry', 'apple', 'orange'}
fruits.remove("banana"); # {'cherry', 'apple', 'orange'}

# remove와 discard의 차이: remove는 없으면 에러 발생, discard는 에러 발생 안함
fruits.discard("banana"); # {'cherry', 'apple', 'orange'} 

# set union, intersection, difference
set1 = {1, 2, 3};
set2 = {3, 4, 5};
print(set1.union(set2)); # {1, 2, 3, 4, 5}
print(set1 | set2); # {1, 2, 3, 4, 5}

print(set1 & set2); # {3}
print(set1.intersection(set2)); # {3}

print(set1 - set2); # {1, 2}
print(set1.difference(set2)); # {1, 2}


#zip
# 두 개 이상의 리스트를 묶어주는 함수
list1 = [1, 2, 3];
list2 = ["a", "b", "c"];
list3 = list(zip(list1, list2)); # [(1, 'a'), (2, 'b'), (3, 'c')]
print(list3); # [(1, 'a'), (2, 'b'), (3, 'c')]

# enumerate
# 리스트의 인덱스와 값을 함께 반환하는 함수
list1 = ["a", "b", "c"];
for index, value in enumerate(list1):
    print(index, value); # 0 a, 1 b, 2 c