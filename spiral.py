import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Colors and Font
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
font = pygame.font.SysFont('monospace', 20)

# Setup for the rain drops
drops = [1 for _ in range(WIDTH // 20)]

# Game loop
while True:
    screen.fill(BLACK)
    for i, y in enumerate(drops):
        text = font.render(random.choice("01"), True, GREEN)
        x = i * 20
        screen.blit(text, (x, y * 20))
        drops[i] = y + 1 if y * 20 < HEIGHT and random.random() > 0.975 else 0
    pygame.display.flip()