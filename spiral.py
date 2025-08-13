import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starfield")
clock = pygame.time.Clock()

# Generate stars with random positions and speeds [x, y, speed]
stars = [[random.randrange(WIDTH), random.randrange(HEIGHT), random.uniform(1, 5)] for _ in range(300)]

# Main animation loop
while True:
    screen.fill((0, 0, 10))  # A dark blue space color
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); exit()

    for star in stars:
        # Move the star and reset it if it goes off-screen
        star[0] -= star[2]
        if star[0] < 0:
            star[0] = WIDTH; star[1] = random.randrange(HEIGHT)

        # Draw the star as a small circle
        pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), max(1, int(star[2] / 2)))

    pygame.display.flip()
    clock.tick(60) # Limit frame rate to 60 FPS