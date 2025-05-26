def Total(*numbers):
    value = sum(numbers)
    print(value)

Total(1, 2, 3, 4)


def asd(**asd):
    print(asd.items())
asd(a = "asd")

addLamda = lambda x, y: x + y
print(addLamda(1, 2))
