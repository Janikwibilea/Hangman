from random import random, randint
import sys
import time
import csv



def hangman_main():
    print("Welcome to Hangman:\n 1 to Play Hangman\n 2 to show Leaderboard\n 3 to exit Programm")
    mode = int(input("\n"))
    if mode == 1:
        global counter
        counter = 0
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
        global level
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

    secret_word = wortliste_lvl[randint(0, len(wortliste_lvl))].lower()
    print(secret_word)

    secret_word_split = []

    for i in secret_word:
        secret_word_split.append(i)

    eingabeliste = []

    for i in range(0, level):
        eingabeliste.append("x")

    print(eingabeliste)

    global versuche
    versuche = level * 2
    user_input(eingabeliste, secret_word, secret_word_split)


def user_input(eingabeliste, secret_word, secret_word_split):
    global versuche
    userinput = input("\n\n\nGeben sie einen Buchstaben ein:\n")

    if userinput not in eingabeliste:
        pass
    else:
        print("Der Buchstabe wurde schon versucht")
        user_input(eingabeliste, secret_word, secret_word_split)

    if userinput in secret_word:
        correctletter(secret_word, userinput, eingabeliste, secret_word_split)
    else:
        print("nicht drin")
        print(eingabeliste)
        versuche -= 1
    if versuche > 0:
        user_input(eingabeliste, secret_word, secret_word_split)
    else:
        loser(secret_word)


def correctletter(secret_word, userinput, eingabeliste, secret_word_split):
    global counter
    for i in range(0, len(secret_word_split)):
        if secret_word_split[i] == userinput:
            eingabeliste[i] = str(userinput)
            print("Korrekt")
            print(eingabeliste)
            counter += 1
    if counter == len(secret_word_split):
        win()


def loser(secret_word):
    print("Du hast verloren " + secret_word)
    time.sleep(3)
    hangman_main()

def win():
    print("\n\n\nYou win\n\n\n")
    time.sleep(3)
    addToLeaderboard()
    hangman_main()


def addToLeaderboard():
    global level
    global versuche
    with open("leaderboard.csv", "a", newline="") as file:
        write = csv.writer(file, delimiter=";")
        write.writerow([str(level), str(versuche)])


def leaderboard():
    file = open("leaderboard.csv", "r")
    for i in file:
        print(i)
    file.close()
    input("Zurück zum Menü\n")
    hangman_main()


hangman_main()
