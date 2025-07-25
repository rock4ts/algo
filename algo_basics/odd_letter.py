'''
https://contest.yandex.ru/contest/23389/problems/L/

Лишняя буква

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод	Вывод
abcd    e
abcde

Пример 2
Ввод	Вывод
go      g
ogg

Пример 3
Ввод	Вывод
xtkpx   c
xkctpx
'''

def get_odd_letter(initial_text, modified_text):
    initial_ord_sum = sum(ord(char) for char in initial_text)
    modified_ord_sum = sum(ord(char) for char in modified_text)
    odd_letter_ord = modified_ord_sum - initial_ord_sum

    return chr(odd_letter_ord)


def main():
    initial_text, modified_text = input(), input()
    print(get_odd_letter(initial_text, modified_text))


if __name__ == '__main__':
    main()
