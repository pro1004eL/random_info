


# Task 1
'''
Напишіть функцію capitalize_text, яка приймає рядок тексту і повертає цей же текст,
але з першою великою і іншими маленькими літерами для кожного слова.
Вхідні дані: good Bad UGLY
Вихідні: Good Bad Ugly
'''


def capitalize_text(text: str) -> str:

    if text == '':
        return ' '
    else:
        return text.title()

some_text = ['good Bad UGLY']

print(capitalize_text(some_text))




