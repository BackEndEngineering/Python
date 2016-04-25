import random
master = open("/usr/share/dict/words")
dictionary = master.read()
dictionary = dictionary.lower().split()
player_score = 0
computer_score = 0
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
    ]

def hangedman(hangman):
    graphic = [
"""
 ------
 |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
         ,____
              |---.\
      ___     |    `
     / .-\  ./=)
    |  |"|_/\/|
    ;  |-;| /_|     YOUR DEAD !!!
   / \_| |/ \ |
  /      \/\( |
  |   /  |` ) |
  /   \ _/    |
 /--._/  \    |
 `/|)    |    /
   /     |   |
 .'      |   |
/         \  |
(_.-.__.__./  /

"""]
    print(graphic[hangman])

def normal_words(
    word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    normal_word_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            normal_word_list.append(word)
    return normal_word_list


def medium_words(
    word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 10:
            medium_word_list.append(word)
    return medium_word_list


def nightmare_words(
    word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    nightmare_word_list = []
    for word in word_list:
        if len(word) >= 10:
            nightmare_word_list.append(word)
    return nightmare_word_list


def random_word(
    word_list):
    """
    Returns a random word from the word list.
    """
    correct_word = random.choice(word_list)
    return correct_word


def display_word(
    word, guesses):

    progress_display = []
    for letter in word:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display


def is_word_complete(
    word, guesses):

    progress = display_word(word, guesses)
    if '_' in progress:
        return False
    else:
        return True


def get_level():
    level = input("""
    888888888888888888888888888888888888888888888888888888888888888888888
    88        (8)                                                      88
    88       (8)                                                       88
    88        (8)               Welcome to HANGMAN                     88
    88       (8)             Do have the guts to Play?                 88
    88        (8)            If You said "YES", I have a               88
    88       (8)                   Secret Word!                        88
    88       (8))        What difficulty setting do you want?          88
    88       (8)        Please enter normal, medium or nightmare.      88
    88      (8)(8)                                                     88
    88     (8)'`(8)                                                    88
    88    (8)    (8)                                                   88
    88    (8)    (8)                                                   88
    88    (8)    (8)                                                   88
    88    (8)    (8)                                                   88
    88     (8)  (8)                                                    88
    88      (8)(8)                                                     88
    88       `""`                                                      88
    88                                                                 88
    88                                                                 88
    88                                                                 88
    88                                                                 88
    888888888888888888888888888888888888888888888888888888888888888888888
    \n""")
    level = level.lower()
    if level == 'normal':
        answer = random_word(normal_words(dictionary))
    elif level == 'medium':
        answer = random_word(medium_words(dictionary))
    elif level == 'nightmare':
        answer = random_word(nightmare_words(dictionary))
    return answer


def gameplay_loop(
    answer):
    guesses = []
    fails = 0
    hangedman(fails)
    print("The word you're looking for has {} letters.".format(len(answer)))
    while is_word_complete(answer, guesses) == False:
        this_guess = (input("Okay, take a guess!\n")).lower()
        if len(this_guess) > 1:
            print("Not a valid guess. One letter only.")
        elif this_guess not in guesses:
            if this_guess not in answer:
                print("That letter isn't in your word.")
                fails += 1
                hangedman(fails)
                if this_guess not in alphabet:
                    print("Letter already been used.")
                else:
                    alphabet.remove(this_guess)
                    print("Letters Remaining")
                    print(alphabet)
            else:
                if this_guess in alphabet:
                    alphabet.remove(this_guess)
                    print("Letters Remaining")
                    print(alphabet)
                    print("Nice! That letter is in your word!")
        else:
            print("You already guessed that!")
        guesses.append(this_guess)
        print(display_word(answer, guesses))
        print("These are your guesses so far: {}".format(guesses))
        print("You have {} guesses left.\n".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        play_again_lose = input(("You lose! The word was {}. If you want to play again, enter yes.\n".format(answer)))
        play_again_lose.lower()
        if play_again_lose == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")
    else:
        play_again_win = input(("You won! If you want to play again, enter yes.\n"))
        play_again_win.lower()
        if play_again_win == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")


def main():
    answer = get_level()
    return gameplay_loop(answer)


if __name__ == '__main__':
    main()
