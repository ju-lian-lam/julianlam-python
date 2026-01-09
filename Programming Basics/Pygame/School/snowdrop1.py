import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
gameOver = False
xPos = 345
yPos = 10
rect_width = 10
rect_len = 10
speed = 5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic: move left and right
    yPos = yPos + speed
    if yPos <= 0 or yPos >= size[1] - rect_len:
        xPos = random.randint(0, size[0] - rect_width)
        yPos = 0

    # --- Screen-clearing code
    screen.fill(BLACK)

    # --- Drawing code
    pygame.draw.rect(screen, WHITE, [xPos, yPos, rect_width, rect_len])

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
