def solution(age):
    nums = []
    awns = []
    while(age > 0):
        nums.append(age / 10)
        age //= 10

    nums.reverse()

    for num in nums:
        print(num)
    return 1

solution(51)