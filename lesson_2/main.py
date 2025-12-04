import pygame
from models import Ball

WIDTH = 600
HEIGHT = 400
CLOCK = 60
BG_COLOR = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing balls")

clock = pygame.time.Clock()

balls = [
    Ball(100, 100, 30, (255, 0, 0), 4, 2),
    Ball(300, 200, 20, (0, 255, 0), -3, 5),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    for ball in balls:
        ball.update(screen)

    pygame.display.flip()
    clock.tick(CLOCK)

pygame.quit()
