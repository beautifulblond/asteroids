import pygame
from pygame.math import Vector2

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
        self.position = pygame.Vector2(position.x, position.y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collision_check(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        # True : collision, False : no collision
        return distance >= self.radius + CircleShape.radius
        
    
    def draw(self, screen):
        # subclass override
        pass

    def update(self, dt):
        # subclass override
        pass