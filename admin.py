from modules import *
init(autoreset=True)

class manage_session:
    def __init__(self, file_name, user_name):
        self.file_name = file_name
        self.user_name = user_name

    def open_file(self, mode):
        self.file = open(self.file_name, mode)

    def close_file(self):
        self.file.close()

    def write_file(self, text):
        self.open_file("w")
        self.file.write(text)
        self.close_file()

    def start(self):
        self.write_file('"Waiting for Player...", "Username of Admin: {}", 0'.format(self.user_name))
        print(Fore.BLUE + "Game Created, waiting for other Player")

    def state(self):
        self.open_file("r")
        self.session_state = int(self.file.readline().split(',')[2])
        self.close_file()
        return self.session_state

    def waiting_for_user(self):
        user_is_ready = False
        while user_is_ready == False:
            if session.state() == 1:
                print(Fore.GREEN + "User is ready")
                user_is_ready = True
            elif session.state() == 0:
                print(Fore.YELLOW + "User is not ready")
                time.sleep(1)
            else:
                print(Fore.RED + "Something went wrong, exiting Hangman")
                sys.exit(0)

def input_secret_word():
    global secret_word
    global word_level
    secret_word = input("Input a secret Word: ")
    word_level = len(secret_word)
    session.write_file("{}, {}".format(secret_word, word_level))
    print("The secret word is: {}. It's a word from level: {}.".format(secret_word, word_level))

def user_stats():
    # Importing stats from session.txt
    # Import: "Eingabeliste", "Remaining Tries", "All letters inputed", "Is word Correct (Bool)"
    did_game_end = False
    old_tries = word_level
    while not did_game_end:
        input_list = str(session.file.readline().split(',')[0])
        remaining_tries = int(session.file.readline().split(',')[1])
        all_letters_tried = str(session.file.readline().split(',')[2])
        did_game_end = bool(session.file.readline().split(',')[3])
        if old_tries != remaining_tries:
            old_tries = remaining_tries
            print("\n\n\n\n\n\nWord: {} \nRemaining tries: {}\nAll letters tried: {}\n".format(input_list, remaining_tries, all_letters_tried))
        time.sleep(1)
    get_results(input_list, remaining_tries)

def get_results(input_list, remaining_tries):
    # Get the results from the user (import from session.txt)
    print("\n\n\nUser {} won the Game".format("..")) # TODO User name
    print("Word: {} \nRemaining tries: {}".format(input_list, remaining_tries))

def end_game():
    #Print options
    # Play again?
    return False

def hangman_admin_main():
    print(Fore.BLUE + "Welcome to Hangman (Admin Panel)")
    user_name = input(Fore.BLUE + "Please enter a Username: ")
    global session
    session = manage_session("session.txt", user_name)
    session.start()
    session.waiting_for_user()
    input_secret_word()
    user_stats()
    if end_game():
        hangman_admin_main()



hangman_admin_main()