import pygame
from pygame.math import Vector2
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(Vector2(x, y), radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        # may need draw_top_right=None as the last parameter, leave it empty for now.
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        