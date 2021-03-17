my_file = open('6lab.py', 'w+')
print('имя файла:', my_file.name)
# запись в файл
my_file.write("один:десять,два:девять,три:восемь")
# чтение файла
string = my_file.read()

print(string)
print('я на позиции:', my_file.tell())

# возвращаемся в начало
my_file.seek(0)
print('я на позиции:', my_file.tell())
# закрытие файла
my_file.close()
