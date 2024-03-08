def cw1():
    user_input = input('Wprowadz tekst: ')
    return user_input[::-1]

if __name__ == '__main__':
    result = cw1()
    print(result)