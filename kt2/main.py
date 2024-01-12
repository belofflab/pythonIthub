import random

def load_wordlist() -> list:
    wordlist = []
    wlines = open("words_list.txt", "r", encoding="utf-8").readlines()
    for line in wlines:
        parsed_line = line.split(" - ")
        wordlist.append({
            "word": parsed_line[0].lower(),
            "description": parsed_line[-1].strip()
        })
    return wordlist

def choose_word(wordlist: list) -> dict:
    return random.choice(wordlist)

def load_hangman_stage(stage) -> str:
    file_path = f"hangman{stage}.txt"
    with open(file_path, "r") as file:
        return file.read()

def display_word(word: str, guessed_letters: list) -> str:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main() -> None:
    wordlist = load_wordlist()
    word_obj = choose_word(wordlist=wordlist)
    word_to_guess = word_obj["word"]
    word_to_guess_description = word_obj["description"]
    guessed_letters = []
    tried_letters = []
    # max_attempts = len(word_to_guess)
    max_attempts = 5
    attempts = 0

    while True:
        print("Описание: ", word_to_guess_description)
        print("\n" + load_hangman_stage(attempts))
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Угадайте букву: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"Вы уже угадали эту букву. Попробуйте другую.")
                continue
            if guess in tried_letters:
                print(f"Вы уже пробовали эту букву. Попробуйте другую.")
                continue

            if guess not in word_to_guess:
                attempts += 1
                tried_letters.append(guess)
                print("Неправильно!")
            else:
                guessed_letters.append(guess)
                print("Правильно!")

            if set(guessed_letters) == set(word_to_guess):
                print("Поздравляю, вы угадали слово!")
                break

            if attempts >= max_attempts:
                print("\n" + load_hangman_stage(attempts))
                print("Вы проиграли. Загаданное слово:", word_to_guess)
                break

        else:
            print("Введите корректную букву.")

if __name__ == "__main__":
    main()
