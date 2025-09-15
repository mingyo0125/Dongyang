# 집합 실습

def line(title):
    print("\n" + "=" * 50);
    print(title);
    print("=" * 50);

def end():
    input("\n▶ 계속하려면 Enter 키를 누르세요...");

#1 단계: 기본 집합 만들기
def step1():
    line("1단계: 집합 생성과 중복 제거하기");

    colors = ["red", "blue", "green", "red", "yellow", "blue"];
    print(f"원본 리스트: {colors}");

    unique_colors = set(colors);  # 중복 제거
    print(f"중복 제거된 집합: {unique_colors}");

    end();

def step2():
    line("2단계: 집합 연산");

    set_a = {"apple", "banana", "cherry", "kiwi"};
    set_b = {"banana", "cheery", "orange", "fig", "grape"};
    print(f"집합 A: {set_a}");
    print(f"집합 B: {set_b}");

    print(f"합집합 A|B: {set_a | set_b}");
    print(f"교집합 A&B: {set_a & set_b}");
    print(f"차집합 A-B: {set_a - set_b}");
    print(f"대칭차집합 A^B: {set_a ^ set_b}");

    end();

def step3():
    line("3단계: 집합 메소드 연습");

    fruits = set();
    print(f"현재 과일 집합: {fruits}");

    fruits.add("apple");
    fruits.add("banana");
    print(f"추가 이후: {fruits}");

    fruits.update(["kiwi", "orange", "apple"]);
    print(f"kiwi, orange, apple update 이후: {fruits}");

    fruits.discard("banana");
    print(f"banana 삭제 이후: {fruits}");

    fruits.clear();
    print(f"모든 과일 삭제 이후: {fruits}");

    end();







#zip 실습

def step1_zip():
    line("zip 기본 사용법");

    list1 = ["호날두", "신지드", "샘 해밍턴"];
    list2 = [1, 2, 3];

    print(f"리스트1: {list1}");
    print(f"리스트2: {list2}");

    zipped = zip(list1, list2);
    print(f"zip 결과: {list(zipped)}");

    end();


# enumerate 실습
def step1_enumerate():
    line("enumerate 기본 사용법");

    fruits = ["apple", "banana", "cherry"];
    print(f"과일 리스트: {fruits}");

    for index, fruit in enumerate(fruits):
        print(f"인덱스: {index}");
        print(f"과일: {fruit}");




def run_them():
    step1();
    step2();
    step3();
    step1_zip();
    step1_enumerate();
    print("\n");

run_them();