from random import random, randint
import sys
import time


def hangman_main():
    print("Welcome to Hangman:\n 1 to Play Hangman\n 2 to show Leaderboard\n 3 to exit Programm")
    mode = int(input("\n"))
    if mode == 1:
        play_hangman()
    elif mode == 2:
        leaderboard()
    elif mode == 3:
        sys.exit(0)
    else:
        print("Eingabe Fehler\n\n\n")
        time.sleep(2)
        hangman_main()


def play_hangman():
    print("\n\n\n1: Play Hangman\n\n\n")
    print("Wie lange soll dein Wort sein?(3-8)\n")
    try:
        level = int(input(""))
    except ValueError:
        play_hangman()

    if level in range(3, 9):
        pass
    else:
        print("Geben sie ein gültiges Level an")

    file = open("wordlist.txt", "r")
    wortliste_lvl = []

    for word in file:
        word = word.strip()
        if len(word) == level:
            wortliste_lvl.append(word)
    file.close()

    secret_word = wortliste_lvl[randint(0, len(wortliste_lvl))]
    print(secret_word)

    secret_word_split = []

    for i in secret_word:
        secret_word_split.append(i)

    eingabeliste = []

    for i in range(0, level):
        eingabeliste.append(i)
        
    userputin = input("\n\n\nGeben sie einen Buchstaben ein:\n")

def check_input():
    pass

def leaderboard():
    l = []


hangman_main()
