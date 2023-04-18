
def is_correct_bracket_seq(bracket_sequence):
    bracket_dict = {')': '(', ']': '[', '}': '{'}
    open_brackets_stack = []

    for elem in bracket_sequence:
        if elem in bracket_dict.values():
            open_brackets_stack.append(elem)
        elif open_brackets_stack:
            if not (bracket_dict[elem] == open_brackets_stack[-1]):
                return False
            open_brackets_stack.pop()
        else:
            return False

    if open_brackets_stack:
        return False
    return True


if __name__ == '__main__':
    bracket_sequence = input()

    print(is_correct_bracket_seq(bracket_sequence))
