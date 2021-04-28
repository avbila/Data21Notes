from hangman_words import word_list
import random

# Functions:


def get_letter_from_user(used_letters):
    while True:
        letter = input("Please input your letter:  ")
        if letter in used_letters:
            print(f"The letter {letter}  has been used before.\nPlease select a new letter.")
        else:
            break
    return letter


def get_name_from_player():
    while True:
        player_name = input('Please Enter Your Name: \n')
        if player_name.isalpha():
            break
        else:
            print("Incorrect entry !\nPlease Enter Your First Name only.")
    return player_name


def hangman_graphics(strikes):
    """Outputs a graphic of a hangman."""
    if strikes == 0:
        print(" ___\n|   |\n|   \n|   \n|   \n|   ")
    elif strikes == 1:
        print(" ___\n|   |\n|   0\n|   \n|   \n|   ")
    elif strikes == 2:
        print(" ___\n|   |\n|   0\n|   |\n|   \n|   ")
    elif strikes == 3:
        print(" ___\n|   |\n|   0\n|  /|\n|   \n|   ")
    elif strikes == 4:
        print(" ___\n|   |\n|   0\n|  /|\\\n|   \n|   ")
    elif strikes == 5:
        print(" ___\n|   |\n|   0\n|  /|\\\n|  / \n|   ")
    elif strikes == 6:
        print(" ___\n|   |\n|   0\n|  /|\\\n|  / \\\n|   ")


def hangman_game():
    available_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    used_letters = []
    strikes = 0
    name = get_name_from_player()
    word = word_list[random.randint(0, len(word_list) - 1)].upper()
    separator = ""

    while True:
        print("\n"*10)
        displayed_word = []
        for index in range(len(word)):
            if word[index] in used_letters:
                displayed_word.append(word[index]+" ")
            else:
                displayed_word.append("_ ")
        hangman_graphics(strikes)
        print(separator.join(displayed_word))
        if displayed_word.count("_ ") == 0:
            print(f"congratulations! You Won {name}!!!")
            break
        print(f"Available Letters:\n{available_letters}")
        print(f"Previously Selected Letters:\n{used_letters}")
        letter_guess = get_letter_from_user(used_letters)
        available_letters.remove(letter_guess)
        used_letters.append(letter_guess)
        if letter_guess not in list(word.upper()):
            strikes += 1
        if strikes == 6:
            print("\n" * 10)
            hangman_graphics(strikes)
            print(f"Sorry {name}. You have lost.")
            break


while True:
    hangman_game()
    print("Thank you for playing.")
    replay = input("Would you like to play again?[Y|N]   ")
    if replay == "N":
        break
