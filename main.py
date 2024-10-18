import pygame
import sys
from player import *
from asteroid import *
from circleshape import *
from constants import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        dt = clock.tick(60)/1000

        for updatables in updatable:
            updatables.update(dt)

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.update()

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
    

if __name__ == "__main__":
    main()

