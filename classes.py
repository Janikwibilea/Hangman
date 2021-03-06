from modules import time, sys, Fore, init
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

    def start_admin(self):
        self.write_file('"Waiting for Player...", "Username of Admin: {}", 0'.format(self.user_name))
        print(Fore.BLUE + "Game Created, waiting for other Player")
    
    def start_user(self):
        self.open_file("r")
        self.admin_name = self.file.readline().split(',')[1]
        self.close_file()
        self.write_file('"User joined", "Name of User: {}", 1'.format(self.user_name))
        print(Fore.BLUE + "Game joined, waiting for Admin")

    def state(self):
        try:
            self.open_file("r")
            self.session_state = int(self.file.readline().split(',')[2])
            self.close_file()
            return self.session_state
        except IndexError:
            time.sleep(1)
            self.state()

    def waiting_for_user(self):
        user_is_ready = False
        while user_is_ready == False:
            if self.state() == 1:
                print(Fore.GREEN + "User is ready")
                user_is_ready = True
            elif self.state() == 0:
                print(Fore.YELLOW + "User is not ready")
                time.sleep(1)
            else:
                print(Fore.RED + "Something went wrong, exiting Hangman")
                sys.exit(0)
        self.open_file("r")
        self.name_of_user = self.file.readline().split(',')[1]
        self.close_file()


