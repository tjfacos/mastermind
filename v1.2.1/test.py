import pygame

from modules.ui.stats import *
from modules.ui.config import *

screen = pygame.display.set_mode((1500, 800))

SCREEN_DIMS = Screen_Dims()
SCREEN_DIMS.dims = screen.get_size()

user = User("tom", "password123")

import os

for k, v in os.environ.items():
    print(f'{k}={v}')
