def is_palindrom(text):
    
    text = ''.join(char.lower() for char in text if char.isalnum())
    if text == text[::-1]:
        return True
    
    return False


def main():
    text = input()
    print(is_palindrom(text))


if __name__ == '__main__':
    main()
