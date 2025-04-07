
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

print(capitalize_text(some_text))


# Task 2
'''
Створіть функцію word_count, яка приймає рядок тексту і повертає кількість слів у цьому тексті.
Вважайте словами будь-яку послідовність символів, розділених пробілом. 
Напишіть тести для перевірки роботу функції на різних вхідних текстах.
'''
def word_count(text: str):

    x = len([k for k in text.split()])

    return x


print(word_count('rrr 123 rerer, rwr , к '))



