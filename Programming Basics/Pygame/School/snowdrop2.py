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
x1 = random.randint(0, size[0] - 10)
x2 = random.randint(0, size[0] - 10)
x3 = random.randint(0, size[0] - 10)
y1 = random.randint(-100, 0)
y2 = random.randint(-100, 0)
y3 = random.randint(-100, 0)
speed1 = random.randint(2, 6)
speed2 = random.randint(2, 6)
speed3 = random.randint(2, 6)

while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic: move left and right
    y1 = y1 + speed1
    y2 = y2 + speed2
    y3 = y3 + speed3
    if y1 > size[1]:
        x1 = random.randint(0, size[0] - 10)
        y1 = random.randint(-50, 0)
        speed1 = random.randint(2, 6)
    if y2 > size[1]:
        x2 = random.randint(0, size[0] - 10)
        y2 = random.randint(-50, 0)
        speed2 = random.randint(2, 6)
    if y3 > size[1]:
        x3 = random.randint(0, size[0] - 10)
        y3 = random.randint(-50, 0)
        speed3 = random.randint(2, 6)

    # --- Screen-clearing code
    screen.fill(BLACK)

    # --- Drawing code:
    pygame.draw.rect(screen, WHITE, [x1, y1, 10, 10])
    pygame.draw.rect(screen, WHITE, [x2, y2, 10, 10])
    pygame.draw.rect(screen, WHITE, [x3, y3, 10, 10])


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
