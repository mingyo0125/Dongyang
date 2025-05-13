import Utils


Utils.PrintLine("점수 평균 계산기")

# *: 가변인자(튜플), **: 가변 키워드 인자(딕셔너리)
def weighted_average(*scores, **weights):
    sum = 0
    idx = 0
    for i in weights.values():
        sum += scores[idx] * i
        idx += 1
    return sum


print(weighted_average(80,90,70, math = 0.5, english = 0.3, science = 0.2))

Utils.PrintLine("사용자 정보 출력 함수")

def show_user(name, age = 20, *hobbies, **details):
    print(f"이름: {name}")
    print(f"나이: {age}")
    print("취미:", ", ".join(hobbies))
    print("기타정보:", details)

show_user("Alice", 25, "Reading", "Gaming", city="Seoul", job = "Engineer")


Utils.PrintLine("압축 풀기 연산자")

def create_character(name, **custom_options):

    default_stats = {
        "strength" : 5,
        "agility": 5,
        "intelligence": 5,
        "weapon": "wooden sword"
    }

    final_stats = {**default_stats, **custom_options}

    print(f"캐릭터 이름: {name}")
    print("능력치: ")
    for i, j in final_stats.items():
        print(f"{i}, {j}")

option1 = {"strength": 10, "weapon": "Siu"}
option2 = {"agility": 12, "intelligence": 8}

create_character("호날두", **option1)
print()
create_character("신지드", **option2)

Utils.PrintLine("특수 매개변수")

# 특수 매개변수
def greet(name, /, greeting="안녕"): # name은 위치 전용 매개변수
    print(f"{greeting}, {name}님")

greet("민수")                # 가능
greet("지민", greeting="하이")  # 가능
# greet(name="지민")         # 불가능: name은 키워드 인자로 사용 불가


Utils.PrintLine("인코더와 디코더")

def create_encoder(secret_key):
    def encode(message):
        encoded = ""
        for char in message:
            encoded += chr(ord(char) + secret_key)
        return encoded
    return encode

def create_decoder(secret_key):
    def decode(message):
        decoded = ""
        for char in message:
            decoded += chr(ord(char) - secret_key)
        return decoded
    return decode

e = create_encoder(3)
d = create_decoder(3)

origin = "Hello"
encoded = e(origin)
decoded = d(encoded)

print("원본:", origin)
print("인코딩:", encoded)
print("디코딩:", decoded)
