# Write your code here
import random

list_ = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N")


def play_game():
    global list_
    riddle = random.choice(list_)
    riddle_set = set(riddle)
    riddle_hidden = "-" * len(riddle)
    riddle_list = list(riddle_hidden)
    typed = set()
    tries = 8
    while tries > 0:
        print("\n{}".format(riddle_hidden))
        letter = input("Input a letter: ")

        if len(letter) > 1:
            print("You should print a single letter")
            continue
        if not letter.isascii() or not letter.islower():
            print("It is not an ASCII lowercase letter")
            continue
        if letter in typed:
            print("You already typed this letter")
            continue
        else:
            typed.add(letter)

        if letter in riddle_set:
            for i in range(len(riddle)):
                if letter == riddle[i]:
                    riddle_list[i] = letter
                    riddle_hidden = "".join(riddle_list)
            if "-" not in riddle_hidden:
                print("\n{}".format(riddle_hidden))
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("No such letter in the word")
            tries -= 1
    else:
        print("You are hanged!")


while True:
    play_or_not = input('\nType "play" to play the game, "exit" to quit: ')
    if play_or_not == "play":
        play_game()
    elif play_or_not == "exit":
        break
