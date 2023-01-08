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
        
        r = requests.get(self.url + f"/user/{username}/{password}")
        print(r)
        if r.text == "401":
            return False

        response = r.json()
        print(response)
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
        r = requests.post(self.url + f"/score/{username}/{password}/{score}")

        if r.text == "200":
            return True
        
        return False

if __name__ == "__main__":
    api = API(SERVER_URL)
    # print(api.getUserStats("thomas",
    # "264a441634556b66e64b60496fc16d6ba223eadc5d3d581e7271933f9e41135e2c9deb9a7b9c778b2b2578ef899e9bd077130972feefe04e9e6bf669be29de50"))

    

    print(api.getUserStats("tom",
    "bed4efa1d4fdbd954bd3705d6a2a78270ec9a52ecfbfb010c61862af5c76af1761ffeb1aef6aca1bf5d02b3781aa854fabd2b69c790de74e17ecfec3cb6ac4bf"))