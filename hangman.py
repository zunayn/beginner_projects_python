"""
### HANGMAN GAME IN PYTHON ###

Simple game in python, does the following:

1. Choose a random word from words.txt

2. Prompt user to guess letters of the word, provided he gets 6 tries,
until all tries are exhausted, or the word has been successfully guessed.

3. Prompt user to play the game again.



Made by: Zunayn Nazir
"""


def welcome():
    greeting = "WELCOME TO HANGMAN".center(50)
    print(f"\n {greeting} \n".center(200, "="))

    intro = """
    HANGMAN is a word guessing game where the computer will guess
    a random english word and you will have to guess it.
    """

    how_to = """
    HOW TO GUESS : You'll be prompted to guess one letter of the
    hidden word. If the word you guessed was right, you can move on.
    You'll also get to know the position of your guessed letter in the
    hidden word.
    """

    tries = """
    You'll be given 6 tries for a guess and you can keep going
    as long as you haven't exhuasted all your guesses.
    """

    outro = """It's a fun game! Just keep your head open."""

    print(intro, tries, how_to, outro)
    print("\n\nSO, THE COMPUTER JUST CHOSE A WORD, AND IT'S YOUR TIME TO GUESS IT. \n\n")


def make_list(file):
    """
    Read a file object, and store all the
    words in a list and return the list.

    file: text file containing
    one word on each line.
    """
    words = []

    for line in file:
        word = line.strip()

        words.append(word)

    return words


def random_word(file):
    """
    Choose a random word from file and return it lowercased.

    file: text file containing
    one word on each line.
    """

    import random

    word_list = make_list(file)
    word = random.choice(word_list)

    return word.lower()



def guess_letter(word, cracked, not_cracked):
    """
    Prompt user to guess a letter, return if the guess was valid.

    Check validity by comparing the elements in 'cracked' and
    'not_cracked' i.e the guess is only valid if it has not been cracked
    yet.


    word: a word string.

    cracked: list of length == len(word) containing elements of 'word' cracked,
    and stars for elements not cracked.

    not_cracked: list containing elements of 'word' not cracked.
    """

    print()
    print("Hidden word: ", "".join(cracked))

    guess = input("Guess >> ").lower()

    if guess in not_cracked:
        ind = word.index(guess)

        if guess in cracked:
            ind = word.index(guess, ind+1)

        cracked[ind] = guess
        not_cracked.remove(guess)

        return True

    else:
        print("Incorrect Guess!")
        return False



def check_win(word, cracked):
    """
    Check if elements in word == elements in cracked, display result
    and ask user to play again.

    word: word string.

    cracked: list of length == len(word) containing elements of 'word' cracked,
    and stars for elements not been cracked.
    """

    cracked_word = "".join(cracked)
    print()

    if cracked_word == word:
        print("YOU WON! CONGRATS")
    else:
        print("YOU LOST! GOOD LUCK NEXT TIME.")

    play_again()


def play_again():
    """
    Ask user to play the game again.
    """

    print("\nDo you want to play again?")
    choice = input("Y/N?").lower()

    if choice.startswith("y"):
        main()
    else:
        print("\nThanks for playing!")


def main():

    welcome()

    with open("words.txt") as f:
        randword = random_word(f)

    not_cracked = list(randword)
    cracked = ["*"] * len(randword)
    tries = 6

    while ("*" in cracked) and (tries > 0):

        right_guess = guess_letter(randword, cracked, not_cracked)

        if not right_guess:
            tries -= 1
        else:
            tries = 6

        print(f"Tries left: {tries}")

    else:
        check_win(randword, cracked)



if __name__ == "__main__":
    main()
