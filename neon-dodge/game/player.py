import pygame
from .settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2,
            SCREEN_HEIGHT - 50,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, NEON_BLUE, self.rect)
