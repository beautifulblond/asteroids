import pygame
from pygame.math import Vector2
from constants import *
from circleshape import CircleShape
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius, shots_group):
        super().__init__(Vector2(x, y), radius)
        self.rotation = 0
        self.shots_group = shots_group
        self.radius = PLAYER_RADIUS
        
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
        self.MAX_SPEED = 300
        self.FRICTION = 0.99
        
        self.last_shot_time = 0
        self.SHOT_COOLDOWN = 250
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        self.velocity *= self.FRICTION
        
        thrust = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += thrust * PLAYER_SPEED * dt
        
        if self.velocity.length() > self.MAX_SPEED:
            self.velocity.scale_to_length(self.MAX_SPEED)
        
        self.position += self.velocity * dt
        self.rect.center = self.position
        
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.SHOT_COOLDOWN:
            print("before shoot:", self.velocity)
            shot_position = Vector2(self.position.x, self.position.y)
            new_shot = Shot(self.position, SHOT_RADIUS)
        
            direction = Vector2(0, 1).rotate(self.rotation)
            #direction = direction.rotate(self.rotation)
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED
        
            '''shot_velocity = Vector2(0, 1)
            shot_velocity.rotate_ip(self.rotation)
            shot_velocity *= PLAYER_SHOOT_SPEED
            new_shot.velocity = shot_velocity'''
        
            self.shots_group.add(new_shot)
            self.last_shot_time = current_time
            print(f"Shot velocity: {new_shot.velocity}")
            print("After shoot:", self.velocity)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_e]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()