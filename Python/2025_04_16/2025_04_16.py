# dict

# 리터럴 방식
sdic = {"name": "John", "age": 30, "city": "New York"};

# dict() 생성자 방식
sdic = dict(name="John", age=30, city="New York");

# fromkeys() 메서드 사용
# 모든 키에 대해 동일한 값을 설정
sdic2 = dict.fromkeys(["name", "age", "city"], "Unknown");

# setdefault: 주어진 키가 딕셔너리에 존재하지 않으면 그 키를 지정한 기본값으로 추가하고, 이미 존재하는 경우에는 해당 키의 값을 반환
sdic2.setdefault("name", "Unknown");

# update: 키가 기존 딕셔너리에 있으면 그 값을 덮어쓰고, 없으면 새로운 키-값 쌍이 추가
sdic.update(sdic2);

# 두 개의 딕셔너리 병합
sdic3 = {**sdic, **sdic2};

# 딕셔너리에서 value가 큰 값의 키를 찾기
max(sdic, key= sdic.get);

#-------------------------------------------------------------------------------------

# set 정렬 안 되고 중복 안 됨
set1 = {1, 2, 3, 4, 5};
# 추가할때는 Add, 지울때는 remove
# discard: remove와 비슷하지만, remove는 없는 값을 지우려고 하면 에러가 나지만 discard는 에러가 안남

#-------------------------------------------------------------------------------------
A = {1, 2, 3}
B = {3, 4, 5}

# 합집합: 두 집합 A와 B의 모든 원소를 합친 집합
union_set = A | B  # 또는 A.union(B)
print(union_set)  # {1, 2, 3, 4, 5}


# 교집합: 두 집합 A와 B에 공통으로 존재하는 원소들
intersection_set = A & B  # 또는 A.intersection(B)
print(intersection_set)  # {3}


# 차집합: 집합 A에만 존재하는 원소들
difference_set = A - B  # 또는 A.difference(B)
print(difference_set)  # {1, 2}


# 대칭 차집합: 집합 A와 B에 대해 서로 다른 원소들
symmetric_difference_set = A ^ B  # 또는 A.symmetric_difference(B)
print(symmetric_difference_set)  # {1, 2, 4, 5}

#-------------------------------------------------------------------------------------

#zip
# zip은 iterable한 객체를 묶어주는 역할
zipelem = zip([1, 2, 3], ['a', 'b', 'c']);

# zip을 사용하여 두 개의 리스트를 묶어 딕셔너리로 변환
zip_dict = dict(zipelem);
print(zip_dict);  # {1: 'a', 2: 'b', 3: 'c'}

zipelem2 = zip([1, 2, 3], range(5), ['a', 'b', 'c']);
# zip을 사용하여 세 개의 리스트를 묶어 딕셔너리로 변환
zip_dict2 = list(zipelem2);
print(zip_dict2);  # [(1, 0, 'a'), (2, 1, 'b'), (3, 2, 'c')]

#-------------------------------------------------------------------------------------

# enumerate: iterable한 객체를 인덱스와 함께 반환

# 예시 리스트
fruits = ["apple", "banana", "cherry"]

# enumerate를 사용하여 인덱스와 값을 동시에 출력
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Value: {fruit}")