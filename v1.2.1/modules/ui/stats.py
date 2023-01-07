import pygame, sys
from pygame.locals import *


from modules.ui.components import *
from modules.ui.config import *
from modules.network.account import *


class LeaderBoard:
    def __init__(self, centre, width, height, leaderboard_array) -> None:
        self.rect = pygame.Rect(500, 500, width, height)
        self.rect.center = centre

        self.leaderboard = [] #To be filled with labels
        for entry in leaderboard_array:
            self.leaderboard.append(Label(
                self.rect.x + 10,
                self.rect.y + 50*(entry[0] - 1),
                f"{entry[0]}: {entry[1]} - {entry[2]} points",
                50
            ))



    def run(self,screen):
        pygame.draw.rect(
            screen,
            Colours.LIGHT_GREY,
            self.rect,
            0,
            5
        )

        for label in self.leaderboard:
            label.run(screen)







class PersonalStats:
    def __init__(self, topleft, width, height) -> None:
        self.topleft = topleft
        self.rect = pygame.Rect(
            topleft[0],
            topleft[1],
            width,
            height
        )
        

    def setLabels(self, username, user_data):
        self.user_label = Label(
            self.topleft[0]+10,
            self.topleft[1]+10,
            f"Username: {username}",
            60
        )
        
        self.average = Label(
            self.topleft[0]+10,
            self.topleft[1]+110,
            f"Average: {user_data[0]}",
            60
        )
        
        self.personal_best = Label(
            self.topleft[0]+10,
            self.topleft[1]+210,
            f"Personal Best: {user_data[1]}",
            60
        )

    def run(self, screen):
        pygame.draw.rect(
            screen,
            Colours.LIGHT_GREY,
            self.rect,
            0,
            5
        )
        self.user_label.run(screen)
        self.average.run(screen)
        self.personal_best.run(screen)










class StatsPage():
    def __init__(self, SCREEN_DIMS) -> None:
        self._continue = True
        
        self.SCREEN_DIMS = SCREEN_DIMS

        self.leaderboard = LeaderBoard(
            (
                SCREEN_DIMS.width * 0.8,
                SCREEN_DIMS.height/2
            ),
            SCREEN_DIMS.width * 0.4,
            SCREEN_DIMS.height * 0.8,
            User("", "").getLeaderboard()
        )
        self.PersonalStats = PersonalStats(
            (
                100,
                SCREEN_DIMS.height * 0.1
            ),
            SCREEN_DIMS.width * 0.5,
            SCREEN_DIMS.height * 0.8
        )
        self.back_btn = Button(0, 0, 100, 50, Path("stop_btn"), self.stop)
        self.set = False


    def stop(self):
        self._continue = False



    def run(self, screen, user):
        screen.fill(Colours.DARK_GREY)
        # print(user.verify())
        # print(user.getData())

        if not self.set:
            self.leaderboard = self.leaderboard = LeaderBoard(
                (
                    self.SCREEN_DIMS.width * 0.8,
                    self.SCREEN_DIMS.height/2
                ),
                self.SCREEN_DIMS.width * 0.4,
                self.SCREEN_DIMS.height * 0.8,
                User("", "").getLeaderboard()
            )

            if user.username and not self.set:
                self.PersonalStats.setLabels(user.username, user.getData())
        
        self.set = True

        if self._continue:
            self.leaderboard.run(screen)
            self.back_btn.run(screen)
            if user.username:
                self.PersonalStats.run(screen)





