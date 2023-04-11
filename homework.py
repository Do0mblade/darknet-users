s = input('Введите строку: ')
is_alphabetical = True
for i in range(len(s)-1):
    if ord(s[i]) > ord(s[i+1]):
        is_alphabetical = False
        break
print(is_alphabetical)