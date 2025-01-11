# Задание 2 (2 балла)
# Напишите функцию, которая принимает строку и сжимает её определённым образом.
# Строки содержат произвольные символы, включая пробелы и спецсимволы, и требуют точного учета длины при кодировании.
# Сжатие строки происходит сериями одинаковых символов в формате символ + количество повторений в виде целого числа,
# но только если длина сжатой строки не превышает исходную.

# Метод, который сжимает строку
def compress_string(string):
    if len(string) < 2:
        return string
    char = string[0]
    count = 1
    result = ''
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            result += char
            if count > 1:
                result += str(count)
            char = string[i]
            count = 1
    result += char
    if count > 1:
        result += str(count)
    return result

# Тесты
str_list = ['2222222222','aaaabbbccc', 'abcc', 'abc', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaabbc', 'abcd', 'aabccaaacabbb','', '   asdasssss   ,;""221241@@@4121']

for i in str_list:
    compressed_str = compress_string(i)
    print(i, 'длина строки', len(i), '->', compressed_str, 'длина сжатой строки', len(compressed_str))