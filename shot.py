import pygame
from circleshape import CircleShape
from pygame.math import Vector2
from constants import *

class Shot(CircleShape):
    def __init__(self, position, radius):
      position_copy = Vector2(position.x, position.y)
      super().__init__(position, radius)
      self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
      pygame.draw.circle(self.image, WHITE, (radius, radius), radius)
      self.rect = self.image.get_rect()
      self.velocity = Vector2(0, 0)
    
    def update(self, dt):
      self.position += self.velocity * dt
      self.rect.center = self.position
        