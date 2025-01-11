# Задание 7
# Задача Шредингера
# Разработайте программу, которая «стирает» фрагменты текста в файле. Например:
#
# Пользователь указывает файл и процент текста, который нужно удалить (например, 30%).
# Программа случайно выбирает слова или части абзацев и заменяет их на пробел или ..., сохраняя общий объем документа.
# Вход:
# «Сегодня солнечный день, и я собираюсь гулять в парке с моими друзьями.»
#
# Вывод (удалено ~30%):
# «Сегодня ... день, и я собираюсь гулять ... моими друзьями.»

import random


def remove_text(file_name, percent):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    num_words = len(words)
    num_remove = int(num_words * percent / 100)
    indexes = list(range(0, num_words-1))
    random.shuffle(indexes)
    for i in range(num_remove):
        index = indexes[i]
        words[index] = '...'

    new_text = ' '.join(words)

    print(new_text)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(new_text)

remove_text('text.txt', 30)
