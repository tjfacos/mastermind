import pygame, sys

def exit_game():
    pygame.quit()
    sys.exit()

def run_ui(*args, screen):
    for element in args:
        element.run(screen)