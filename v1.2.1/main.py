import pygame, sys, os, time
from pygame.locals import *
from random import randint

from modules.ui.menu import *
from modules.ui.config import Screen_Dims, Colours
from modules.ui.element_functions import exit_game
from modules.ui.save import SaveLoadBox
from modules.ui.components import *
from modules.ui.stats import *

from modules.game.groups import SelectionBox, Row, KeyBlock

from modules.network.account import *

score = 0
total_time = 0
start_time = 0

def getUser():
    global user
    
    user = load_user()
    user.verify()


user = User("", "")
getUser()

SCREEN_DIMS = Screen_Dims()

screen = pygame.display.set_mode((1500, 800))
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

stats_page = StatsPage(SCREEN_DIMS)

def submit():
    global active_row, activeStatusArray, won, lost, rowsArray, keyBlockArray, start_time, total_time

    total_time = int(time.time()) - start_time
    print(total_time)

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
    global screen, active_row, activeStatusArray, rowsArray, keyBlockArray, won, lost, ANSWER_CODE, selected_colour, save_load_block, start_time
    global winBox, loseBox

    start_time = int(time.time())
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
    save_load_block = SaveLoadBox((topleft[0] + row_width + 30 + row_height, topleft[1]))

    # Diagnostic Block

    # print(f"won: {won}")
    # print(f"lost: {lost}")

    print(f"ANSWER CODE: {ANSWER_CODE} ", end="")

    for n in range(4):
        print(list(Colours.Colour_ID.keys())[list(Colours.Colour_ID.values()).index(ANSWER_CODE[n])], end=", ")
    print()

    # print(activeStatusArray)

    winBox = Win_Box(SCREEN_DIMS, (
        topleft[0] + row_width + 30 + row_height,
        topleft[1]
    ), set_up)

    loseBox = Lose_Box(SCREEN_DIMS, (
        topleft[0] + row_width + 30 + row_height,
        topleft[1]
    ), set_up)



SelectionBlock = SelectionBox(SCREEN_DIMS, (
    topleft[0] - row_height - 30,
    topleft[1]
))


#Define Buttons
quit_button = Button(0,0, 100, 50, Path("stop_btn"), exit_game)

submit_btn = Button(topleft[0], topleft[1] + row_height*10, row_width, SCREEN_DIMS.height * 0.1, Path("submit_btn"), submit)

#Define win and lose boxes


logo = Image(50, 100, (topleft[0] - row_height - 30)*0.8, SCREEN_DIMS.height * 0.1, Path("mastermind-logo"))

stats_button = Button(0, SCREEN_DIMS.height - 150, 100, 100, Path("account"), stats_page.run)




def play():
    global activeStatusArray, SelectionBlock, rowsArray, keyBlockArray, winBox, loseBox, total_time
    global submit_btn, quit_button, stats_button, selected_colour, active_row, ANSWER_CODE, user


    set_up()

   

    run = True
    while run:
        stats_button.run(screen, (screen, user))
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        logo.run(screen)

        quit_button.run(screen)
        
        if won:
            winBox.run(screen, set_up, total_time, active_row, user)
            
        
        if lost:
            loseBox.run(screen, set_up, total_time, active_row, user)
        
        if not won and not lost:
            loaded_values = save_load_block.run(screen, rowsArray, active_row, ANSWER_CODE, total_time)
            pygame.draw.rect(
                screen,
                Colours.DARK_GREY,
                pygame.Rect(topleft[0] + row_width + 30 + row_height, topleft[1]+800, 500, SCREEN_DIMS.height-800)
            )

        if loaded_values:
            #If there are loaded values, assign them, set activeStatusArray, then set values for rows, then set key pegs
            rowsValues, active_row, ANSWER_CODE, total_time = loaded_values
            for i in range(10):
                rowsArray[i].setValues(rowsValues[i])
                keyBlockArray[i].setKeyPegs(ANSWER_CODE, rowsValues[i])
            activeStatusArray = [False] * 10
            activeStatusArray[active_row] = True

        selected_colour = SelectionBlock.run(screen, selected_colour)
        
        for row in range(10):
            rowsArray[row].run(screen, selected_colour, activeStatusArray[row])
            keyBlockArray[row].run(screen)
        
        submit_btn.run(screen)





main_menu = Menu(SCREEN_DIMS)

def show_menu():
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        main_menu.run(screen)
        
        
        if main_menu.game_started:
            return True

# sign_in_page = SignIn(SCREEN_DIMS)


    
    



def main():
    getUser()
    
    pygame.init()
    
    show_menu()
    play()




getUser()
main()