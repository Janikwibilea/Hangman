from modules import time, sys, Fore, init, classes
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
        # Import Secret Word
        pass

hangman_user_main()