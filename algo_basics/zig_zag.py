'''
https://contest.yandex.ru/contest/26365/problems/B/

"Застёжка-молния"

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны два массива чисел длины n. Составьте из них один массив длины 2n, в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...). При этом относительный порядок следования чисел из одного массива должен быть сохранён.

Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 1 ≤ n ≤ 1000.

Во второй строке записано n чисел из первого массива, через пробел.

В третьей строке –— n чисел из второго массива.

Значения всех чисел –— натуральные и не превосходят 1000.

Формат вывода
Выведите 2n чисел из объединённого массива через пробел.
'''

with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, a, b = [row.strip().split() for row in input_f.readlines()]
    zig_zag = list()
    for i in range(int(n[0])):
        zig_zag.extend([a[i], b[i]])
    output_f.write(' '.join(zig_zag))
