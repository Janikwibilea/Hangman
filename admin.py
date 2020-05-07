from modules import time, sys, init, Fore, classes
init(autoreset=True)


def input_secret_word():
    secret_word = input("Input a secret Word: ")
    secret_word.lower()
    global word_level
    word_level = len(secret_word)
    session_admin.write_file("{},{}".format(secret_word, word_level))
    print("The secret word is: {}. It's a word from level: {}.".format(secret_word, word_level))

def user_stats():
    # Importing stats from session_admin.txt
    # Import: "Eingabeliste", "Remaining Tries", "All letters inputed", "Is word Correct (Bool)"
    did_game_end = False
    session_admin.open_file("r")
    while not did_game_end:
        session_admin.open_file("r")
        import_session = session_admin.file.readline().split(';')
        session_admin.close_file()
        print(import_session)
        try:
            input_list = import_session[0]
            remaining_tries = import_session[1]
            all_letters_tried = import_session[2]
            check_game_state = import_session[3]
            if check_game_state == "True":
                did_game_end = True
            print("\n\n\n\n\n\nWord: {} \nRemaining tries: {}\nAll letters tried: {}\nDid Game End?{}".format(str(input_list), str(remaining_tries), str(all_letters_tried), str(did_game_end)))
            time.sleep(1)
        except IndexError:
            print("IndexError")  # TODO Zeile entfernen wenn alles funktioniert
            time.sleep(1)
    session_admin.close_file()
    get_results(input_list, remaining_tries)

def get_results(input_list, remaining_tries):
    # Get the results from the user (import from session_admin.txt)
    print("\n\n\nUser {} won the Game".format(".."))  # TODO User name
    print("Word: {} \nRemaining tries: {}".format(input_list, remaining_tries))

def end_game():
    # Print options
    # Play again?
    return False

def hangman_admin_main():
    print(Fore.BLUE + "Welcome to Hangman (Admin Panel)")
    user_name = input(Fore.BLUE + "Please enter a Username: ")
    global session_admin
    session_admin = classes.manage_session("session.txt", user_name)
    session_admin.start_admin()
    session_admin.waiting_for_user()
    input_secret_word()
    user_stats()
    if end_game():
        hangman_admin_main()

hangman_admin_main()