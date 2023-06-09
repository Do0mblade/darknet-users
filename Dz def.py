# Вы спрашиваете маленькую девочку: "Сколько тебе лет?"
# Она может ответить вам: "Мне x лет", где x - число от 0 до 9.

# Напишите скрипт, который находит цифру в строке (0-9) и вывожит на в виде целого числа.

# Например,
#   строка "Мне 6 лет" –> 6
#   строка "Мама говорит, что мне 3" –> 3
#   строка "Я ниняяю" –> None

# Допущение,
#  в строке всегда должна быть одна цифра!


s = input()  # вводим строку с числовым значением

def baby_age(s):
    l = len(s)             # значение длины введенной строки
    result = []            # результат (числовое значение), найденный из введенной строки (возраст)
    i = 0                  # начальное значение номера элемента в строке (первый элемент массива по сути)
    while i < l:           # пока номер элемента в строке меньше длины строки, мы входим в цикл и перебираем каждый следующий элемент
        s_res = ''         # пока пустое значение результата
        a = s[i]           # перебираем элементы массива, начиная с первого, а - это значение самого элемента в строке
        while '0' <= a <= '9':          # пока значение элемента больше или равно 0 или меньше или равно 9
            s_res += a                  # мы добавляем к результату этот элемент
            i += 1                      # и номер элемента массива прибавляется на один (то есть второй)
            if i < l:                   # если номер элемента все еще меньше длины строки
                a = s[i]                # то перебираем дальше
            else:
                break                   # иначе завершаем цикл
        i += 1                          # добавляем 1 к значению номера элемента
        if s_res != '':                 # если значение результата не пустое
            result.append(int(s_res))      # то добавляем результат в числовом значении

    if result == []:
        return 'None'
    else:
        return result[0]

print(baby_age(s))


if __name__ == '__main__':
    pass