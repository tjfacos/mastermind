import pygame, sys
from pygame.locals import *


from modules.ui.components  import *
from modules.ui.config import Colours, Path
from modules.ui.element_functions import exit_game

from modules.network.api_connection import *
from modules.network.encrypt import encrypt
from modules.network.account import User


import pygame

class Win_Box:
    def __init__(self, SCREEN_DIMS, topleft, replay_method) -> None:
        self.width = SCREEN_DIMS.width - topleft[0]
        self.height = SCREEN_DIMS.height

        self.outer_rect = pygame.Rect(topleft[0], topleft[1], self.width, self.height)

        self.state_image = Image(topleft[0], topleft[1] + 10, self.width, self.height * 0.5, Path("you_win") )
        

        btn_topleft = (topleft[0], topleft[1] + self.height * 0.5 + 10)
        self.play_again_btn = Button(
            btn_topleft[0], 
            btn_topleft[1], 
            self.width, 
            self.height * 0.2,  
            Path("replay"), 
            replay_method
        )
    
    def run(self, screen, replay_method):
        
        pygame.draw.rect(
            screen,
            Colours.LIGHT_GREY,
            self.outer_rect,
            0,
            10
        )

        self.state_image.run(screen)
        self.play_again_btn.run(screen)

class Lose_Box(Win_Box):
    def __init__(self, SCREEN_DIMS, topleft, replay_method) -> None:
        super().__init__(SCREEN_DIMS, topleft, replay_method)
        self.state_image = Image(topleft[0], topleft[1] + 10, self.width, self.height * 0.5, Path("you_lose") )









class Menu():

    def __init__(self, SCREEN_DIMS):
        
        self.background_rect = pygame.Rect(0, 0, SCREEN_DIMS.width, SCREEN_DIMS.height)
        self.game_started = False
        
        self.logo = Image(0, 0, SCREEN_DIMS.width, SCREEN_DIMS.height * 0.4, Path("mastermind-logo"))
        

        #Define Button Width
        btn_width = SCREEN_DIMS.width / 5
        
        #Define Start Button
        self.start_btn = Button(0, 0, btn_width, btn_width*0.6, Path("start_btn"), self.start_game)
        self.start_btn.topleft = (SCREEN_DIMS.width/2 - btn_width/2, self.logo.height + 50)
        
        #Define Quit Button
        self.quit_btn = Button(0, 0, btn_width, btn_width*0.6, Path("stop_btn"), exit_game)
        self.quit_btn.topleft = (SCREEN_DIMS.width/2 - btn_width/2, self.logo.height + 50 + self.start_btn.height + 50)

    def start_game(self):
        self.game_started = True

    def run(self, screen):
        pygame.draw.rect(screen, Colours.DARK_GREY, self.background_rect)

        self.logo.run(screen)
        self.start_btn.run(screen)
        self.quit_btn.run(screen)

class LeaderBoard():
    def __init__(self, centre, width, height, leaderboard_array) -> None:
        self.rect = pygame.Rect(500, 500, width, height)
        self.rect.center = centre

        self.leaderboard = [] #To be filled with labels
        for entry in leaderboard_array:
            self.leaderboard.append(Label(
                self.rect.x,
                self.rect.y + 50*(entry[0] - 1),
                f"{entry[0]}: {entry[1]} - {entry[2]} points"
            ))

    def run(self, screen):
        pygame.draw.rect(screen, Colours.LIGHT_GREY, self.rect)
        for x in range(5):
            self.leaderboard[x].run(screen)

class AccountBlock():
    def __init__(self, topleft, user, targets) -> None:
        self.topleft = topleft
        
        self.sign_out_btn = Button(topleft[0], topleft[1]+300, 100, 50, Path("sign_out"), self.sign_out)
        self.sign_in_btn = Button(topleft[0], topleft[1]+300, 100, 50, Path("sign_out"), self.sign_in)

        if user.verified:
            data = user.getData()
            self.personal_best_label = Label(topleft[0], topleft[1]+50, f"Personal Best: {data[1]}")
            self.average_label = Label(topleft[0], topleft[1]+150, f"Average Score: {data[0]}")
        else:
            self.username_input = TextInput()
            self.password_input = TextInput()

    def sign_out(self):
        pass

    def set_user(self, new_user):
        self.user = new_user
        if self.user.verified:
            data = self.user.getData()
            self.personal_best_label = Label(self.topleft[0], self.topleft[1]+50, f"Personal Best: {data[1]}")
            self.average_label = Label(self.topleft[0], self.topleft[1]+150, f"Average Score: {data[0]}")

    def run(self, screen):
        if self.user.verified:
            self.personal_best_label.run(screen)
            self.average_label.run(screen)
            self.sign_out_btn.run(screen)
        else:
            self.sign_in_btn.run(screen)
            self.entered_username = self.username_input.run(screen)
            self.entered_password = self.password_input.run(screen)


class Global_Stats():
    def __init__(self, SCREEN_DIMS, user): #If logged in, verify user, then get user stats. 
        self.user = user
                
        self.label = Label(0, 100, "Not Signed In")
        self.label_bg_colour = Colours.LIGHT_RED

        self.back_btn = Button(0, 0, 100, 50, Path("back"), self.finish)

        self.leaderboard = LeaderBoard(
            (
                SCREEN_DIMS.width / 2,
                SCREEN_DIMS.height/2
            ),
            SCREEN_DIMS.width * 0.6,
            SCREEN_DIMS.height * 0.5,
            self.API.getLeaderboard()
        )

        self.username_target = ""
        self.password_target = ""

        self.signed_in = self.user.verified

        #Account Block

    def finish(self):
        self._continue = True

    def sign_in(self, username, password):
        self.user = User(username, password)
        if self.user.verified:
            self.label = Label(0, 100, f"Signed in as {self.user.username}")
            self.label_bg_colour = Colours.LIGHT_GREEN
            self.signed_in = True
            return True
        else:
            return False
            
    def sign_out(self):
        self.label = Label(0, 100, "Not Signed In")
        self.label_bg_colour = Colours.LIGHT_RED
        self.user = User("", "")
        self.signed_in = False
    
    def run(self, screen):
        screen.fill(Colours.DARK_GREY)
        
        self._continue = True
        while self._continue:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()

            #run label and bg
            pygame.draw.rect(
                screen, 
                self.label_bg_colour,
                pygame.Rect(0, 100, 500, 100),
                0,
                10
            )
            
            self.back_btn.run(screen)
            self.sign_in_btn.run(screen, (self.user[0], self.user[1]))
            self.sign_in_btn.run(screen)
            self.label.run(screen)
            
            if self.signed_in:
                pass
