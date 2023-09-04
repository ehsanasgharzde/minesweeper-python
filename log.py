import pandas


class Log():
    def __init__(self):
        pass

    def top(self):
        self.read()
        self.sort()
        print("Rank\t\tUsername\t\tHighscore")
        counter = 0
        for rank, player in self.csv.iterrows():
            if counter < 10:
                print(f"{rank + 1}\t\t{player.username}\t\t\t{player.highscore}")

    def append(self, username, password, highscore):
        self.read()
        info = pandas.DataFrame({
            "username": [username],
            "password": [password],
            "highscore": [highscore]
        })
        info.to_csv("log/log.csv", mode="a", header=False)
        self.sort()

    def update(self, username, highscore):
        self.read()
        self.csv.at[self.csv.username.tolist().index(username), "highscore"] = highscore
        self.csv.to_csv("log/log.csv", header=False)

    def sort(self):
        self.read()
        self.csv.sort_values(by=["highscore", "username"], ascending=[False, True], inplace=True)
        self.csv.reset_index(drop=True, inplace=True)
        self.csv.to_csv("log/log.csv", header=False)

    def read(self):
        self.csv = pandas.read_csv("log/log.csv")
        self.csv.drop(self.csv.filter(regex="Unname"), axis=1, inplace=True)
        
