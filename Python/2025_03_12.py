"""
print("안녕하세요");

name = "셜록 홈즈"
age = 40;
location = "런던 베이커가 221B";

clues = ["붉은 줄", "낡은 지도", "좌표 37.56, 126.97"];

num_of_clues = 3;

print("탐정이름:", name);
print("탐정나이:", age);
print("현재위치:", location);
print("보물 단서들:", clues);
print("단서 개수:", num_of_clues);

new_clue = "비밀의 암호"
clues.append(new_clue);

secret_message = "gninraeL nohtyP si nuf!";
decoded_message = secret_message[::-1];
print("해독된 메시지:" + decoded_message);
print("BoloRet".upper());


detective_name = "정민교";
clues = ["안녕하세요", "1", "2"];
print(f"{detective_name} 탐정의 보고서");
print(f"현재까지 발견한 단서들: {clues}");
print(f"총 단서 개수: {len(clues)}");

new_clue = input("새로운 단서를 입력하세요: ");
clues.append(new_clue);

print("업데이트된 단서 목록:", clues);
print(f"총 단서 개수: {len(clues)}");

"""

experiment_result = ["성공", "실패", "부분성공", "부분실패", "성공", "실패"];
unique_results = set(experiment_result);

print(f"{len(unique_results)} {unique_results}");

unique_results.add("예상 밖의 결과");
print(f"업데이트된 실험 결과: {unique_results}");

secret_codes = {
    "A1B2": "실험실 문 열기",
    "C3D4": "경보해제",
    "E5F6": "비밀 문서 열람"
}


if input() in secret_codes:
   print("asd")
else: print("dsa");