from modules import time, sys, Fore, init, classes, datetime
init(autoreset=True)


def hangman_user_main():
    print(Fore.BLUE + "Welcome to Hangman (User Panel)")
    user_name = input(Fore.BLUE + "Please enter a Username: ")
    global session_user
    session_user = classes.manage_session("session.txt", user_name)
    wait_for_admin()
    wait_for_secret_word()

def wait_for_admin():
    if session_user.state() == 0:
        session_user.start_user()   
    else:
        time.sleep(1)
        wait_for_admin()

def wait_for_secret_word():
    try:
        session_user.file.readline().split(',')[2]
        time.sleep(1)
    except IndexError:
        secret_word = session_user.file.readline().split(',')[0]
        word_level = session_user.file.readline().split(',')[1]

    secret_word_split = []

    for i in secret_word:
        secret_word_split.append(i)

    input_list = []

    for i in range(0, word_level):
        input_list.append("x")

    global user_fails
    user_fails = 0
    global user_tries
    user_tries = word_level * 2
    user_input(input_list, secret_word, secret_word_split)

def user_input(input_list, secret_word, secret_word_split):
    global user_fails
    global user_tries
    global letters_tried
    letters_tried = []
    session_user.write_file("{}, {}, {}, {}".format(input_list, user_tries, letters_tried))
    userinput = input("\n\n\nEnter a letter:\n")
    userinput.lower()
    if userinput not in letters_tried:
        letters_tried.append(userinput)
    else:
        print(Fore.RED + "The letter has already been tried")
        user_input(input_list, secret_word, secret_word_split)

    if userinput in secret_word:
        correctletter(secret_word, userinput, input_list, secret_word_split)
    else:
        print(Fore.RED + "Letter not in there\n")
        print(input_list)
        user_tries -= 1
        user_fails += 1
    if user_tries > 0:
        user_input(input_list, secret_word, secret_word_split)
    else:
        loser(secret_word)


def correctletter(secret_word, userinput, input_list, secret_word_split):
    global counter
    for i in range(0, len(secret_word_split)):
        if secret_word_split[i] == userinput:
            input_list[i] = str(userinput)
            print(Fore.GREEN + "Correct Letter")
            print(input_list)
            counter += 1
    if counter == len(secret_word_split):
        win()


def loser(secret_word):
    print(Fore.RED + "You lost, the solution is: " + secret_word + "\n\n\n")
    time.sleep(3)


def win():
    global user_tries
    print(Fore.GREEN + "\n\n\nYou have won\n" + "Your number of mistakes: " + str(user_fails) + "\n\n")
    #timenow = datetime.now()
    time.sleep(3)
    #addtoleaderboard(timenow)
    #hangman_main()

hangman_user_main()