import random

lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        number = random.choice(lst)
    Left = []
    Middle = []
    Right = []
    for i in lst:
        if i < number:
            Left.append(i)
        elif i > number:
            Right.append(i)
        else:
            Middle.append(i)
    return quick_sort(Left) + Middle + quick_sort(Right)

mas = quick_sort(lst)

print(mas)

def min(mas):
    return mas[0]

print(min(mas))

def max(mas):
    return mas[-1]

print(max(mas))

if __name__ == '__main__':
    pass
