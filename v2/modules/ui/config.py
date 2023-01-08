class Colours:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    LIGHT_GREY = (74,74,74)
    DARK_GREY = (30, 30, 30)
    GREEN = (0,230,0)
    RED = (230,0,0)
    BLUE = (0,0,230)
    PINK = (230,0,191)
    YELLOW = (255,255,51)
    BROWN = (153,51,0)
    PURPLE = (102,0,102)
    ORANGE = (255,85,0)
    LIGHT_BLUE = (4,200,249)
    LIGHT_BROWN = (170, 105, 76)
    DARK_BROWN = (122, 60, 34)
    LIGHT_GREEN = (140, 230, 86)
    LIGHT_RED = (230, 85, 85)
    DARK_RED = (139, 0, 0)

    Colour_ID = {
            "light_grey": 0,
            "red": 1,
            "green": 2,
            "blue": 3,
            "pink": 4,
            "yellow": 5,
            "brown": 6,
            "purple": 7,
            "orange": 8,
            "black": 9,
            "white": 10 
    }


class Screen_Dims:
    
    @property
    def height(self):
        return self.WINDOW_HEIGHT

    @height.setter
    def height(self, h):
        self.WINDOW_HEIGHT = h
        
    @property
    def width(self):
        return self.WINDOW_WIDTH
        
    @width.setter
    def width(self, w):
        self.WINDOW_WIDTH = w

    @property
    def dims(self):
        return (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

    @dims.setter
    def dims(self, dims):
        self.WINDOW_WIDTH = dims[0]
        self.WINDOW_HEIGHT = dims[1]

def Path(file_name):
    return f"./assets/{file_name}.png"
    
    