import pygame
from sys import exit 


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
screen_rect = screen.get_rect()
spaceship = pygame.image.load('images/spaceship.png').convert_alpha() 
spaceship_rect = spaceship.get_rect(midleft = screen_rect.midleft) 
                                                                                
asteroid = pygame.image.load('images/asteroid.png').convert_alpha()
asteroid_rect = asteroid.get_rect(midright = screen_rect.midright)  
projectile = pygame.Surface((16,4))
projectile_rect = projectile.get_rect(midleft = spaceship_rect.midright) # set projectile_rect midleft to spaceship_rect midright
projectile.fill('white') 
projectile_speed = 8 # set projectile speed

font = pygame.font.SysFont('Aptos', 36, False, False) 
score = 0 
score_display = font.render(f"Score: {score}", True, "white", None) 
score_display_rect = score_display.get_rect(topright = screen_rect.topright) 
                                                                         

clock = pygame.time.Clock() 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                pass 
    screen.fill((0,0,0)) # draw over old frames to hide them
    screen.blit(spaceship, spaceship_rect) 
    screen.blit(projectile, projectile_rect) 
    screen.blit(asteroid, asteroid_rect) 
    screen.blit(score_display, score_display_rect) 
    projectile_rect.x += projectile_speed # move projectile upward by decrementing the y position by the speed

    clock.tick(30) 
    pygame.display.update()


