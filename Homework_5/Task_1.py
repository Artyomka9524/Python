# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def random_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        let = sample(alp, 3)
        words_list.append("".join(let
        ))
    return " ".join(words_list)

def simple_sentence(words: str) -> str:
    return " ".join(words.replace("абв", "").split())

all_list = random_words(int(input("ВВедите количество: ")))
print(all_list)
print(simple_sentence(all_list))