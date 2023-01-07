import requests

SERVER_URL = "https://mastermind-server-flask-gjr5-main-arlah6e57a-ew.a.run.app"

class API:
    def __init__(self, url) -> None:
        self.url = url
    
    def CreateUser(self, username, password):
        r = requests.post(self.url + f"/user/{username}/{password}")
        if r.text == "200":
            return True
        else:
            return False
    
    def getUserStats(self, username, password):
        print(password)
        
        r = requests.get(self.url + f"/user/{username}/{password}")
        if r.text == "401":
            return False

        response = r.json()
        return (response["average"], response["personal_best"])

    def CheckUser(self, username, password):
        r = requests.get(self.url + f"/verify/{username}/{password}")
        
        if r.text == "200":
            return True
        
        return False
    
    def getLeaderboard(self):
        leaderboard_array = []
        
        r = requests.get(self.url + "/leaderboard")
        response = r.json()
        # print(response)
        for key in response:
            leaderboard_array.append([response[key]["user"], int(response[key]["score"])])
        # print(leaderboard_array)
        # print(leaderboard_array)
        for i in range(len(leaderboard_array)):
            leaderboard_array[i].insert(0, i+1)
        
        return leaderboard_array

    def postScore(self, username, password, score):
        r = requests.get(self.url + f"/score/{username}/{password}/{score}")

        if r.text == "200":
            return True
        
        return False

if __name__ == "__main__":
    api = API(SERVER_URL)
    # print(api.CheckUser("daisy", "duckling"))
    print(api.postScore("daisy", "duckling", 2_000))