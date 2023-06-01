word1 = input('Введите слово1')
word2 = input('Введите слово2')

if word1 == word2:
    print(True)
elif abs(len(word1) - len(word2)) > 1:
    print(False)
else:
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    i = 0
    count = 0
    while i < len(word1):
        if word1 == word2[:i] + word2[i+1:]:
            if count > 1:
                print(False)
                break
    else:
        print(True)
 