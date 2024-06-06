import random

def sum(a, b):
    return a + b
print('sum(1, 2): ', sum(1, 2))

def getRandomNumber():
    number = random.randint(1, 10)
    return number
print('getRandomNumber(): ', getRandomNumber())

def printName(name):
    print('printName(): ', name)
printName('Miles')

def sayHello():
    print('Hello World')
sayHello()

def sub(a: int, b: int) -> int:
    return a - b
print('sub(4, 1): ', sub(4, 1))
