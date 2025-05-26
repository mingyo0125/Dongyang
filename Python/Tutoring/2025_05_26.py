import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils import Prints
from Utils import Calculator

import turtle


def Total(*numbers):
    value = sum(numbers)
    print(value)

Total(1, 2, 3, 4)

def asd(**asd):
    print(asd.items())
asd(a = "asd")

addLamda = lambda x, y: x + y
print(addLamda(1, 2))

Prints.PrintLine("패키지와 모듈")

turtle.speed(10)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.circle(50, 360)

for i in range(5):
    turtle.forward(-100)
    turtle.right(144)
turtle.done()


print(Calculator.add(1, 2))
print(Calculator.minus(1, 2))
print(Calculator.multiply(2, 2))


