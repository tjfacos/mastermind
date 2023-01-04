# import pygame
import pygame
from modules.ui.components import Label

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

# create the display surface
display_surface = pygame.display.set_mode((1000, 700))

# change the window screen title
pygame.display.set_caption('Our Text')

label = Label(100, 100, "Hello, World!", 50)

run = False
while run:

    # add background color using RGB values
    display_surface.fill((0, 0, 0))

    label.run(display_surface)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get()
    # method.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # deactivating the pygame library
            pygame.quit()

            # quitting the program.
            quit()

        # update the display
        pygame.display.update()


string = "1 2 3 4    "
print(string.split())