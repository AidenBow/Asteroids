import pygame
import random
from circleshape import CircleShape
from constants import *


class Score(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 7)
        self.total_points = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text = self.font.render(f"Good job Reef! You defeated {self.total_points} peppers!", 1, "white")
        textpos = text.get_rect(centerx=SCREEN_WIDTH/2)
        screen.blit(text, textpos)
        

    def update(self, dt):
        pass

    def add_points(self):
        self.total_points += 1