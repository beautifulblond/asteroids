import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)


def main():
    
    
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

	
	AsteroidField()
	pygame.init()

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
 
	ticktock = pygame.time.Clock()
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				  return

		updateable.update(dt)
  
		for asteroid in asteroids:
			if asteroid.collision_check(player) == False:
				print("Game over!")
				sys.exit()
    

		screen.fill("black")
		for sprite in drawable:
			sprite.draw(screen)
			
		pygame.display.flip()
		#ticktock.tick(60)
		dt = ticktock.tick(60) / 1000

if __name__ == "__main__":
	main()
