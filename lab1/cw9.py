def cw9():
    user_input = input('Wprowadz slowo/zdanie: ')
    user_input = user_input.lower()
    return user_input == user_input[::-1]

if __name__ == '__main__':
    result = cw9()
    print(result)