# id посылки 8153836

'''

Тренажёр для скоростной печати

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой
строке. Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.

'''

def max_score(keystrokes_per_player, number_or_players, keys_to_push):
    key_counts = {}
    max_keystrokes = keystrokes_per_player * number_or_players
    score = 0

    for i in range(len(keys_to_push)):
        key_counts[keys_to_push[i]] = key_counts.get(keys_to_push[i], 0) + 1

    for value in key_counts.values():
        if value <= max_keystrokes:
            score += 1
    
    return score


if __name__ == '__main__':
    keystrokes_per_player = int(input())
    input_game_sequence = ''
    for _ in range(4):
        input_game_sequence += input()
    keys_to_push = [key for key in input_game_sequence if key != '.']

    print(max_score(keystrokes_per_player, keys_to_push))
