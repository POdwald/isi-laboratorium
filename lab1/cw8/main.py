import funkcje as f

def display_equation(numbers, sign):
    result = ''
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            sign = '='
        result += str(numbers[i]) + ' ' + sign + ' '
    return result

if __name__ == '__main__':
    numbers = [10, 2, 5]
    print(f'{display_equation(numbers, "+")}{f.dodawanie(numbers)}')
    print(f'{display_equation(numbers, "-")}{f.odejmowanie(numbers)}')
    print(f'{display_equation(numbers, "*")}{f.mnozenie(numbers)}')
    print(f'{display_equation(numbers, "/")}{f.dzielenie(numbers)}')