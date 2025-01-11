# Задание 1
# Обратный порядок слов в блоках текста
# Дан текстовый файл, каждое предложение которого занимает одну строку.
# Напишите программу, которая разделяет текст на блоки — каждый блок состоит из нескольких предложений.
# Затем переворачивает порядок слов только внутри каждого предложения, не меняя порядок самих предложений в блоке.

# Метод, который делит строку на блоки определенного размера.
# Если размер блока больше или равен длине строки, то второй блок будет пустым
def split_line_on_blocks(line, block_size):
    if len(line) <= block_size:
        return [line, '']
    else:
        result = []
        idx = 0
        while idx < len(line):
            result += [line[idx:idx + block_size]]
            idx += block_size
        return result


# Метод, который переворачивает слова в блоке и собирает их в строку
def reverse_string(block):
    result = ''
    for i in range(len(block) - 1, -1, -1):
        result += block[i]
        result += ' '
    result = result.strip()
    return result


# Читаем данные из файла по строкам и собираем их в список
with open('input.txt', 'r', encoding='utf-8') as input_data:
    str_list = [line.split() for line in input_data]

# Каждую строку из файла разбиваем на блоки и переворачиваем внутри блока.
for i, str in enumerate(str_list):
    blocks = split_line_on_blocks(str, i + 1)
    for block in blocks:
        print(reverse_string(block))
