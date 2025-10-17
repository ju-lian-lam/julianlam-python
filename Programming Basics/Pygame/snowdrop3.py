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
snowdrops = []
for i in range(500):
    x = random.randint(0, size[0] - 10)
    y = random.randint(-100, 0)
    width = 10
    height = 10
    speed = random.randint(2, 6)
    horizontalvelocity = random.randint(-2, 2)
    snowdrops.append({"x": x, "y": y, "speed": speed, "horizontalvelocity": horizontalvelocity})

while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic: move left and right
    for drop in snowdrops:
        drop["y"] = drop["y"] + drop["speed"]
        drop["x"] = drop["x"] + drop["horizontalvelocity"]
        
        if drop["y"] > size[1]:
            drop["x"] = random.randint(0, size[0] - 10)
            drop["y"] = random.randint(-50, 0)
            drop["speed"] = random.randint(2, 6)
            drop["horizontalvelocity"] = random.randint(-2, 2)

    # --- Screen-clearing code
    screen.fill(BLACK)

    # --- Drawing code
    for drop in snowdrops:
        pygame.draw.rect(screen, WHITE, [drop["x"], drop["y"], width, height])

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
