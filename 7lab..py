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
    c = random.randrange(0,100)
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
        # проверяем условие равенства списков
if b != c:
        print('количество слов не равно между собой')
else:
        print('количество слов равно')
        print('создадим соварь')
        d={ }
        for a,b in zip(words,words1):
                d[a]=b
                print(d)

