print('введите строку до 10 слов')
# введем первую строку слов
list = input(' введите первую строку слов:')
b = len(list.split(' '))
print('количество слов:', b)
g = set(list)
print(g)

# введем вторую строку слов
list1 = input(' введите вторую строку слов:')
c = len(list1.split(' '))
print('количество слов:', c)
g = set(list1)
print(g)

words = list.split(',')
words1 = list1.split(',')

# проверяем условие равенства списков
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
