# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    spaceship = Player(x, y)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        spaceship.update(dt)
        spaceship.draw(screen)
        pygame.display.flip()

    print("Starting Asteroids!")
    print("Screen width: "+str(SCREEN_WIDTH))
    print("Screen height: "+str(SCREEN_HEIGHT))

if __name__ == "__main__":
    main()