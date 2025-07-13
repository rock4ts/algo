'''

https://contest.yandex.ru/contest/26365/problems/E/

"Две фишки - c сортировкой."

Все языки	GNU c++17 7.3
Ограничение времени	1 секунда	0.2 секунды
Ограничение памяти	256Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Обратите внимание на ограничения в этой задаче.

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 105.

Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».
'''

def twosum_sort(n, numbers, k):
    numbers.sort()
    left_ix = 0
    right_ix = n - 1
    
    while left_ix < right_ix:
        left_num = numbers[left_ix]
        right_num = numbers[right_ix]
        current_sum = left_num + right_num
        if current_sum == k:
            return f'{left_num} {right_num}'
        if current_sum < k:
            left_ix += 1
        else:
            right_ix -= 1
    return 'None'


with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, numbers, k = [row.strip() for row in input_f.readlines()]
    n, numbers, k = int(n), [int(num) for num in numbers.split()], int(k)
    output_f.write(twosum_sort(n, numbers, k))
