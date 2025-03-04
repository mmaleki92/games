# Pygame Tutorial: From Beginner to Advanced

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Your First Pygame Window](#your-first-pygame-window)
4. [Game Loop Fundamentals](#game-loop-fundamentals)
5. [Drawing Shapes and Images](#drawing-shapes-and-images)
6. [Handling User Input](#handling-user-input)
7. [Movement and Physics](#movement-and-physics)
8. [Collision Detection](#collision-detection)
9. [Sprites and Object-Oriented Approach](#sprites-and-object-oriented-approach)
10. [Animation](#animation)
11. [Sound and Music](#sound-and-music)
12. [Game States](#game-states)
13. [Text and UI](#text-and-ui)
14. [Advanced Topics](#advanced-topics)
15. [Complete Game Example](#complete-game-example)

## Introduction

Pygame is a set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. Pygame is built on top of the SDL library, providing a simple interface to various hardware components like the display, sound, music, and input devices.

This tutorial will guide you through creating games with Pygame, starting with the basics and progressing to advanced concepts.

## Installation

First, let's install Pygame. Open your terminal or command prompt and run:

```python
pip install pygame
```

To verify the installation:

```python
import pygame
pygame.init()
print(f"Pygame version: {pygame.__version__}")
```

## Your First Pygame Window

Let's create a simple window to start:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black background
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
```

Save this as `first_window.py` and run it. You should see a black window that you can close by clicking the X button.

## Game Loop Fundamentals

Every game has a main loop that continuously updates and renders the game. The basic structure is:

```python
while running:
    # Handle events (input)
    for event in pygame.event.get():
        # Process events
    
    # Update game state
    # ...
    
    # Render graphics
    # ...
    
    # Update display
    pygame.display.flip()  # or pygame.display.update()
    
    # Control game speed
    clock.tick(FPS)
```

Let's enhance our previous example with a proper game loop:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Loop Example")

# Set up the clock for a decent framerate
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game state
    
    # Fill the screen with a color
    screen.fill((50, 50, 50))  # Dark gray background
    
    # Draw a simple shape
    pygame.draw.circle(screen, (255, 0, 0), (WIDTH//2, HEIGHT//2), 50)
    
    # Update the display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
```

## Drawing Shapes and Images

Pygame provides functions to draw various shapes and load images.

### Drawing Shapes:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Shapes")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # White background
    
    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
    
    # Draw a circle
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 80)
    
    # Draw a line
    pygame.draw.line(screen, (0, 0, 255), (100, 400), (700, 500), 5)
    
    # Draw a polygon
    pygame.draw.polygon(screen, (255, 255, 0), [(600, 100), (700, 200), (650, 300)])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### Loading Images:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loading Images")
clock = pygame.time.Clock()

# Load an image
# Replace 'player.png' with your image file path
player_image = pygame.image.load('player.png')
# Optional: scale the image
player_image = pygame.transform.scale(player_image, (100, 100))
# Optional: get the rectangle for positioning
player_rect = player_image.get_rect(center=(WIDTH//2, HEIGHT//2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    # Draw the image
    screen.blit(player_image, player_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Handling User Input

### Keyboard Events:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Input")
clock = pygame.time.Clock()

x, y = WIDTH//2, HEIGHT//2
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Event-based input (for one-time actions)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed once")
    
    # State-based input (for continuous movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Ensure player stays on screen
    x = max(0, min(WIDTH, x))
    y = max(0, min(HEIGHT, y))
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### Mouse Events:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Input")
clock = pygame.time.Clock()

circles = []  # List to store circles

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Create circle when clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                pos = pygame.mouse.get_pos()
                circles.append((pos, (255, 0, 0)))
            elif event.button == 3:  # Right click
                pos = pygame.mouse.get_pos()
                circles.append((pos, (0, 0, 255)))
    
    # Get current mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    screen.fill((255, 255, 255))
    
    # Draw all circles in our list
    for pos, color in circles:
        pygame.draw.circle(screen, color, pos, 30)
    
    # Draw a circle that follows the mouse
    pygame.draw.circle(screen, (0, 255, 0), mouse_pos, 15)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Movement and Physics

Let's create a simple example with basic movement and gravity:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movement and Physics")
clock = pygame.time.Clock()

# Player properties
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_width, player_height = 50, 50
velocity_x, velocity_y = 0, 0
gravity = 0.5
jump_strength = -10
on_ground = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_strength
    
    # Horizontal movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        velocity_x = 5
    else:
        velocity_x = 0
    
    # Apply gravity
    velocity_y += gravity
    
    # Update position
    player_x += velocity_x
    player_y += velocity_y
    
    # Check for ground collision
    if player_y + player_height >= HEIGHT:
        player_y = HEIGHT - player_height
        velocity_y = 0
        on_ground = True
    else:
        on_ground = False
    
    # Check for wall collisions
    if player_x < 0:
        player_x = 0
    if player_x + player_width > WIDTH:
        player_x = WIDTH - player_width
    
    screen.fill((200, 200, 255))
    
    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    # Draw ground
    pygame.draw.rect(screen, (0, 100, 0), (0, HEIGHT - 10, WIDTH, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Collision Detection

### Rectangle Collision:

```python
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection")
clock = pygame.time.Clock()

# Player rectangle
player = pygame.Rect(100, 100, 50, 50)
player_color = (255, 0, 0)
player_speed = 5

# Obstacles
obstacles = [
    pygame.Rect(200, 200, 100, 50),
    pygame.Rect(400, 300, 80, 80),
    pygame.Rect(600, 150, 60, 200),
]
obstacle_color = (0, 0, 255)

# Collectible
collectible = pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 30, 30)
collectible_color = (255, 255, 0)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    
    # Keep player on screen
    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
    
    # Check for collision with obstacles
    collision = False
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            collision = True
    
    # Change player color based on collision
    player_color = (255, 100, 100) if collision else (255, 0, 0)
    
    # Check for collectible collision
    if player.colliderect(collectible):
        score += 1
        collectible.x = random.randint(50, WIDTH-50)
        collectible.y = random.randint(50, HEIGHT-50)
    
    screen.fill((255, 255, 255))
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)
    
    # Draw collectible
    pygame.draw.rect(screen, collectible_color, collectible)
    
    # Draw player
    pygame.draw.rect(screen, player_color, player)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Sprites and Object-Oriented Approach

Sprites are a key concept in Pygame, providing an object-oriented way to manage game elements:

```python
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites Example")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a simple player sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20))
        )
    
    def respawn(self):
        self.rect.center = (random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20))

# Create sprite groups
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create coins
for _ in range(10):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()
    
    # Check for collisions between player and coins
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected_coins:
        score += 1
        # Create a new coin to replace the collected one
        new_coin = Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)
    
    # Draw
    screen.fill((50, 50, 50))
    all_sprites.draw(screen)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Animation

Let's create a simple sprite sheet animation:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation Example")
clock = pygame.time.Clock()

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # For this example, let's create a fake spritesheet
        # In a real game, you would load this from an image file
        self.spritesheet = pygame.Surface((200, 50))
        for i in range(4):
            color = (255, 0, 0) if i % 2 == 0 else (0, 0, 255)
            pygame.draw.rect(self.spritesheet, color, (i*50, 0, 50, 50))
        
        # Animation frames
        self.frames = []
        for i in range(4):
            frame = self.spritesheet.subsurface((i*50, 0, 50, 50))
            self.frames.append(frame)
        
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Animation speed
        self.animation_time = 0
        self.animation_speed = 200  # milliseconds
    
    def update(self, dt):
        # Update animation
        self.animation_time += dt
        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        
        # Move sprite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Create sprite group
all_sprites = pygame.sprite.Group()
player = AnimatedSprite()
all_sprites.add(player)

running = True
last_time = pygame.time.get_ticks()

while running:
    # Calculate delta time
    current_time = pygame.time.get_ticks()
    dt = current_time - last_time
    last_time = current_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update(dt)
    
    # Draw
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Sound and Music

Playing sound effects and music:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sound and Music Example")
clock = pygame.time.Clock()

# Initialize the mixer
pygame.mixer.init()

# Load sound effects
# Replace with your own sound files
try:
    jump_sound = pygame.mixer.Sound("jump.wav")
    collect_sound = pygame.mixer.Sound("collect.wav")
except pygame.error:
    # Create fallback sound if files not found
    jump_sound = pygame.mixer.Sound.fromstring(bytes([128] * 1000), 22050, 8)
    collect_sound = pygame.mixer.Sound.fromstring(bytes([128] * 1000), 22050, 8)

# Load background music
try:
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # 50% volume
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
except pygame.error:
    print("Music file not found. No background music will play.")

font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_sound.play()
            elif event.key == pygame.K_c:
                collect_sound.play()
            elif event.key == pygame.K_m:
                # Toggle music
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    
    screen.fill((50, 50, 100))
    
    # Display instructions
    instructions = [
        "Press SPACE to play jump sound",
        "Press C to play collect sound",
        "Press M to toggle music"
    ]
    
    for i, text in enumerate(instructions):
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, 50 + i*40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Game States

Managing different game states (menu, game, game over):

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game States Example")
clock = pygame.time.Clock()

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

current_state = MENU
score = 0
player_pos = [WIDTH // 2, HEIGHT // 2]

# Fonts
title_font = pygame.font.SysFont(None, 72)
menu_font = pygame.font.SysFont(None, 48)
game_font = pygame.font.SysFont(None, 36)

def draw_menu():
    screen.fill((50, 0, 100))
    
    # Title
    title = title_font.render("Game States Demo", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(title, title_rect)
    
    # Play button
    play_text = menu_font.render("Press SPACE to Play", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(play_text, play_rect)
    
    # Quit button
    quit_text = menu_font.render("Press Q to Quit", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    screen.blit(quit_text, quit_rect)

def draw_game():
    screen.fill((0, 100, 50))
    
    # Player
    pygame.draw.circle(screen, (255, 0, 0), player_pos, 30)
    
    # Score
    score_text = game_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # Instructions
    instructions = game_font.render("Arrow keys to move, ESC to menu", True, (255, 255, 255))
    instructions_rect = instructions.get_rect(center=(WIDTH//2, HEIGHT - 30))
    screen.blit(instructions, instructions_rect)

def draw_game_over():
    screen.fill((100, 0, 0))
    
    # Game over text
    over_text = title_font.render("GAME OVER", True, (255, 255, 255))
    over_rect = over_text.get_rect(center=(WIDTH//2, HEIGHT//3))
    screen.blit(over_text, over_rect)
    
    # Final score
    score_text = menu_font.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(score_text, score_rect)
    
    # Restart instruction
    restart_text = menu_font.render("Press SPACE to play again", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    screen.blit(restart_text, restart_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if current_state == MENU:
                if event.key == pygame.K_SPACE:
                    current_state = PLAYING
                    score = 0
                    player_pos = [WIDTH // 2, HEIGHT // 2]
                elif event.key == pygame.K_q:
                    running = False
            
            elif current_state == PLAYING:
                if event.key == pygame.K_ESCAPE:
                    current_state = MENU
                # For demo purposes, let's end the game after reaching a certain score
                if score >= 10:
                    current_state = GAME_OVER
            
            elif current_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    current_state = PLAYING
                    score = 0
                    player_pos = [WIDTH // 2, HEIGHT // 2]
    
    # Game logic based on state
    if current_state == PLAYING:
        # Move player and update score
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5
        
        # Keep player on screen
        player_pos[0] = max(30, min(player_pos[0], WIDTH - 30))
        player_pos[1] = max(30, min(player_pos[1], HEIGHT - 30))
        
        # Increment score (for demo purposes)
        score += 0.01
    
    # Draw based on current state
    if current_state == MENU:
        draw_menu()
    elif current_state == PLAYING:
        draw_game()
    elif current_state == GAME_OVER:
        draw_game_over()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Text and UI

Creating buttons and text elements:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UI Example")
clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.SysFont(None, 36)
    
    def draw(self, screen):
        # Draw button background
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        
        # Draw button border
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        
        # Draw button text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def update(self):
        # Check if mouse is hovering over button
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False

class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.font = pygame.font.SysFont(None, 32)
    
    def draw(self, screen):
        # Draw input box
        color = (100, 200, 255) if self.active else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        
        # Render text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        # Ensure text doesn't overflow
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 5, self.rect.y + self.rect.height // 2))
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state
            self.active = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(f"Input submitted: {self.text}")
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                # Add character to text, limit length
                if len(self.text) < 20:  # Limit to 20 chars
                    self.text += event.unicode

# Create UI elements
start_button = Button(300, 200, 200, 50, "Start", (0, 255, 0), (100, 255, 100))
quit_button = Button(300, 300, 200, 50, "Quit", (255, 0, 0), (255, 100, 100))
name_input = TextInput(250, 400, 300, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle button clicks
        if start_button.is_clicked(event):
            print("Start button clicked!")
        if quit_button.is_clicked(event):
            running = False
        
        # Handle text input
        name_input.handle_event(event)
    
    # Update
    start_button.update()
    quit_button.update()
    
    # Draw
    screen.fill((240, 240, 240))
    start_button.draw(screen)
    quit_button.draw(screen)
    name_input.draw(screen)
    
    # Display instructions
    font = pygame.font.SysFont(None, 36)
    instructions = font.render("Enter your name:", True, (0, 0, 0))
    screen.blit(instructions, (250, 360))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Advanced Topics

### Camera System

Let's implement a basic camera system to follow the player in a scrolling world:

```python
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Camera System")
clock = pygame.time.Clock()

# World size (larger than screen)
WORLD_WIDTH, WORLD_HEIGHT = 2000, 1500

class Camera:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity_rect):
        # Returns the rect's position relative to the camera
        return pygame.Rect(entity_rect.x - self.rect.x, 
                         entity_rect.y - self.rect.y,
                         entity_rect.width, entity_rect.height)
    
    def update(self, target):
        # Center the camera on the target
        x = -target.centerx + WIDTH // 2
        y = -target.centery + HEIGHT // 2
        
        # Limit scrolling to world size
        x = min(0, x)  # Left boundary
        y = min(0, y)  # Top boundary
        x = max(-(WORLD_WIDTH - WIDTH), x)  # Right boundary
        y = max(-(WORLD_HEIGHT - HEIGHT), y)  # Bottom boundary
        
        self.rect.x = x
        self.rect.y = y

# Player 
player = pygame.Rect(WORLD_WIDTH//2, WORLD_HEIGHT//2, 50, 50)
player_speed = 8

# Create some trees for the world
trees = []
for _ in range(100):
    tree = pygame.Rect(
        random.randint(50, WORLD_WIDTH-50),
        random.randint(50, WORLD_HEIGHT-50),
        30, 60)
    trees.append(tree)

# Initialize camera
camera = Camera(WIDTH, HEIGHT)

# Background texture
bg_color = (50, 150, 50)  # Green for grass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    
    # Keep player in world bounds
    player.left = max(0, player.left)
    player.right = min(WORLD_WIDTH, player.right)
    player.top = max(0, player.top)
    player.bottom = min(WORLD_HEIGHT, player.bottom)
    
    # Update camera
    camera.update(player)
    
    # Draw background
    screen.fill(bg_color)
    
    # Draw grid for reference
    grid_color = (100, 180, 100)
    grid_spacing = 100
    
    # Draw vertical grid lines
    for x in range(0, WORLD_WIDTH, grid_spacing):
        # Only draw lines that are visible on screen
        if 0 <= x + camera.rect.x <= WIDTH:
            pygame.draw.line(screen, grid_color, 
                           (x + camera.rect.x, 0), 
                           (x + camera.rect.x, HEIGHT))
    
    # Draw horizontal grid lines
    for y in range(0, WORLD_HEIGHT, grid_spacing):
        # Only draw lines that are visible on screen
        if 0 <= y + camera.rect.y <= HEIGHT:
            pygame.draw.line(screen, grid_color, 
                           (0, y + camera.rect.y), 
                           (WIDTH, y + camera.rect.y))
    
    # Draw trees
    for tree in trees:
        # Only draw trees that are visible on screen
        tree_rect = camera.apply(tree)
        if (tree_rect.right >= 0 and tree_rect.left <= WIDTH and
            tree_rect.bottom >= 0 and tree_rect.top <= HEIGHT):
            pygame.draw.rect(screen, (100, 50, 0), tree_rect)  # Brown for tree trunk
    
    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), camera.apply(player))
    
    # Draw world boundary indicator
    # This will help visualize where the world ends
    pygame.draw.rect(screen, (255, 0, 0), 
                   (camera.rect.x, camera.rect.y, WORLD_WIDTH, WORLD_HEIGHT), 2)
    
    # Draw minimap (top-right corner)
    minimap_rect = pygame.Rect(WIDTH - 210, 10, 200, 150)
    pygame.draw.rect(screen, (0, 0, 0), minimap_rect)
    pygame.draw.rect(screen, (50, 50, 50), minimap_rect.inflate(-4, -4))
    
    # Calculate scale factor for minimap
    scale_x = minimap_rect.width / WORLD_WIDTH
    scale_y = minimap_rect.height / WORLD_HEIGHT
    
    # Draw player on minimap
    mini_player = pygame.Rect(
        minimap_rect.x + player.x * scale_x,
        minimap_rect.y + player.y * scale_y,
        max(2, player.width * scale_x),
        max(2, player.height * scale_y)
    )
    pygame.draw.rect(screen, (255, 0, 0), mini_player)
    
    # Display coordinates
    font = pygame.font.SysFont(None, 24)
    coords = font.render(f"X: {player.centerx}, Y: {player.centery}", True, (255, 255, 255))
    screen.blit(coords, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### Particle Systems

Let's implement a simple particle system:

```python
import pygame
import sys
import random
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle System")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, color, size=5, lifetime=60):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.gravity = 0.1
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.lifetime -= 1
        # Shrink particle as it ages
        self.size = self.size * (self.lifetime / self.max_lifetime)
    
    def draw(self, screen):
        # Fade out particle as it ages
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        color = (*self.color, alpha)
        
        # Create a surface for the particle
        surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, color, (self.size, self.size), self.size)
        
        # Blit the surface onto the screen
        screen.blit(surf, (self.x - self.size, self.y - self.size))
    
    def is_alive(self):
        return self.lifetime > 0

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def emit(self, x, y, count, color, size_range=(3, 8), lifetime_range=(30, 90)):
        for _ in range(count):
            size = random.uniform(*size_range)
            lifetime = random.randint(*lifetime_range)
            self.particles.append(Particle(x, y, color, size, lifetime))
    
    def update(self):
        # Update particles and remove dead ones
        self.particles = [p for p in self.particles if p.is_alive()]
        for particle in self.particles:
            particle.update()
    
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

# Create particle systems
fire_particles = ParticleSystem()
water_particles = ParticleSystem()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((20, 20, 20))
    
    # Get mouse position and buttons
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    
    # Emit particles based on mouse input
    if mouse_buttons[0]:  # Left mouse button for fire
        fire_particles.emit(mouse_pos[0], mouse_pos[1], 5, (255, 100, 0), (4, 8), (40, 60))
    if mouse_buttons[2]:  # Right mouse button for water
        water_particles.emit(mouse_pos[0], mouse_pos[1], 5, (0, 100, 255), (3, 6), (30, 50))
    
    # Update and draw particle systems
    fire_particles.update()
    water_particles.update()
    
    water_particles.draw(screen)
    fire_particles.draw(screen)
    
    # Draw instructions
    font = pygame.font.SysFont(None, 28)
    instructions1 = font.render("Left click: Fire particles", True, (255, 255, 255))
    instructions2 = font.render("Right click: Water particles", True, (255, 255, 255))
    screen.blit(instructions1, (10, 10))
    screen.blit(instructions2, (10, 40))
    
    # Display particle count
    count = font.render(f"Particle count: {len(fire_particles.particles) + len(water_particles.particles)}", 
                      True, (255, 255, 255))
    screen.blit(count, (10, HEIGHT - 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### Tilemaps

Creating and rendering a simple tilemap:

```python
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tilemap Example")
clock = pygame.time.Clock()

# Tile constants
TILE_SIZE = 50
MAP_WIDTH, MAP_HEIGHT = 20, 15

# Tile types
GRASS = 0
WATER = 1
SAND = 2
STONE = 3

# Tile colors
TILE_COLORS = {
    GRASS: (0, 153, 0),
    WATER: (51, 153, 255),
    SAND: (255, 255, 153),
    STONE: (128, 128, 128)
}

# Create a simple tilemap
# 0 = grass, 1 = water, 2 = sand, 3 = stone
tilemap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
    [1, 2, 2, 0, 0, 0, 2, 2, 1, 1, 1, 1, 2, 2, 2, 0, 0, 2, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
    [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Camera position
camera_x, camera_y = 0, 0
camera_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move camera with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x = max(0, camera_x - camera_speed)
    if keys[pygame.K_RIGHT]:
        max_x = MAP_WIDTH * TILE_SIZE - WIDTH
        camera_x = min(max_x, camera_x + camera_speed)
    if keys[pygame.K_UP]:
        camera_y = max(0, camera_y - camera_speed)
    if keys[pygame.K_DOWN]:
        max_y = MAP_HEIGHT * TILE_SIZE - HEIGHT
        camera_y = min(max_y, camera_y + camera_speed)
    
    screen.fill((0, 0, 0))
    
    # Render visible portion of tilemap
    start_row = camera_y // TILE_SIZE
    end_row = min(MAP_HEIGHT, start_row + HEIGHT // TILE_SIZE + 2)
    start_col = camera_x // TILE_SIZE
    end_col = min(MAP_WIDTH, start_col + WIDTH // TILE_SIZE + 2)
    
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            tile_type = tilemap[row][col]
            rect = pygame.Rect(
                col * TILE_SIZE - camera_x,
                row * TILE_SIZE - camera_y,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, TILE_COLORS[tile_type], rect)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)  # Grid lines
    
    # Display camera position
    font = pygame.font.SysFont(None, 24)
    cam_text = font.render(f"Camera: ({camera_x}, {camera_y})", True, (255, 255, 255))
    screen.blit(cam_text, (10, 10))
    
    # Instructions
    instructions = font.render("Arrow keys to move camera", True, (255, 255, 255))
    screen.blit(instructions, (10, HEIGHT - 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

## Complete Game Example

Let's create a simple but complete game combining many of the concepts we've learned:

```python
import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLATFORM_SPEED = 2
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.velocity_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.max_jumps = 2  # Double jump
        self.score = 0
    
    def update(self, platforms):
        # Apply gravity
        self.velocity_y += GRAVITY
        
        # Move vertically
        self.rect.y += self.velocity_y
        
        # Check for ground collision
        self.on_ground = False
        for platform in platforms:
            if (self.rect.bottom >= platform.rect.top and
                self.rect.bottom <= platform.rect.top + 10 and
                self.rect.right >= platform.rect.left and
                self.rect.left <= platform.rect.right and
                self.velocity_y > 0):
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True
                self.jump_count = 0
                
                # Add score for landing on a platform
                if platform.point_value:
                    self.score += platform.point_value
                    platform.point_value = 0  # Only get points once per platform
        
        # Check for ceiling collision
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity_y = 0
        
        # Check for bottom of screen (game over)
        if self.rect.top > HEIGHT:
            return True  # Game over
        
        # Horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            # Wrap around screen edges
            if self.rect.right < 0:
                self.rect.left = WIDTH
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            # Wrap around screen edges
            if self.rect.left > WIDTH:
                self.rect.right = 0
        
        return False  # Game continues
    
    def jump(self):
        if self.on_ground or self.jump_count < self.max_jumps:
            self.velocity_y = JUMP_STRENGTH
            self.jump_count += 1
            self.on_ground = False
            return True
        return False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=PLATFORM_WIDTH, height=PLATFORM_HEIGHT, moving=False, color=GREEN):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.moving = moving
        self.direction = 1  # 1 for right, -1 for left
        self.speed = random.randint(1, 3) if moving else 0
        self.point_value = 10
    
    def update(self):
        if self.moving:
            self.rect.x += self.direction * self.speed
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.direction *= -1  # Reverse direction
        
        # Move platform upward
        self.rect.y -= PLATFORM_SPEED
        
        # Remove if off screen
        if self.rect.bottom < 0:
            self.kill()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = random.choice([RED, YELLOW, ORANGE])
        self.velocity_x = random.uniform(-2, 2)
        self.velocity_y = random.uniform(-3, -1)
        self.lifetime = random.randint(20, 40)
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.lifetime -= 1
        self.size = max(1, self.size * 0.95)
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))
    
    def is_alive(self):
        return self.lifetime > 0

# Define colors for better readability
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)

class Game:
    def __init__(self):
        self.state = MENU
        self.platforms = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.score = 0
        self.high_score = 0
        self.particles = []
        
        # Create initial platforms
        self.create_starting_platforms()
        
        # Load sounds
        self.jump_sound = pygame.mixer.Sound(self.generate_sound_effect(1))
        self.jump_sound.set_volume(0.2)
        self.land_sound = pygame.mixer.Sound(self.generate_sound_effect(0))
        self.land_sound.set_volume(0.2)
        self.game_over_sound = pygame.mixer.Sound(self.generate_sound_effect(2))
        self.game_over_sound.set_volume(0.3)
        
        # Font
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 72)
    
    def generate_sound_effect(self, sound_type):
        """Generate a simple sound effect if no sound file available"""
        if sound_type == 0:  # Landing sound
            arr = bytearray([128 - int(127 * math.sin(x/10)) for x in range(500)])
        elif sound_type == 1:  # Jump sound
            arr = bytearray([128 + int(127 * math.sin(x/5)) for x in range(500)])
        else:  # Game over sound
            arr = bytearray([
                128 + int(127 * math.sin(x/20) * math.sin(x/10)) 
                for x in range(2000)
            ])
        return arr
    
    def create_starting_platforms(self):
        # Create ground
        ground = Platform(0, HEIGHT - 40, WIDTH, 40, moving=False, color=GREEN)
        self.platforms.add(ground)
        self.all_sprites.add(ground)
        
        # Create some starting platforms
        for i in range(8):
            x = random.randint(0, WIDTH - PLATFORM_WIDTH)
            y = HEIGHT - (i + 2) * 70
            moving = random.choice([True, False])
            color = BLUE if moving else GREEN
            platform = Platform(x, y, moving=moving, color=color)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
    
    def add_platform(self):
        # Add a new platform at the top
        if random.random() < 0.7:  # 70% chance of adding a platform
            x = random.randint(0, WIDTH - PLATFORM_WIDTH)
            y = -PLATFORM_HEIGHT
            moving = random.random() < 0.3  # 30% chance of moving platform
            
            # Determine platform color and properties
            if random.random() < 0.1:  # 10% chance of special platform
                color = YELLOW
                width = PLATFORM_WIDTH // 2
            else:
                color = BLUE if moving else GREEN
                width = PLATFORM_WIDTH
                
            platform = Platform(x, y, width=width, moving=moving, color=color)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
    
    def reset_game(self):
        self.player = Player()
        self.platforms.empty()
        self.all_sprites.empty()
        self.all_sprites.add(self.player)
        self.particles = []
        self.score = 0
        self.create_starting_platforms()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == PLAYING:
                        self.state = MENU
                    elif self.state == MENU:
                        return False
                
                if event.key == pygame.K_SPACE:
                    if self.state == MENU:
                        self.state = PLAYING
                        self.reset_game()
                    elif self.state == PLAYING:
                        if self.player.jump():
                            self.jump_sound.play()
                            # Add jump particles
                            for _ in range(10):
                                self.particles.append(
                                    Particle(self.player.rect.centerx, self.player.rect.bottom)
                                )
                    elif self.state == GAME_OVER:
                        self.state = PLAYING
                        self.reset_game()
        
        return True
    
    def update(self):
        if self.state == PLAYING:
            # Update player and check for game over
            if self.player.update(self.platforms):
                self.state = GAME_OVER
                self.game_over_sound.play()
                if self.player.score > self.high_score:
                    self.high_score = self.player.score
            
            # Update platforms
            self.platforms.update()
            
            # Update particles
            self.particles = [p for p in self.particles if p.is_alive()]
            for particle in self.particles:
                particle.update()
            
            # Add new platforms occasionally
            if random.random() < 0.05:  # 5% chance per frame
                self.add_platform()
            
            # Update score based on player's score
            self.score = self.player.score
    
    def draw(self):
        screen.fill(BLACK)
        
        if self.state == MENU:
            # Draw menu
            title = self.title_font.render("PLATFORMER", True, WHITE)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))
            
            start = self.font.render("Press SPACE to Start", True, WHITE)
            screen.blit(start, (WIDTH//2 - start.get_width()//2, HEIGHT//2))
            
            if self.high_score > 0:
                high_score = self.font.render(f"High Score: {self.high_score}", True, WHITE)
                screen.blit(high_score, (WIDTH//2 - high_score.get_width()//2, HEIGHT//2 + 50))
            
            controls = self.font.render("Left/Right to move, SPACE to jump", True, LIGHT_BLUE)
            screen.blit(controls, (WIDTH//2 - controls.get_width()//2, HEIGHT - 100))
        
        elif self.state == PLAYING or self.state == GAME_OVER:
            # Draw all sprites
            self.all_sprites.draw(screen)
            
            # Draw particles
            for particle in self.particles:
                particle.draw(screen)
            
            # Draw score
            score_text = self.font.render(f"Score: {int(self.score)}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            # Draw game over message if needed
            if self.state == GAME_OVER:
                over_text = self.title_font.render("GAME OVER", True, RED)
                screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//3))
                
                restart = self.font.render("Press SPACE to Restart", True, WHITE)
                screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2))
                
                final_score = self.font.render(f"Final Score: {int(self.score)}", True, WHITE)
                screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2 + 50))
                
                if self.score >= self.high_score:
                    new_high = self.font.render("NEW HIGH SCORE!", True, YELLOW)
                    screen.blit(new_high, (WIDTH//2 - new_high.get_width()//2, HEIGHT//2 + 100))

# Create game instance
game = Game()

# Main game loop
running = True
while running:
    # Handle events
    running = game.handle_events()
    
    # Update game
    game.update()
    
    # Draw everything
    game.draw()
    
    # Update display and tick clock
    pygame.display.flip()
    clock.tick(FPS)

# Quit game
pygame.quit()
sys.exit()
