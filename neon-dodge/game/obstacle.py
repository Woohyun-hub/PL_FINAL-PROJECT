import pygame
import random
from .settings import *

class Obstacle:
    def __init__(self, difficulty):
        size = random.randint(25, 60)
        x = random.randint(0, SCREEN_WIDTH - size)

        self.rect = pygame.Rect(x, -size, size, size)

        self.speed = random.randint(3 + difficulty, 7 + difficulty)

        self.horizontal = random.random() < 0.3
        self.dx = random.choice([-2, 2])

    def update(self):
        self.rect.y += self.speed

        if self.horizontal:
            self.rect.x += self.dx
            if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.dx *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, NEON_PINK, self.rect)
