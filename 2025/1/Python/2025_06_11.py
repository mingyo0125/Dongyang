from typing import Union
from Utils import Prints

# set, tuple, int, str
# Union 타입이 달라도 가능
lst: list[Union[int, str]] = [{"aa", "bb"}, (5, 50, 500), 1, 2, 3, "3.14", "str"]

print(lst)


def match_dict(d):
    match d:
        case {"particular_key": particular_value}:
            return f"particular_key 와 {particular_value}가 매칭되었음"
        case {"특정 key": "특정 value"}:
            return "특정 key: 특정 value가 매칭되었습니다."
        case {200: "정상종료", "메시지": msg}:
            return f"정상 종료 되었음 ==> 메시지: {msg}"
        case {200: type, "메시지": msg}:
            return f"{type} 문제가 발생되었음 ==> 메시지: {msg}"
        case _:
            return "No match found!"

print(match_dict({"특정 key": "특정 value"}))
print(match_dict({"200": "정상종료", "메시지": "이 메시지가 출력된다면 정상종료"}))


def shape_description(shape):
    match shape:    
        case ("원", radius) if radius > 0:
            return f"반지름이 {radius}인 원"
        case ("정사각형", length) if length > 0:
            return f"한 변의 길이가 {length}인 정사각형"
        case ("직사각형", hori, verti) if hori > 0 & verti > 0:
            return f"{hori} X {verti} 크기의 직사각형"
        case _:
            return "No match"
        
print(shape_description(("원", 8)))

# 예외처리
Prints.PrintLine("예외처리")

try:
    print("예외가 발생하지 않음")
except Exception as ex:
    print(f"type: {type(ex)}: {ex} 예외가 발생하였습니다")



def check_age(age):
    if age >= 18:
        return "성인입니다"
    else:
        return "나이가 18세 미만입니다"
    

def check_age_try(age):
    assert age >= 18, "나이가 18세 미만입니다"
    return "성인입니다"


# file
import sys

tw = open("sam.t", "w") #쓰기 모드

tw.write("Hi")

msg = tw.read()
tw.close()


import os
print(os.getcwd())    
