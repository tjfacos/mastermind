from modules.network.encrypt import encrypt
from modules.network.api_connection import API, SERVER_URL

# from api_connection import API, SERVER_URL
# from encrypt import encrypt

import os

def load_user():
    
    with open("account.txt", "r") as f:
        details = f.read().split()
        if len(details) < 2:
            return User("", "")
    return User(details[0], details[1])

#encrypt passwords before sending to API class

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.api = API(SERVER_URL)
        self.signed_in = False
        if self.username:
            self.verify()

    def verify(self):
        if self.api.CheckUser(self.username, self.password):
            self.signed_in = True
            return True
        else:
            return False
    
    def create(self):
        self.signed_in = True
        return self.api.CreateUser(self.username, self.password)
    
    def getLeaderboard(self):
        return self.api.getLeaderboard()

    def postScore(self, score):
        self.api.postScore(self.username, self.password, score)
    
    def getData(self):
        # print(f"getData {self.username} {self.password}")
        
        return self.api.getUserStats(self.username, self.password)

if __name__ == "__main__":
    print(User("","").getLeaderboard())