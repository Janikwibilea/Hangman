from modules import *
init(autoreset=True)

def hangman_main():
    print(Fore.YELLOW + "Welcome to Hangman:\n 1 to Play Hangman\n 2 to show Leaderboard\n 3 to exit Programm")
    mode = int(input("\n"))
    if mode == 1:
        global counter
        counter = 0
        hangman_playmode()
    elif mode == 2:
        leaderboard()
    elif mode == 3:
        sys.exit(0)
    else:
        print(Fore.RED + "Enter a valid username\n\n\n")
        time.sleep(2)
        hangman_main()


def hangman_playmode():
    print(Fore.BLUE + "Which Hangman mode do you want to play?\n 1 Single Player\n 2 Multiplayer")
    mode = int(input("\n"))
    if mode == 1:
        play_hangman()
    elif mode == 2:
        user_mode()
    else:
        print(Fore.RED + "Enter a valid value\n\n\n")
        time.sleep(2)
        hangman_playmode()

def user_mode():
    print(Fore.BLUE + "Which user role you want to be?\n 1 Admin \n 2 User\n")
    mode = int(input("\n"))
    if mode == 1:
        hangman_admin_main()
    if mode == 2:
        hangman_user_main()
    else:
        print(Fore.RED + "Enter a valid value\n\n\n")
        time.sleep(2)
        user_mode()


def play_hangman():
    print("\n\n1: Play Hangman\n\n")
    print("How long should your word be?(3-8)\n")

    try:
        global level
        level = int(input(""))
    except ValueError:
        print(Fore.RED + "Enter a valid value")
        play_hangman()

    if level in range(3, 9):
        pass
    else:
        print(Fore.RED + "Choose a valid level")

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

    global fehler
    fehler = 0
    global versuche
    versuche = level * 2
    user_input(eingabeliste, secret_word, secret_word_split)


def user_input(eingabeliste, secret_word, secret_word_split):
    global versuche
    global fehler
    userinput = input("\n\n\nEnter a letter:\n")

    if userinput not in eingabeliste:
        pass
    else:
        print(Fore.RED + "The letter has already been tried")
        user_input(eingabeliste, secret_word, secret_word_split)

    if userinput in secret_word:
        correctletter(secret_word, userinput, eingabeliste, secret_word_split)
    else:
        print(Fore.RED + "Letter not in there\n")
        print(eingabeliste)
        versuche -= 1
        fehler += 1
    if versuche > 0:
        user_input(eingabeliste, secret_word, secret_word_split)
    else:
        loser(secret_word)


def correctletter(secret_word, userinput, eingabeliste, secret_word_split):
    global counter
    for i in range(0, len(secret_word_split)):
        if secret_word_split[i] == userinput:
            eingabeliste[i] = str(userinput)
            print(Fore.GREEN + "Correct Letter")
            print(eingabeliste)
            counter += 1
    if counter == len(secret_word_split):
        win()


def loser(secret_word):
    print(Fore.RED + "You lost, the solution is: " + secret_word + "\n\n\n")
    time.sleep(3)
    hangman_main()


def win():
    global fehler
    print(Fore.GREEN + "\n\n\nYou have won\n" + "Your number of mistakes: " + str(fehler) + "\n\n")
    timenow = datetime.now()
    time.sleep(3)
    addtoleaderboard(timenow)
    hangman_main()


def addtoleaderboard(timenow):
    global level
    global fehler
    with open("leaderboard.csv", "a", newline="") as file:
        write = csv.writer(file, delimiter=";")
        write.writerow([str(level), str(fehler), str(timenow.strftime("%Y-%m-%d %H:%M"))])


def leaderboard():
    with open("leaderboard.csv", "r") as file:
        x = from_csv(file)
        print(x)
    input("Back to menue\n")
    hangman_main()


hangman_main()
