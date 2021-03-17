print('введите до 10 слов')
lat=input(' введите список:')  # создаем первый список
b=len(lat.split(' '))
print('количество слов:', b)
g = set(lat)
print(g)

lon=input(' введите второй список :') #создаем второй список слов
c=len(lon.split(' '))
print('количество слов:', c)
g = set(lon)
print(g)

if (b!=c):       #надо убедиться равно ли количество слов в 2-х списках
    print('количество слов не равно в 2 списках')
else:
    print('количество слов равно в 2-х списках')
    words=lat.split(',')
    words1=lon.split(',')
    print("словарь")   #создаем словарь
    d={ }
    d={words[0]:words1[0], words[1]:words1[1], words[2]:words1[2]}
    print(d)
