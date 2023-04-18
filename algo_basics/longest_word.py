def longest_word(words):
    longest_word = ''
    longest_word_length = 0
    
    for word in words:
        current_word_len = len(word)
        if current_word_len > longest_word_length:
            longest_word = word
            longest_word_length = current_word_len
    
    return longest_word, str(longest_word_length)


def main():
    text_len = int(input())
    words = input().split()
    
    print('\n'.join(longest_word(words)))


if __name__ == '__main__':
    main()
