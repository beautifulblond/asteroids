import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.6
        a = self.position + forward * self.radius
        b = self.position - forward * self. radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        # Hoping this starts a new shot at the current player position, and not the default Player() position
        # shot.position = Player.position # May actually not be needed? or useful?
        # I think I use self.rotation to find the Player().rotation, i.e. the new shot starts at the sharpest tip of the triangle
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        # Should make the shot fire in the direction the player is facing
        # shot.position += shot.velocity * PLAYER_SHOT_SPEED * dt # I don't know wtf I'm doing
        #self.shots.add(shot)
        
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