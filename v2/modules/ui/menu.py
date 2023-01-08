import pygame, sys
from pygame.locals import *


from modules.ui.components  import *
from modules.ui.config import Colours, Path
from modules.ui.element_functions import exit_game

from modules.network.api_connection import *
from modules.network.encrypt import encrypt
from modules.network.account import User

from modules.game.score import getScore

class Win_Box:
    def __init__(self, SCREEN_DIMS, topleft, replay_method) -> None:
        self.topleft = topleft
        
        self.width = SCREEN_DIMS.width - topleft[0]
        self.height = SCREEN_DIMS.height
        self.have_posted_score = False

        self.outer_rect = pygame.Rect(topleft[0], topleft[1], self.width, self.height)

        self.state_image = Image(topleft[0], topleft[1] + 10, self.width, self.height * 0.5, Path("you_win") )
        

        self.btn_topleft = btn_topleft = (topleft[0], topleft[1] + self.height * 0.5 + 10)
        self.play_again_btn = Button(
            btn_topleft[0], 
            btn_topleft[1], 
            self.width, 
            self.height * 0.2,  
            Path("replay"), 
            replay_method
        )
    
    def run(self, screen, replay_method, total_time, active_row, user):
        
        # if not self.have_posted_score and user.signed_in:
        #     self.score = getScore(total_time, active_row)
        #     user.postScore(self.score)
        #     self.score_label = Label(
        #         self.btn_topleft[0],
        #         self.btn_topleft[1] + self.height * 0.2 + 50,
        #         f"Score: {self.score}"
        #     )
        #     self.have_posted_score = True

        pygame.draw.rect(
            screen,
            Colours.LIGHT_GREY,
            self.outer_rect,
            0,
            10
        )

        self.state_image.run(screen)
        self.play_again_btn.run(screen)
        # self.score_label.run(screen)


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



