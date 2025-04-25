import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # score for the game, probably create a class later
    score = 0
    score_increment = 10
    
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    
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
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print(f"Game over!\nYour final score is: {score}!")
                pygame.quit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    #asteroid.kill() # to be replaced with asteroid.split()
                    asteroid.split()
                    shot.kill()
                    score += score_increment
                    print(score)
        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
        
    


if __name__ == "__main__":
    main()

pygame.quit()