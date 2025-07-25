# Flappy bird mini-game using Python!!

import pygame
import random

# pygame setup
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Flappy Bird")
clock = pygame.time.Clock()
running = True

# Bird settings
bird = pygame.Rect(100, 250, 30, 30)
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Pipe settings
pipe_width = 60
pipe_gap = 200
pipe_speed = 3
pipes = []

# Game state
game_over = False
score = 0

# Create first pipe
def create_pipe():
    gap_y = random.randint(100, height - 300)
    top_pipe = pygame.Rect(width, 0, pipe_width, gap_y)
    bottom_pipe = pygame.Rect(width, gap_y + pipe_gap, pipe_width, height - gap_y - pipe_gap)
    return [top_pipe, bottom_pipe]

# Add first pipe
pipes.append(create_pipe())

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_strength
            if event.key == pygame.K_r and game_over:
                # Reset game
                bird.y = 250
                bird_velocity = 0
                pipes = [create_pipe()]
                game_over = False
                score = 0

    if not game_over:
        # Bird physics
        bird_velocity += gravity
        bird.y += bird_velocity

        # Move pipes
        for pipe_pair in pipes:
            pipe_pair[0].x -= pipe_speed  # top pipe
            pipe_pair[1].x -= pipe_speed  # bottom pipe

        # Add new pipes
        if pipes[-1][0].x < width - 300:
            pipes.append(create_pipe())

        # Remove old pipes and count score
        if pipes[0][0].x < -pipe_width:
            pipes.pop(0)
            score += 1

        # Check collisions
        for pipe_pair in pipes:
            if bird.colliderect(pipe_pair[0]) or bird.colliderect(pipe_pair[1]):
                game_over = True

        # Check if bird hits ground or ceiling
        if bird.y > height - 30 or bird.y < 0:
            game_over = True

    # Draw everything
    screen.fill("lightblue")
    
    # Draw pipes
    for pipe_pair in pipes:
        pygame.draw.rect(screen, "green", pipe_pair[0])  # top pipe
        pygame.draw.rect(screen, "green", pipe_pair[1])  # bottom pipe
    
    # Draw bird
    pygame.draw.rect(screen, "yellow", bird)
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))
    
    # Draw game over message
    if game_over:
        game_over_text = font.render("Game Over! Press R to restart", True, "red")
        screen.blit(game_over_text, (width//2 - 150, height//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()