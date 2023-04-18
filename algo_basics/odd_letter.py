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
