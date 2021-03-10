s = input('введите строку')
index=2
s=s[:index]+s[index+1:]

s=s[:-1]
n=len(s)
print(s)
print('длина строки:')
print(n)
s=s.lower()
world=s.split(" ")
for w in world:
    n = w.find('с')
    if n!=-1:
        print( str(w) +' - ' + 'В двнной строке присутствует буква с')





