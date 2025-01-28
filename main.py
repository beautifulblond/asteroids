import pygame
from constants import *
from player import Player

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)


def main():
	pygame.init()
 
	ticktock = pygame.time.Clock()
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				  return

			player.update(dt)
			screen.fill("black")
			player.draw(screen)
			pygame.display.flip()
		ticktock.tick(60)
		dt = ticktock.tick(60) / 1000
	
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
