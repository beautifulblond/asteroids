import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #player.update(dt)
        #Player class is now contained by updateable
        
        
        # The following should remain as ordered    
        screen.fill("black")
        
        updateable.update(dt)
        
        #player.draw(screen)
        #Player class is now contained by drawable
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        #dt = clock.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()

pygame.quit()