def solution(num, k):
    idx = str(num).find(str(k))
    return idx + 1 if idx >= 0 else idx

print(solution(123456, 7))