# Задание 3
# Хаотичные скобки
# Реализуйте функцию, которая проверяет, правильно ли расставлены скобки в строке
# (включая круглые, квадратные и фигурные скобки).

# Карта соответствия открывающихся скобок закрывающимся.
brackets_map = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def is_correct_brackets(string):
    stack = []
    for character in string:
        if character in brackets_map.keys():
            stack.append(character)
        elif character in brackets_map.values():
            if not stack:
                return False
            if character != brackets_map[stack.pop()]:
                return False
    return not stack


# Тесты
str_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    'aaaaa(aaavaaf)asds{(asd)}',
    'asasd{asda()sdas}]',
    ''
]

for i in str_list:
    print(i, '->', is_correct_brackets(i))
