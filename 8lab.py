file=open('6lab.py','w+')
print(file.read()) #чтение файла
file.write(" один:десять, два:девять,три:восемь") #запись в файл
print('я на позиции:',file.tell())

# возвращаемся в начало
file.seek(0)
print('я на позиции:',file.tell())
file.close() #закрытие файла
