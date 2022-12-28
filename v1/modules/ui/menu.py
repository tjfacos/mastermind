from modules.ui.components  import *
from modules.ui.config import Colours, Path
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

    def __init__(self, SCREEN_DIMS, start_method, quit_method):
        
        self.background_rect = pygame.Rect(0, 0, SCREEN_DIMS.width, SCREEN_DIMS.height)
        
        
        self.logo = Image(0, 0, SCREEN_DIMS.width, SCREEN_DIMS.height * 0.4, "./v1/assets/mastermind-logo.png")
        

        #Define Button Width
        btn_width = SCREEN_DIMS.width / 5
        
        #Define Start Button
        self.start_btn = Button(0, 0, btn_width, btn_width*0.6, "./v1/assets/start_btn.png", start_method)
        self.start_btn.topleft = (SCREEN_DIMS.width/2 - btn_width/2, self.logo.height + 50)
        
        #Define Quit Button
        self.quit_btn = Button(0, 0, btn_width, btn_width*0.6, "./v1/assets/stop_btn.png", quit_method)
        self.quit_btn.topleft = (SCREEN_DIMS.width/2 - btn_width/2, self.logo.height + 50 + self.start_btn.height + 50)
        
    def run(self, screen):
        pygame.draw.rect(screen, Colours.DARK_GREY, self.background_rect)

        self.logo.run(screen)
        self.start_btn.run(screen)
        self.quit_btn.run(screen)











