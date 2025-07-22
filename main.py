import pygame

# pygame setup
pygame.init()
width = 1280 # width of your application window
height = 720 # height of your application window
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

dy = 0 #Velocity with respect to the y-axis
ay = -20 #Acceleration with respect to the y-axis

rect = pygame.Rect(150, 150, 150, 150)

while running:
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    pygame.draw.rect(screen, "black", rect)

    keys = pygame.key.get_pressed()
    if rect.y < height - 150:
        rect.y += 300 * dy

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dy += clock.tick(60) / 20000

pygame.quit()