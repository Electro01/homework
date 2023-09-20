import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SPEED = 5
PADDLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Initialize ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Initialize paddle positions
paddle1_y = (HEIGHT - 80) // 2
paddle2_y = (HEIGHT - 80) // 2

# Score variables
score1 = 0
score2 = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - 80:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - 80:
        paddle2_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy *= -1

    # Ball collisions with paddles
    if (
        ball_x <= 30
        and paddle1_y <= ball_y <= paddle1_y + 80
        and ball_dx < 0
    ) or (
        ball_x >= WIDTH - 30
        and paddle2_y <= ball_y <= paddle2_y + 80
        and ball_dx > 0
    ):
        ball_dx *= -1

    # Ball out of bounds (score)
    if ball_x <= 0:
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED

    if ball_x >= WIDTH:
        score1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = -BALL_SPEED
        ball_dy = -BALL_SPEED

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (10, paddle1_y, 10, 80))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, paddle2_y, 10, 80))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))

    # Draw scores
    font = pygame.font.Font(None, 36)
    score_display1 = font.render(str(score1), True, WHITE)
    score_display2 = font.render(str(score2), True, WHITE)
    screen.blit(score_display1, (50, 50))
    screen.blit(score_display2, (WIDTH - 80, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

