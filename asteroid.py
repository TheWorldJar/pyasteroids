import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255, 255, 255), 
                           self.position, 
                           self.radius, 
                           2)
    
    def update(self, dt):
        change = self.velocity * dt
        self.position += change

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0, 50.0)
            vec1 = pygame.Vector2(self.velocity).rotate(angle)
            vec2 = pygame.Vector2(self.velocity).rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = vec1 * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = vec2 * 1.2