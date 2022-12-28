import pygame, sys
from pygame.locals import *
from random import randint

from modules.ui.menu import *
from modules.ui.config import Screen_Dims, Colours
from modules.ui.element_functions import exit_game

from modules.game.groups import SelectionBox, Row, KeyBlock


SCREEN_DIMS = Screen_Dims()

screen = pygame.display.set_mode()
pygame.display.set_caption("Mastermind")
screen.fill(Colours.DARK_GREY)

#Set WINDOW_WIDTH and WINDOW_HEIGHT values
SCREEN_DIMS.dims = screen.get_size()

active_row = 0
selected_colour = ""

won = False
lost = False

ANSWER_CODE = []

#Define some dimensions

row_height = (SCREEN_DIMS.height * 0.9) / 10
row_width = row_height * 4
topleft = (SCREEN_DIMS.width / 2 - row_width / 2, 0)


def submit():
    global active_row, activeStatusArray, won, lost, rowsArray, keyBlockArray
    
    row_index = active_row 
    active_row += 1

    if active_row < 10:
        activeStatusArray[row_index] = False
        activeStatusArray[active_row] = True

    #Check if row at row_index is won, and set keys
        row_value = rowsArray[row_index].value()
        won = keyBlockArray[row_index].setKeyPegs(ANSWER_CODE, row_value)
    else:
        lost = True

def setAnswerCode():
    code = []
    
    while len(code) != 4:
        id = randint(1,10)
        if id not in code:
            code.append(id)
    
    return code
        

def set_up():
    global screen, active_row, activeStatusArray, rowsArray, keyBlockArray, won, lost, ANSWER_CODE, selected_colour
    
    screen.fill(Colours.DARK_GREY)

    active_row = 0
    
    won = False
    lost = False

    selected_colour = ""

    ANSWER_CODE = setAnswerCode()

    activeStatusArray = [False] * 10
    rowsArray = []
    keyBlockArray = []


    for n in range(10):
        rowsArray.append(
            Row(
                SCREEN_DIMS,
                (
                    topleft[0],
                    topleft[1] + row_height*n
                )
            ))

        keyBlockArray.append(
            KeyBlock(
                SCREEN_DIMS,
                (
                    topleft[0] + row_width + 30,
                    topleft[1] + row_height*n
                )
            )
        )

    activeStatusArray[0] = True
    
    # Diagnostic Block

    print(f"won: {won}")
    print(f"lost: {lost}")

    print(f"ANSWER CODE: {ANSWER_CODE}")

    for n in range(4):
        print(list(Colours.Colour_ID.keys())[list(Colours.Colour_ID.values()).index(ANSWER_CODE[n])], end=", ")
    print()

    print(activeStatusArray)




SelectionBlock = SelectionBox(SCREEN_DIMS, (
    topleft[0] - row_height - 30,
    topleft[1]
))


#Define Buttons
quit_button = Button(0,0, 100, 50, Path("stop_btn"), exit_game)

submit_btn = Button(topleft[0], topleft[1] + row_height*10, row_width, SCREEN_DIMS.height * 0.1, Path("submit_btn"), submit)

#Define win and lose boxes

winBox = Win_Box(SCREEN_DIMS, (
    topleft[0] + row_width + 30 + row_height,
    topleft[1]
), set_up)

loseBox = Lose_Box(SCREEN_DIMS, (
    topleft[0] + row_width + 30 + row_height,
    topleft[1]
), set_up)

logo = Image(50, 100, (topleft[0] - row_height - 30)*0.8, SCREEN_DIMS.height * 0.1, Path("mastermind-logo"))



def play():
    global activeStatusArray, SelectionBlock, rowsArray, keyBlockArray, winBox, loseBox, submit_btn, quit_button, selected_colour


    set_up()


    # global active_row, activeStatusArray, rowsArray, keyBlockArray, won, lost, ANSWER_CODE
    

    

    run = True
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        logo.run(screen)

        quit_button.run(screen)


        selected_colour = SelectionBlock.run(screen, selected_colour)
        
        for row in range(10):
            rowsArray[row].run(screen, selected_colour, activeStatusArray[row])
            keyBlockArray[row].run(screen)
        
        submit_btn.run(screen)


        if won:
            winBox.run(screen, set_up)
        
        if lost:
            loseBox.run(screen, set_up)
        



def main():
    pygame.init()
    
    play()





main()