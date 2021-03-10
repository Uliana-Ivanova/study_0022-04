import math
import random
choise=input('''Введите наименование операции которую нужно осуществить
+ сложение;  - вычитание;  * умножение;  / деление;   arccos арккосинус; 
 random рандом от 0 до 100;   ** возведение в степень;   mod модуль;  ! факториал''')


if choise == '+':
     num_1=int(input('введите 1 число'))
     num_2=int(input('введите 2 число'))
     print(num_1+num_2)
elif choise =='-':
     num_1 = int(input('введите 1 число'))
     num_2 = int(input('введите 2 число'))
     print(num_1 - num_2)
elif choise =='*':
     num_1 = int(input('введите 1 число'))
     num_2 = int(input('введите 2 число'))
     print(num_1 * num_2)
elif choise =='/':
     num_1 = int(input('введите 1 число'))
     num_2 = int(input('введите 2 число'))
     print(num_1 / num_2)
elif choise =='**':
     num_1 = int(input('введите 1 число'))
     num_2 = int(input('введите 2 число'))
     print(num_1 ** num_2)
elif choise =='random':
     print("случайное число")
     print(random.randint(0,100))
elif choise =='arccos':
     n = float(input('введите 1 число'))
     n=rad = n*math.pi/180
     ac=math.acos(n-rad)
     print('arccos=',ac)
elif choise == '!':
     num_1 = int(input('введите 1 число'))
     print(("факториал числа",math.factorial(num_1)))
elif choise =='mod':
     num = int(input('введите 1 число'))
     b = abs(num)
     print(b)


