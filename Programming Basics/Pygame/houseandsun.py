import pygame, math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sun Moving Over House")

sun_radius = 40
sun_x = -sun_radius
sun_speed_x = 2.0

a = 0.0018
h = SCREEN_WIDTH / 2
k = 110
base_y = SCREEN_HEIGHT - 100

def house(surface, x, y, width, height, color):
    pygame.draw.rect(surface, color, [x, y, width, height])

def roof(surface, color, points):
    pygame.draw.polygon(surface, color, points)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sun_x += sun_speed_x
    sun_y = a * (sun_x - h) ** 2 + k

    if sun_x - sun_radius > SCREEN_WIDTH + 10:
        sun_x = -sun_radius - 10

    clock.tick(FPS)
    screen.fill(BLACK)

    sun_rect = pygame.Rect(0, 0, sun_radius * 2, sun_radius * 2)
    sun_rect.center = (int(sun_x), int(sun_y))
    pygame.draw.ellipse(screen, YELLOW, sun_rect)

    house_x = SCREEN_WIDTH // 2 - 50
    house_y = SCREEN_HEIGHT - 100
    house_width = 100
    house_height = 150
    house(screen, house_x, house_y, house_width, house_height, WHITE)
    roof_points = [
        (house_x - 10, house_y),
        (house_x + house_width // 2, house_y - 80),
        (house_x + house_width + 10, house_y)
    ]
    roof(screen, RED, roof_points)

    pygame.display.update()

pygame.quit()
