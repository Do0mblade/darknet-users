def is_alphabetical(s):
    for i in range(len(s)-1):
        if ord(s[i]) > ord(s[i+1]):
            return False
    return True

s = input('Введите строку: ')
print(is_alphabetical(s))