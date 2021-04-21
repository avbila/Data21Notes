# List of letters:
def isogram():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    phrase = input("Please enter your phrase:\n")
    phrase_lower_case = phrase.lower()  # Converting string to lower case letters
    for letter in letters:
        letter_count = phrase_lower_case.count(letter)
        if letter_count > 1:
            print(f"The {phrase} is not an isogram.")
            break
        elif letter == "z":
            print(f"The {phrase} is an isogram.")


# remove spaces and hyphens using .replace
# then compares size of string vs size of sets


# ----------------------------------------------------------------------------------------------------------------------
# Fizz Buzz:


def fizz_buzz(number):
    for x in range(1, number+1):
        if x % 3 == 0 and x % 5 == 0:
            print("Fizz Buzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)


# ----------------------------------------------------------------------------------------------------------------------
