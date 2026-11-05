import sys
import math

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

if operation in ('0', '1', '2', '3'):
    a = float(input('A = '))
    b = float(input('B = '))
elif operation == '4':
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    
if operation == '0':
    answer = round(add(a, b), 3)
elif operation == '1':
    answer = round(sub(a, b), 3)
elif operation == '2':
    answer = round(mult(a, b), 3)
elif operation == '3':
    answer = round(devid(a, b), 3)
elif operation == '4':
    if a != 0:
        delta = (b ** 2) - (4 * a * c)
        if delta > 0:
            x_1 = (-b - math.sqrt(int(delta))) / (2 * a)
            x_2 = (-b + math.sqrt(int(delta))) / (2 * a)
            answer = 'x_1= ', round(x_1, 3), 'x_2 = ' , round(x_2, 3)
        elif delta == 0:
            x_1 = (-b) / (2 * a)
            answer = 'x_1 = ', round(x_1, 3)
        elif delta < 0:
            print("we dont use complex number yet, try something else")
            sys.exit()
        else:
            sys.exit()
    else:
        print('error')
        sys.exit()    
else:
    print(f'error ==> there is no {operation} in the list')
    sys.exit()

if delta > 0:
    print(f'delta = {delta} > 0')
else:
    print(f'delta = {delta} < 0')
print(f"your answeris > {answer} <")