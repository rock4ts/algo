'''
https://contest.yandex.ru/contest/23389/problems/J/

Факторизация

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.052 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.4 секунды	64Mb
Python 3.7.3	0.2 секунды	64Mb
OpenJDK Java 11	0.4 секунды	64Mb
C# (MS .NET 6.0 + ASP)	0.4 секунды	64Mb
Kotlin 1.8.0 (JRE 11)	0.4 секунды	64Mb
C# (MS .NET 5.0 + ASP)	0.4 секунды	64Mb

Основная теорема арифметики говорит:
любое число раскладывается на произведение простых множителей единственным образом,
с точностью до их перестановки.
Например:

Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.

Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

Формат вывода
Выведите в порядке неубывания простые множители, на которые раскладывается число n.

Пример 1
Ввод	Вывод
8       2 2 2
Пример 2
Ввод	Вывод
13      13
Пример 3
Ввод	Вывод
100     2 2 5 5
'''

from math import sqrt


def factors(n):
    factors = []
    j = 2

    while n > 1:
        for i in range(j, int(sqrt(n)) + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
        else:
            factors.append(n)
            break
    
    return factors


def main():
    n = int(input())
    print(' '.join([str(f) for f in factors(n)]))


if __name__ == '__main__':
    main()
