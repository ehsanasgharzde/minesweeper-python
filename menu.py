from game import Game
from log import Log


class Menu:
    def __init__(self):
        self.log = Log()
        self.username = None
        self.isOn = True

    def introduction(self):
        print("""
        \n-------------------- Welcome to the Mine Sweeper Game! --------------------\n\n
        1. Your first goal is to reveal a good lump of 'safe' squares\n
        with just a few clicks,\n
        depending on the difficulty you are on.\n\n
        2. A square has 8 other squares neighborng it,\n
        If you click the square and see a number in it,\n
        it means we have that many bombs in the other 8 squares around\n\n
        3. If you are certian that a square contains the bomb,\n
        you cand flag it.\n\n
        4. You should choose whether you're going to 'step' in or 'flag' a square.\n
        You should Enter needed info to play like this: [action] [row] [column]\n
        >>> flag 2 3\n
        >>> step 9 1\n""")

    def main(self):
        if self.isOn:
            print("----- Login\n----- Signup\n----- Scoreboard\n----- Exit")

            option = input(">>> ").lower()
            while not option in ["login", "signup", "scoreboard", "exit"]:
                print("Invalid Command.")
                option = input(">>> ").lower()

            if option == "login":
                self.login()
            elif option == "signup":
                self.signup()
            elif option == "scoreboard":
                self.scoreboard()
            elif option == "exit":
                self.exit()

    def login(self):
        self.log.read()
        print("----- Login\n----- Signup\n----- Main Menu")

        option = input(">>> ").lower()
        while not option in ["login", "signup", "main menu"]:
            print("Invalid Command.")
            option = input(">>> ").lower()

        if option == "login":
            if self.isOn:
                exists = False
                while not exists:
                    self.username = input("Username: ")
                    if self.username in self.log.csv["username"].tolist():
                        exists = True
                        correct = False
                    else:
                        print("Username Does not Exist.")
                        print("----- Signup\n----- Try again")
                        
                        option = input(">>> ")
                        if option == "signup":
                            self.signup()
                        correct = True

                    while not correct:
                        password = input("Password: ")
                        if password == str(self.log.csv.loc[self.log.csv.username == self.username].password.item()):
                            correct = True
                            self.game()
                        else:
                            print("Wrong Password.")
                            print("----- Signup\n----- Try again")
                            
                            option = input(">>> ")
                            if option == "signup":
                                correct = True
                                self.signup()

            elif option == "signup":
                self.signup()
            elif option == "main menu":
                self.main()

    def signup(self):
        if self.isOn:
            self.log.read()
            print("----- Signup\n----- Main Menu")

            option = input(">>> ").lower()
            while not option in ["signup", "main menu"]:
                print("Invalid Command.")
                option = input(">>> ").lower()

            if option == "signup":
                exists = True
                while exists:
                    username = input("Username: ")
                    if not username in self.log.csv["username"].tolist():
                        exists = False
                        password = input("Password: ")
                        highscore = 0
                        self.log.append(username, password, highscore)

                        print("----- Login\n----- Main Menu")

                        option = input(">>> ").lower()
                        while not option in ["login", "signup", "main menu"]:
                            print("Invalid Command.")
                            option = input(">>> ").lower()
                        if option == "login":
                            self.login()
                        elif option == "main menu":
                            self.main()
                    else:
                        print("Username Exists.")
                        print("----- Login\n----- Try again")

                        option = input(">>> ")
                        if option == "login":
                            exists = False
                            self.login()

            elif option == "main menu":
                self.main()

    def game(self):
        if self.isOn:
            print("Select Game Mode: ")
            print("----- Easy\n----- Medium\n----- Hard")

            mode = input(">>> ").lower()
            while not mode in ["easy", "medium", "hard"]:
                print("Invalid Command.")
                mode = input(">>> ").lower()

            game = Game(mode)
            self.score = game.run()
            self.scoreboard()

            print("----- Main Menu\n----- Exit")

            option = input(">>> ").lower()
            while not option in ["main menu", "exit"]:
                print("Invalid Command.")
                option = input(">>> ").lower()

            if option == "main menu":
                self.main()
            elif option == "exit":
                self.exit()

    def scoreboard(self):
        if self.isOn:
            self.log.read()
            if self.username != None:
                if int(self.log.csv.loc[self.log.csv.username == self.username].highscore.item()) < self.score:
                    self.log.update(self.username, self.score)

            self.log.top()
            print("----- Main Menu\n----- Exit")

            option = input(">>> ").lower()
            while not option in ["main menu", "exit"]:
                print("Invalid Command.")
                option = input(">>> ").lower()

            if option == "main menu":
                self.main()
            elif option == "exit":
                self.exit()

    def exit(self):
        self.isOn = False
