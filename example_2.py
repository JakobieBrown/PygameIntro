import pygame # imports the module

# -- Set up --
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 #Constants for window size
pygame.init() # pygame must be initialized before it can be used

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
''' ^ Creates a window with a pygame surface ^
    The return value is a pygame surface
'''
clock = pygame.time.Clock() # used to manage the timing and frame rate

# -- Main Loop --
while True:

    # --- Handle Events --- (keyboard, mouse, window close, etc.)
    events = pygame.event.get() # gets the current events
    for event in events: # loop through events

        if event.type == pygame.QUIT: # 'x' button of window pressed
            pygame.quit() # safely quit pygame
            exit() # exit program

    clock.tick(30) # 30 frames per second

