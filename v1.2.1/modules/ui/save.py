import pygame
from modules.ui.components import *
from modules.ui.config import *

class SaveLoadBox:
    def save_game(self, rowsArray, active_row, ANSWER_CODE, total_time):
        with open("save_game.txt", "w") as f:
            for row in rowsArray:
                values = row.value()
                for i in range(4):
                    f.write(str(values[i]) + " ")
                f.write("\n")
            
            f.write("\n" + str(active_row) + "\n")
            for i in range(4):
                f.write(str(ANSWER_CODE[i]) + " ")
            f.write("\n"+str(total_time))
            
            self.label = Label(self.topleft[0]+250, self.topleft[1]+50, "Saved!", 100)

    def load_game(self):
        with open("save_game.txt", "r") as f:
            lines = f.readlines()
        
        rowsArrayValues = []
        for i in range(10):
            rowsArrayValues.append(list(map(int, lines[i].split())))
        
        active_row = int(lines[11])
        answer_code = list(map(int, lines[12].split()))
        total_time = int(lines[13])

        self.label = Label(self.topleft[0]+250, self.topleft[1]+50, "Loaded!", 100)

        return rowsArrayValues, active_row, answer_code, total_time

    def __init__(self, topleft) -> None:
        self.topleft = topleft
        self.save_button = Button(
            topleft[0],
            topleft[1],
            200, 100,
            Path("save"),
            self.save_game,
        )

        self.load_button = Button(
            topleft[0],
            topleft[1]+100,
            200, 100, 
            Path("load"),
            self.load_game
        )

        self.label = Label(topleft[0]+100, topleft[1], "")
    
    def run(self, screen, rowsArray, active_row, ANSWER_CODE, total_time):
        self.save_button.run(screen, (rowsArray, active_row, ANSWER_CODE, total_time))
        self.label.run(screen)

        return self.load_button.run(screen)