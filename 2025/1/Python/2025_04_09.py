li = list({1,2,3,4,5,6});
print(li);

b = bytes(b'hi');

# 문자 슬라이싱
print('python'[5:6:1]);

season = ["Spring", "Summer", "Fall", "Winter"]
print(season[2:3])
print(season[0:2])
season[0:2]= "봄", "여름"
print(season[0:2])
print(season[1:3])
print(season[-4:-1])

print(season[-3:1])

"""
=으로 복사하면 얕은복사(참조를 함)
슬라이싱[:] 이나 list, copy로 복사하면 깊은 복사(참조를 안 하고 새로 만듦)
"""

"""
id = input("아이디를 입력하세요: ");
idx = id.find("@")
id2 = id[0] + "*" * (id.index("@")-1) + id[id.index("@"):]
print("결과: ", id2);
"""
