import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
time = pygame.time.Clock()
dt = 0
fps = 60


def main():
    while True:
        # Quit Window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.update()
        time.tick(fps)
        dt = time.tick(fps) / 1000


if __name__ == "__main__":
    main()
