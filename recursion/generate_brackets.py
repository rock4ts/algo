
def generate_brackets(seq_len, count_open=0, prefix=''):

    if count_open > seq_len or count_open < 0:
        return
    elif seq_len == 0:
        print(prefix)
    else:
        generate_brackets(seq_len - 1, count_open + 1, prefix + '(')
        generate_brackets(seq_len - 1, count_open - 1, prefix + ')')


if __name__ == '__main__':
    seq_len = int(input()) * 2

    generate_brackets(seq_len)
