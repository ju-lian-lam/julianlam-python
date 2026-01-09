import pygame
import random
import sys
import math

WIDTH, HEIGHT = 400, 600
FPS = 60
PIPE_GAP = 150
PIPE_FREQUENCY = 1500

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.radius = 15
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8

    def jump(self):
        self.velocity = self.jump_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, int(self.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - 15, int(self.y - 15), 30, 30)
    

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.width = 60
        self.top_height = random.randint(100, 350)
        self.bottom_y = self.top_height + PIPE_GAP
        self.speed = 3
        self.passed = False

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.bottom_y, self.width, HEIGHT - self.bottom_y))

    def collide(self, bird):
        bird_rect = bird.get_rect()
        top_pipe = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_pipe = pygame.Rect(self.x, self.bottom_y, self.width, HEIGHT - self.bottom_y)
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.running = True

        pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)

    def reset(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        pygame.time.delay(400)

    def draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_surface = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

                if event.type == pygame.USEREVENT:
                    self.pipes.append(Pipe())

            self.bird.update()

            for pipe in self.pipes:
                pipe.update()

                if pipe.collide(self.bird):
                    self.reset()

                if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                    pipe.passed = True
                    self.score += 1

            self.pipes = [p for p in self.pipes if p.x > -p.width]

            if self.bird.y > HEIGHT or self.bird.y < 0:
                self.reset()

            self.screen.fill((0, 150, 255))
            self.bird.draw(self.screen)

            for pipe in self.pipes:
                pipe.draw(self.screen)

            self.draw_score()
            pygame.display.update()

if __name__ == "__main__":
    Game().run()
