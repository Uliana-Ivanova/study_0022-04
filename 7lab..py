import math
import random
choise = input('''Введите наименование операции которую нужно осуществить
+ сложение; 
- вычитание; 
* умножение; 
/ деление; 
arccos арккосинус; 
random рандом от 1 до 30; 
** возведение в степень;  
mod модуль; 
 ! факториал;
  5 - переделанная задача номер 5''')

# сложение чисел
if choise == '+':
   def umn(x, y):
       c = x+y
       return c
   x = int(input('введите число:'))
   y = int(input('введите число:'))
   c = umn(x, y)
   print(c)

# вычитание чисел
elif choise == '-':
    def umn(x, y):
        c = x - y
        return c
    x = int(input('введите число:'))
    y = int(input('введите число:'))
    c = umn(x, y)
    print(c)

# умножение чисел
elif choise == '*':
    def umn(x, y):
        c = x * y
        return c
    x = int(input('введите число:'))
    y = int(input('введите число:'))
    c = umn(x, y)
    print(c)

# деление чисел
elif choise == '/':
    def umn(x, y):
        c = x / y
        return c
    x = int(input('введите число:'))
    y = int(input('введите число:'))
    c = umn(x, y)
    print(c)

# возведение в степень
elif choise == '**':
    def umn(x, y):
        c = x ** y
        return c
    x = int(input('введите число:'))
    y = int(input('введите число:'))
    c = umn(x, y)
    print(c)

# поиск рандомного числа
elif choise == 'random':
    print('рандом от 1 до 30')
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    c = random.choice(l)
    print(c)

# поиск арккосинуса числа
elif choise == 'arccos':
    x = int(input('введите число:'))
    print("acos(x):", math.acos(x))

# нахождение модуля числа
elif choise == 'mod':
   x = int(input('введите 1 число'))
   print(math.fabs(x))

# нахождение факториала числа
elif choise == '!':
   x = int(input('введите 1 число'))
   print("факториал числа", math.factorial(x))

# решение 5 задачи с помощью функции
elif choise =='5':
    print('введите строку до 10 слов')
    list = input(' введите первую строку слов:')
    b = len(list.split(' '))
    print('количество слов:', b)
    g = set(list)
    print(g)

    list1 = input(' введите вторую строку слов:')
    c = len(list1.split(' '))
    print('количество слов:', c)
    g = set(list1)
    print(g)

    words = list.split(',')
    words1 = list1.split(',')

    if b != c:
        print('количество слов не равно между собой')
    else:
        print('количество слов равно')
        print('создадим соварь')
        d = {}
        d = {list[0]: list1[0], list[1]: list1[1], list[2]: list1[2], list[3]: list1[3], list[4]: list1[4],
             list[5]: list1[5], list[6]: list1[6], list[7]: list1[7], list[8]: list1[8], list[9]: list1[9]}
        # вывод словаря
        print(d)

