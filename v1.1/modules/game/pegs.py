from modules.ui.config import Colours
import pygame

class Peg:
    
    def __init__(self, x, y, side) -> None:
        self.pos_x =  0
        self.pos_y = 0
        self.pos = (0,0)
        self.side = 0

        self.side = side
        self.position = (x,y)
        self.clicked = False
        self.colour = Colours.LIGHT_GREY
    
    def set_rect(self):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.side, self.side)

    #Co-ordinate properties and setters
    

    #Position (tuple)
    @property
    def position(self):
        return self.pos
    
    @position.setter
    def position(self, pos):
        self.pos = pos

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
        self.set_rect()

    #x co-ordinaate
    @property
    def x(self):
        return self.pos_x

    @x.setter
    def x(self, x):
        self.pos_x = x
        self.pos = (x, self.pos[1])
        self.set_rect()
    
    #y co-ordinate
    @property
    def y(self):
        return self.pos_y
            
    @y.setter
    def y(self, y):
        self.pos_y = y
        self.pos = (self.pos[0], y)
        self.set_rect()

#Coloured Pegs
class CPeg(Peg):
    
    def __init__(self, x, y, side) -> None:
        super().__init__(x, y, side)
        self.value = 0

    def run(self, screen, selected_colour, active):
        

        #Check moused over and clicked
        if selected_colour and self.rect.collidepoint(pygame.mouse.get_pos()) and active:
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                
                #Set the colour of the peg to the selected colour
                self.value = Colours.Colour_ID[selected_colour]
                
        
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        self.colour = list(Colours.Colour_ID.keys())[self.value].upper()
        pygame.draw.rect(screen, getattr(Colours, self.colour), self.rect, 0, 2)

        if active:
            pygame.draw.rect(screen, Colours.LIGHT_BLUE, self.rect, 2, 2)

#Key Pegs
class KPeg(Peg):
    
    def __init__(self, x, y, side) -> None:
        super().__init__(x, y, side)
        self.value = 0
    
    def run(self, screen, value):
        # 1 indicates colour, but not position (white)
        # 2 indicates colour AND position (black)

        boarder = 0
        if value:
            self.value = value
        
        if self.value == 1: 
            self.colour = Colours.WHITE
        elif self.value == 2:
            self.colour = Colours.BLACK
        else:
            boarder = 2

        pygame.draw.rect(screen, self.colour, self.rect, boarder)

#Used to select the colours
class SelectionPeg(Peg):
    
    def __init__(self, x, y, side, colour_id) -> None:
        super().__init__(x, y, side)
        self.value = colour_id
        self.colour = list(Colours.Colour_ID.keys())[colour_id]

    def run(self, screen, selected_colour):
        #Check moused over and clicked
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                
                return self.colour #Returns selected colour
                             
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        pygame.draw.rect(screen, self.colour, self.rect, 0, 2)
        if selected_colour == self.colour:
            #Add boarder to selected peg
            pygame.draw.rect(screen, Colours.LIGHT_BLUE, self.rect, 5, 2)
        
        return selected_colour


