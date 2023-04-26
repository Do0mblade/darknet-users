s = input('Введите строку: ')
is_alphabetical = True
for i in range(len(s)-1):
    if ord(s[i]) > ord(s[i+1]):
        is_alphabetical = False
print(is_alphabetical)

# Супер)
# Теперь наша задача преобразовать данный код в функцию.
# Новое решение нужно добавить с помощью git с локального устройства
