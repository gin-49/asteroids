import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Asteroid.containers = (asteroids, drawable, updatable)
Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, drawable, updatable)
field = AsteroidField()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
time = pygame.time.Clock()
dt = 0
fps = 60
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)


def main():
    while True:
        # Quit Window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = time.tick(fps) / 1000
        screen.fill((0, 0, 0))

        updatable.update(dt)
        for i in asteroids:
            if i.collision(player):
                print("Game over!")
                sys.exit()

            for j in shots:
                if i.collision(j):
                    i.split()
                    j.kill()


        for i in drawable:
            i.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
