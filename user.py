from modules import time, sys, Fore, init, cl
init(autoreset=True)


def hangman_user_main():
    print(Fore.BLUE + "Welcome to Hangman (User Panel)")
    user_name = input(Fore.BLUE + "Please enter a Username: ")
    global session_user
    session_user = cl.manage_session("session.txt", user_name)
    session_user.start()
    session_user.user_is_ready()



hangman_user_main()