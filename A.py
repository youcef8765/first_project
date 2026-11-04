import sys
import math
from math import sqrt


def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def devid(x, y):
    if y != 0:
        return x / y
    else:
        print('error')

print('''0-addintion
1-subtraction
2-multiplation
3-devide
4-second_degree_function''')

operation = input("choose one: ")


if operation == '0':
    a = int(input("A = "))
    b = int(input("B = "))
    answer = add(a, b)
elif operation == '1':
    a = int(input("A = "))
    b = int(input("B = "))
    answer = sub(a, b)
elif operation == '2':
    a = int(input("A = "))
    b = int(input("B = "))
    answer = mult(a, b)
elif operation == '3':
    a = int(input("A = "))
    b = int(input("B = "))
    answer = devid(a, b)
elif operation == '4':
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))
    delta = (b ** 2) - 4 * a * c
    if delta > 0:
        x_1 = (-b - sqrt(int(delta))) / (2 * a)
        x_2 = (-b + sqrt(int(delta))) / (2 * a)
        answer = 'x_1= ', x_1, 'x_2 = ' , x_2
    elif delta == 0:
        x_1 = (-b) / (2 * a)
        answer = 'x_1 = ', x_1
    elif delta < 0:
        print("we dont use complex number yet, try something else")
        sys.exit()
    else:
        sys.exit()
        
else:
    print(f'error ==> there is no {operation} in the list')
    sys.exit()


print(f"your answeris > {answer} <")




