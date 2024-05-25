import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game objects dimensions
paddle_width, paddle_height = 10, 100
ball_width, ball_height = 10, 10

# Paddle speed and positions
paddle_speed = 10
left_paddle_x, left_paddle_y = 50, (screen_height / 2) - (paddle_height / 2)
right_paddle_x, right_paddle_y = screen_width - 50 - paddle_width, (screen_height / 2) - (paddle_height / 2)

# Ball speed and position
ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
ball_x, ball_y = (screen_width / 2) - (ball_width / 2), (screen_height / 2) - (ball_height / 2)

# Score
left_score, right_score = 0, 0
font = pygame.font.Font(None, 74)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= left_paddle_x + paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height) or \
       (ball_x + ball_width >= right_paddle_x and right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_speed_x *= -1

    # Score update
    if ball_x < 0:
        right_score += 1
        ball_x, ball_y = (screen_width / 2) - (ball_width / 2), (screen_height / 2) - (ball_height / 2)
        ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
    if ball_x > screen_width:
        left_score += 1
        ball_x, ball_y = (screen_width / 2) - (ball_width / 2), (screen_height / 2) - (ball_height / 2)
        ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_width, ball_height))
    pygame.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height))

    left_score_text = font.render(str(left_score), True, white)
    screen.blit(left_score_text, (screen_width / 4, 10))

    right_score_text = font.render(str(right_score), True, white)
    screen.blit(right_score_text, (screen_width * 3 / 4, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
