# Задание 6
# Проверка на «почти палиндром»
# Напишите программу, которая проверяет, является ли строка палиндромом или «почти палиндромом».
# «Почти палиндром» означает, что можно удалить одну букву, чтобы строка стала палиндромом.


# Функция проверки на палиндром
def is_palindrome(string):
    return string == string[::-1]


# Функция проверки строки. Определяет является ли строка палиндромом, «почти палиндромом» или не палиндром
def is_almost_palindrome(string):
    if is_palindrome(string):
        return 'Палиндром'
    for i in range(len(string)):
        sub_str = string[:i] + string[i+1:]
        if is_palindrome(sub_str):
            return 'Почти палиндром'
    return 'Не палиндром'

str_list = ['aabaa', 'abcba', 'aabaaa', 'abacaba', 'abacab', 'abcdefg']

for string in str_list:
    print(string, '->', is_almost_palindrome(string))