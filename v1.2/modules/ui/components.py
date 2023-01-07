import pygame
from modules.ui.config import Colours


class Image: #Image class to use in labels, menus etc.
    
    def setImageRect(self):
        
        self.image = pygame.transform.scale(self.img, (
            int(self._width), 
            int(self._height)
        ))

        self.rect = self.image.get_rect()

    @property
    def topleft(self):
        return self.rect.topleft
    
    @topleft.setter
    def topleft(self, topleft):
        self.rect.topleft = topleft

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        self._height = h
        self.setImageRect()

    @property
    def width(self):
        return self._width * self._scale
    
    @width.setter
    def width(self, w):
        self._width = w
        self.setImageRect()




    def __init__(self, x, y, width, height, img_path) -> None:
        self.img = pygame.image.load(img_path).convert_alpha()
        
        
        self._width = width
        self._height = height

        self.setImageRect()
        
        self.topleft = (x,y)
    


    def run(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



class Button(Image):
    
    def __init__(self, x, y, width, height, img_path, method) -> None:
        
        super().__init__(x, y, width, height, img_path)

        self.method = method
        self.clicked = False

    def run(self, screen, args=()):
        #Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        #Get mouse position
        pos = pygame.mouse.get_pos()

        #Check moused over and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return self.method(*args)
        
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

class Label:
       
    def __init__(self, x, y, text, font_size=35, colour = (255,255,255)) -> None:
        pygame.font.init()
        self.font = pygame.font.SysFont("Ariel", font_size)
        self.text = self.font.render(text, True, colour)
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y

    def run(self, screen):
        screen.blit(self.text, self.rect)


#Must Finish!!!
# Figure out selection
# Implement in menu.Global_Stats

class TextInput():
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect(x, y, 200, 80)
        self.value = ""
        self.active = False
        
    def run(self, screen, selected):
        pos = pygame.mouse.get_pos()

        colour = Colours.LIGHT_GREY

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.active = True
        
        if pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(pos):
            self.active = False

        if self.active:
            colour = Colours.LIGHT_BLUE
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
        
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        
        pygame.draw.rect(screen, colour, self.rect, 5, 5)



