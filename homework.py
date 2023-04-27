word1 = input('Введите слово1')
word2 = input('Введите слово2')
def check_words(word1, word2):
    if abs(len(word1) - len(word2)) >= 2:
        return False
    if word1 == word2:
        return True
    if len(word1) == len(word2):
        count_diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count_diff += 1
            if count_diff >= 2:
                return False
        return True
    if len(word1) > len(word2):
        return check_words(word2, word1)
    else:
        for i in range(len(word2)):
            if word1 == word2[:i] + word2[i+1:]:
                return True
        return False
print(check_words(word1, word2))

# C учетом условия, поправил свой вариант решения.
# Воспользовался множествами (см. презентации)
def mispelled(w1, w2):
    if len(set(w1) - set(w2)) <= 1:
        return True
    else: 
        return False
# Но это решение сработает не всегда. Просто привожу как вариант

# Это если ввиде функции. Но у нас задача записать пока без функции.
# Поэтому тебе задание написать решение этой задачи без применения функции def
# его надо добавить через git с локального устройства
