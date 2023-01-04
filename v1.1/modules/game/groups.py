import pygame

from modules.game.pegs import *

class Row:
    
    
    #Topleft property (sets x and y attributes when topleft is defined)
    @property
    def topleft(self):
        return self._topleft
    
    @topleft.setter
    def topleft(self, topleft):
        self._topleft = topleft
        self.x = self._topleft[0]
        self.y = self._topleft[1]


    
    def __init__(self, SCREEN_DIMS, topleft) -> None:
        self.pegs = []
        self.SCREEN_DIMS = SCREEN_DIMS
        self.topleft = topleft

        row_height = SCREEN_DIMS.height*0.9 / 10
        row_width = row_height*4

        peg_width = row_height*0.9
        margin = row_height*0.05 #margins each side of the pegs
        row_width = row_width + margin*2

        
        for n in range(4):
            self.pegs.append(CPeg(
                self.x + (margin*2 + peg_width)*n + margin , 
                self.y + margin , 
                peg_width
            )) 
        

    def run(self, screen, selected_colour, active):
        
        for peg in self.pegs:
            peg.run(screen, selected_colour, active)


    def value(self):
        
        row_array = [self.pegs[x].value for x in range(4)]
        
        return row_array

    def setValues(self, rowValues):
        for i in range(4):
            self.pegs[i].value = rowValues[i]
        







class KeyBlock:

    def __init__(self, SCREEN_DIMS, topleft) -> None:
        self.height = SCREEN_DIMS.height*0.8
        
        row_height = self.height / 10
        
        peg_width = row_height*0.9
        margin = row_height*0.05
        
        self.width = row_height

        self.keyValues = [0 for x in range(4)]

        key_width = peg_width * 0.45
        self.keys = [KPeg(0, 0, key_width) for x in range(4)]
        
        local_topleft = (topleft[0] + margin, topleft[1] + margin)
        offset = peg_width * 0.55

        for key in range(4):
            position = (
                local_topleft[0] + offset*(key%2),
                local_topleft[1] + offset*(key//2)
            )
            self.keys[key].position = position
        
        

    def run(self, screen):
            for key in range(4):
                self.keys[key].run(screen, self.keyValues[key])



    def setKeyPegs(self, answer_code, row_array):
        values = []
        handled_values = []
        temp = []
        

        #Black pegs (Colour and position) - 2
        
        for n in range(4):

            if row_array[n] == answer_code[n]:
                values.append(2)
                handled_values.append(answer_code[n])
            else:
                temp.append(n)
        
        #White pegs (Colour) - 1
        for n in temp:
            if row_array[n] in answer_code and row_array[n] not in handled_values:
                values.append(1)

        #No peg - 0   
        while len(values) < 4:
            values.append(0)
        
        #Set key values to those in values array
        self.keyValues = values

        if values == [2,2,2,2]:
            return True
        else:
            return False
















class SelectionBox:
    
    
    @property
    def topleft(self):
        return self._topleft
    
    @topleft.setter
    def topleft(self, topleft):
        self._topleft = topleft
        self.x = self._topleft[0]
        self.y = self._topleft[1]
    
    def __init__(self, SCREEN_DIMS, topleft) -> None:
        self.height = SCREEN_DIMS.height
        self.topleft = topleft

        self.width = (SCREEN_DIMS.height * 0.9) / 10

        peg_width = self.width * 0.9
        margin = self.width * 0.05 #margins each side of the pegs
        
        
        self.pegs = []
        colour_ids = [x for x in range(1,11)]
        for n in range(10):
            self.pegs.append(SelectionPeg(
                self.x + margin, 
                self.y + margin + (margin*2 + peg_width)*n,
                peg_width,
                colour_ids[n]
            ))
        

    def run(self, screen, current_selected_colour):
        selected_colour = current_selected_colour

        
        for peg in self.pegs:
            selected_colour = peg.run(screen, selected_colour)

        return selected_colour
