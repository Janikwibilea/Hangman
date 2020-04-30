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
        self.file.write('["Waiting for Player", "{}"]'.format(self.user_name))
    

def hangman_main():
    print(Fore.BLUE + " Welcome to Hangman")
    user_name = input(Fore.YELLOW + "Please enter a Username: ")
    session = manage_session("connection_files/session.txt", user_name)
    session.start()

hangman_main()