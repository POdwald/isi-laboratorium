import random
import string

def generate_passwords(file_path, num_passwords):
    with open(file_path, 'w') as file:
        for _ in range(num_passwords):
            password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
            file.write(password + '\n')


if __name__ == '__main__':
    file_path = 'passwords.txt'
    num_passwords = 1000

    generate_passwords(file_path, num_passwords)
    print(f"Pomyślnie wygenerowano i zapisano {num_passwords} losowych haseł do pliku '{file_path}'.")