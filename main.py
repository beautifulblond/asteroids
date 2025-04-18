import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updateable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        asteroid_field
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                pygame.quit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    #asteroid.kill() # to be replaced with asteroid.split()
                    asteroid.split()
                    shot.kill()
        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
        
    


if __name__ == "__main__":
    main()

pygame.quit()