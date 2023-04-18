
keyboard_dict = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def combinations(keys, prefix):
    if not keys:
        print(prefix, end=" ")
    else:
        key = int(keys[0])
        for letter in keyboard_dict[key]:
            combinations(keys[1:], prefix + letter)


if __name__ == '__main__':
    keys = input()
    prefix = ''
    combinations(keys, prefix)
