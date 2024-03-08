def cw2():
    user_input = input('Wprowadz tekst: ')
    char_map = { 
        'o': '0',
        'i': '1',
        'e': '3',
        'a': '4'
    }
    result = ''.join(char_map.get(char, char) for char in user_input)
    return result

if __name__ == '__main__':
    result = cw2()
    print(result)