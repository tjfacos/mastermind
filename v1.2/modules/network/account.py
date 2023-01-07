from modules.network.encrypt import encrypt
from modules.network.api_connection import API, SERVER_URL

def load_user():
    with open("account.txt", "r+") as f:
        user_tuple = tuple(f.readlines())
        if user_tuple:
            return User(*user_tuple)
        else:
            return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.api = API(SERVER_URL)
        self.verified = False
        if self.username:
            self.verify()

    def verify(self):
        if self.api.CheckUser(self.username, encrypt(self.password)):
            self.verified = True
            return True
        else:
            return False
    
    def create(self):
        self.api.CreateUser(self.username, encrypt(self.password))
    
    def getLeaderboard(self):
        return self.api.getLeaderboard()

    def postScore(self, score):
        self.api.postScore(self.username, encrypt(self.password), score)
    
    def getData(self):
        return self.api.getUserStats(self.username, self.password)