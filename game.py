from random import randint
from scoreboard import Scoreboard


class Game():
    def __init__(self, mode):
        self.scoreboard = Scoreboard()
        self.modes = {
            "easy": 10,
            "medium": 15,
            "hard": 25
        }
        self.rounds = self.modes[mode]
        self.base()
        self.valid()
        self.map()

    def base(self):
        self.basement = []

        for i in range(self.rounds):
            self.basement.append([])
            for j in range(self.rounds):
                self.basement[i].append("*")

    def map(self):
        self.ground = []
        self.bombs = []

        for i in range(self.rounds):
            self.ground.append([])
            for j in range(self.rounds):
                probability = randint(1, 10)
                if probability == 10:
                    self.ground[i].append("o")
                    self.bombs.append(f"{i} {j}")
                else:
                    self.ground[i].append(0)
        self.bomber()

    def valid(self):
        self.isValid = []

        for i in range(self.rounds):
            self.isValid.append([])
            for j in range(self.rounds):
                self.isValid[i].append(True)

    def bomber(self):
        n = len(self.ground)
        for bomb in self.bombs:
            I, J = bomb.split(" ")
            I, J = int(I), int(J)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        if I + i > -1 and J + j > -1:
                            if I + i < n and J + j < n:
                                if self.ground[I + i][J + j] != "o":
                                    self.ground[I + i][J + j] += 1

    def run(self):
        self.printer(self.basement)
        
        end = False
        while not end:
            action, i, j = input(">>> ").split(" ")
            action, i, j = action.lower(), int(i), int(j)

            if action == "step":
                if self.isValid[i][j]:
                    if self.ground[i][j] != "o":
                        self.scoreboard.score()
                        self.basement[i][j] = self.ground[i][j]
                        self.isValid[i][j] = False
                        self.printer(self.basement)
                    else:
                        print("You Lost.")
                        for bomb in self.bombs:
                            i, j = bomb.split(" ")
                            i, j = int(i), int(j)
                            self.basement[i][j] = "x"
                        self.printer(self.basement)

                        break
                else:
                    print("Invalid Command.")

            elif action == "flag":
                if self.isValid[i][j]:
                    self.basement[i][j] = "f"
                    self.printer(self.basement)

            else:
                print("Invalid Command.")

            end = self.end()
        return self.scoreboard.points

    def end(self):
        n = len(self.basement)
        safe = (n * n) - len(self.bombs)
        counter = 0

        for i in range(n):
            for j in range(n):
                if self.basement[i][j] != "*":
                    counter += 1
        if counter == safe:
            return True
        return False

    def printer(self, map):
        n = len(map)
        space = " "
        str = f"\n{5 * space}"
        
        for i in range(n):
            if i < 10:
                str += f"{i}{3 * space}"
            else:
                str += f"{i}{2 * space}"
        
        str += "\n"
        i = 0
        for row in map:
            if i < 10:
                str += f"\n{i}{4 * space}"
            else:
                str += f"\n{i}{3 * space}"
            for item in row:
                str += f"{item}{3 * space}"
            i += 1

        print(str)
