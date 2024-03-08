import random

def cw10():
    target_number = random.randint(1, 100)
    while True:
        guess = int(input('Wprowadz liczbe: '))
        if guess < target_number:
            print('Za mala liczba!\n')
        elif guess > target_number:
            print('Za duza liczba!\n')
        else:
            print('Woooow super, zgadles\n')
            break


if __name__ == '__main__':
    cw10()