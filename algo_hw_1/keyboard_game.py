# id посылки 81538365

def max_score(keystrokes_per_person, keys):
    key_counts = {}
    max_keystrokes = keystrokes_per_person * 2
    score = 0

    for i in range(len(keys)):
        key_counts[keys[i]] = key_counts.get(keys[i], 0) + 1

    for value in key_counts.values():
        if value <= max_keystrokes:
            score += 1
    
    return score


if __name__ == '__main__':
    keystrokes_per_person = int(input())
    input_game_sequence = ''
    for _ in range(4):
        input_game_sequence += input()
    keys = [key for key in input_game_sequence if key != '.']

    print(max_score(keystrokes_per_person, keys))
