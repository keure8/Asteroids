import sys
import pygame
from constants import *
from player import Player
from AsteroidField import *
from asteroid import *
from shot import *

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroid_field = AsteroidField()

    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player) == True:
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collisions(shot) == True:
                    shot.kill()
                    asteroid.split()

        

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
