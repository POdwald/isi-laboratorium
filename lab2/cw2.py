import re

def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            cleaned_words = [word.strip(".,;?!") for word in words]  # W przypadku interpunkcji
            longest_word = max(cleaned_words, key=len)
            return longest_word
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None

if __name__ == '__main__':
    file_path = 'test.txt'
    longest_word = find_longest_word(file_path)
    if longest_word:
        print(f"Najdłuższy wyraz w pliku to: {longest_word}")


