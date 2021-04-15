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
         d={ }
        for a,b in zip(words,words1):
                d[a]=b
                print(d)
