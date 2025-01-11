# Задание 4
# Генератор случайных паролей
# Напишите функцию, которая генерирует пароль заданной длины. В реализации надо учитывать, что:
# Пароль должен содержать буквы, цифры и специальные символы.
# Длина пароля задается пользователем.

import string
import random

# Метод, который генерирует пароль. Пароль не может содержать меньше трех символов
# и должен содержать буквы, цифры и специальные символы.
# Кол-во букв, цифр и спец. символов определяется случайным образом, но не может быть меньше 1, а общее кол-во символов
# не может превышать длину пароля.
# Порядок букв, цифр и спец. символов определяется случайным образом.
def generate_password(length):
    if length < 3:
        raise ValueError('Длина пароля должна быть больше или равна 3')
    special_char_qty = random.randint(1, length-2)
    digits_qty = random.randint(1, length-special_char_qty-1)
    letters_qty = length - special_char_qty - digits_qty
    chars = []
    chars += random.sample(string.ascii_letters, letters_qty)
    chars += random.sample(string.digits, digits_qty)
    chars += random.sample(string.punctuation, special_char_qty)
    random.shuffle(chars)
    return ''.join(chars)

# Тесты
len_list = [3,4,5,6,6,6,7,8,4,10]
for i in len_list:
    password = generate_password(i)
    print(i, '->', password, 'длина пароля', len(password))
