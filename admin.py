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
    
    def start(self):
        self.open_file("w")
        self.file.write('"Waiting for Player...", "Username of Admin: {}", 0'.format(self.user_name))
        self.close_file()

    def state(self):
        self.open_file("r")
        self.session_state = int(self.file.readline().split(',')[2])
        self.close_file()
        return self.session_state

def waiting_for_user():
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

def hangman_main():
    print(Fore.BLUE + "Welcome to Hangman")
    user_name = input(Fore.BLUE + "Please enter a Username: ")
    global session
    session = manage_session("connection_files/session.txt", user_name)
    session.start()
    



hangman_main()