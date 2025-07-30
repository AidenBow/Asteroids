import pygame
import random
from circleshape import CircleShape
from constants import *


class Score(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 7)
        self.total_points = 0
        self.font = pygame.font.Font(None, 36)
        self.font_color = "white"
        self.time_to_be_red = 0

    def draw(self, screen):
        text = self.font.render(f"Good job Reef! You defeated {self.total_points} peppers!", 1, self.font_color)
        textpos = text.get_rect(center=(SCREEN_WIDTH/2, 100))
        screen.blit(text, textpos)
        
    def update(self, dt):
        pass

    def add_points(self, dt):

        self.font_color = "red"
        self.total_points += 1
        