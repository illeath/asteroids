import pygame
from constants import *
from player import Player

def main():
    pygame.init
    new_screen = screen()
    Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    print("Starting asteroids!")

def screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        Player.draw(screen)


if __name__ == "__main__":
    main()