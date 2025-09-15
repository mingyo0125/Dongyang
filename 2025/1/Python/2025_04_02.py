import random # random 함수를 쓰기 위한 import

# 1. 랜덤 int 생성
random.randint(1, 100)

st = "asd";
st.strip(); # 공백 제거

"""

iterable : 반복 가능한 것(for 가능). list, tuple, str, set, dict
sequence: 순서를 가진 것(인덱스로 접근 가능). list, tuple, str
collction: 원소들이 모여 있는 것 길이가 존재함. set, list, tuple, set, dict
"""

# ------------------------------------------------------------------------

# 2. 퀴즈 게임
# dict를 사용하여 질문과 정답을 저장
# for문을 사용하여 질문을 반복
# if 문을 사용하여 정답 여부 판별
def QuizGame():
    question_list = {};

    for i in range(3):
        ques = input("질문을 입력하세요: ");
        ans = input("정답을 입력하세요: ");
        question_list[ques] = ans;

    for i in range(len(question_list)):
        ques = list(question_list.keys())[i];
        answer = question_list[ques];
        print(f"{i+1}번 문제: {ques}");
        inputAns = input("정답을 입력하세요: ");
        if inputAns.strip().lower == answer:
            print("정답입니다.");
        else:
            print(f"오답입니다. 정답은 {answer}입니다.");


# ------------------------------------------------------------------------

# 3. 숫자 맞추기 게임
# lambda 함수를 사용하여 1~50사이의 난수 생성
# while 문을 사용하여 사용자가 정답을 맞출 때까지 반복
# if 문을 사용하여 힌트 제공 (숫자가 크거나 작은지 안내)

def GuessNumberGame():
    GetRandomNumber = lambda: random.randint(1, 50);
    while(True):
        num = GetRandomNumber();
        print("1~50 사이의 숫자를 맞춰보세요.");
        while True:
            guess = int(input("숫자를 입력하세요: "));
            if guess == num:
                print("정답입니다.");
                break;
            elif guess < num:
                print("너무 작습니다.");
            else:
                print("너무 큽니다.");
        again = input("다시 하시겠습니까? (y/n): ");
        if again.strip().lower() != 'y':
            break;
# ------------------------------------------------------------------------

# 메뉴 시스템 (while문 활용)
# 사용자가 원하는 게임을 선택할 수 있도록 구성
# 0을 입력하면 프로그램 종료

while(True):
    print("1. 퀴즈 게임, 2. 숫자 맞추기 게임, 0. 종료");
    choice = int(input("원하는 게임을 선택하세요: "));
    if choice == 1:
        QuizGame();
    elif choice == 2:
        GuessNumberGame();
    elif choice == 0:
        print("프로그램을 종료합니다.");
        break;

# ------------------------------------------------------------------------

str = "Hello World";
str.capitalize(); # 첫 글자만 대문자로
str.upper(); # 모두 대문자로
str.lower(); # 모두 소문자로
str.title(); # 각 단어의 첫 글자만 대문자로
str.swapcase(); # 대문자는 소문자로, 소문자는 대문자로
str.casefold(); # 소문자로 변환