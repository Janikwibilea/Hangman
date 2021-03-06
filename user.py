from modules import time, sys, Fore, init, classes, datetime
init(autoreset=True)

global counter
counter = 0

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
    session_user.open_file("r")
    import_session = session_user.file.readline().split(',')
    while len(import_session) >= 3:
        session_user.close_file()
        session_user.open_file("r")
        import_session = session_user.file.readline().split(',')
        time.sleep(1)
    session_user.close_file()
    global secret_word
    global word_level
    secret_word = import_session[0]
    word_level = import_session[1]
    global secret_word_split
    secret_word_split = []

    for i in secret_word.lower():
        secret_word_split.append(i)

    global input_list
    input_list = []

    for i in range(0, int(word_level)):
        input_list.append("_")

    global user_fails
    user_fails = 0
    global user_tries
    user_tries = int(word_level) * 2
    global letters_tried
    letters_tried = []
    user_input(input_list, secret_word, secret_word_split)

def user_input(input_list, secret_word, secret_word_split):
    global user_fails
    global user_tries
    global letters_tried
    session_user.write_file("{}; {}; {}; {}".format(input_list, user_tries, letters_tried, False))
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
    if int(user_tries) > 0:
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
    session_user.write_file("{}, {}, {}, {}".format(input_list, user_tries, letters_tried, False))
    print(Fore.RED + "You lost, the solution is: " + secret_word + "\n\n\n")
    time.sleep(3)


def win():
    session_user.write_file("{}, {}, {}, {}".format(input_list, user_tries, letters_tried, True))
    print(Fore.GREEN + "\n\n\nYou have won\n" + "Your number of mistakes: " + str(user_fails) + "\n\n")
    #timenow = datetime.now()
    time.sleep(3)
    #addtoleaderboard(timenow)
    #hangman_main()
    sys.exit(0)

hangman_user_main()