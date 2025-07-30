import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.pepper = pygame.image.load("images/PEPPER.png").convert_alpha()

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pepper = pygame.transform.scale(self.pepper, (self.radius*2, self.radius*2))
        pepperpos = pepper.get_rect(center=(self.position.x, self.position.y))
        screen.blit(pepper, pepperpos)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius:
            random_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(-random_angle)
            vector_2 = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = vector_2 * 1.2