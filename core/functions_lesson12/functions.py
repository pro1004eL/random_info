
# Task 1
'''
Напишіть функцію capitalize_text, яка приймає рядок тексту і повертає цей же текст,
але з першою великою і іншими маленькими літерами для кожного слова.
Вхідні дані: good Bad UGLY
Вихідні: Good Bad Ugly
'''


def capitalize_text(text: str) -> str:
    if text == '':
        raise AttributeError
    return text.title()

some_text = 'good Bad UGLY'

# print(capitalize_text(some_text))


# Task 2
'''
Створіть функцію word_count, яка приймає рядок тексту і повертає кількість слів у цьому тексті.
Вважайте словами будь-яку послідовність символів, розділених пробілом. 
Напишіть тести для перевірки роботу функції на різних вхідних текстах.
'''
def word_count(text: str):

    x = len([k for k in text.split()])

    return x

# print(word_count('rrr 123 rerer, rwr , к '))


# Task 3

some_list = [1, 2, 3,4,5,6,7,8, '123']

def check_if_all_el_is_num(list1: list):

    k = all([type(k) == int for k in list1])

    if k == True:
        k2 = [k2 for k2 in list1 if k2 % 2 != 0]

        return k2
    else:
        return 'Not all elements in the list have integer type'


print(check_if_all_el_is_num(some_list))














