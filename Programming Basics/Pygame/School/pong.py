import pygame

pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (0xFF, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700

font_name = pygame.font.match_font('Helvetica')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) #anti-alias True grey and white pixels
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

class Paddle:
    colour = WHITE
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__speed = 0
        self.score = 0
    #end constructor

    def move(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
                if event.key == pygame.K_w:
                    self.__speed = -5
                elif event.key == pygame.K_s:
                    self.__speed = 5
                #end if
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.__speed = 0
                #end if
            #end if
        #next event
        self.__y += self.__speed
        if self.__y < 0:
            self.__y = 0
        if self.__y > 460:
            self.__y = 460
    #end procedure

    def draw(self,screen)->None:
        pygame.draw.rect(screen, self.colour,
                         [self.__x, self.__y, 10, 60], 
                         0)
    #end procedure

class Paddle2(Paddle):
    def __init__(self,x,y):
        #super().__init__(x,y)
        self.colour = RED
        self.__x = x
        self.__y = y
        self.__speed = 0
        self.score = 0
    #end constructor   

    def move(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
                if event.key == pygame.K_UP:
                    self.__speed = -5
                elif event.key == pygame.K_DOWN:
                    self.__speed = 5
                #end if
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.__speed = 0
                #end if
            #end if
        #next event
        self.__y += self.__speed
        if self.__y < 0:
            self.__y = 0
        if self.__y > 460:
            self.__y = 460
    #end procedure

    def draw(self,screen)->None:
        pygame.draw.rect(screen, self.colour,
                         [self.__x, self.__y, 10, 60], 
                         0)
    #end procedure


# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong 1")

# Loop until the user clicks the close button.
gameOver = False
paddleA = Paddle(10,240)
paddleB = Paddle2(680,240)
ball = pygame.Rect(350,250,25,25)
ball_xspeed = 4
ball_yspeed = 0


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here

    paddleA.move(events)
    paddleB.move(events)

    ball.x = ball.x + ball_xspeed
    ball.y = ball.y + ball_yspeed

    # bouncing on top and bottom
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_yspeed = ball_yspeed * -1

    # bouncing on edges and scoring
    if ball.left <= 0:
        paddleB.score = paddleB.score + 1
        #ball.x = SCREEN_WIDTH / 2
        #ball.y = SCREEN_HEIGHT / 2
        ball_yspeed = 0
        ball_xspeed = ball_xspeed * -1

    if ball.right >= SCREEN_WIDTH:
        paddleA.score = paddleA.score + 1
        #ball.x = SCREEN_WIDTH / 2
        #ball.y = SCREEN_HEIGHT / 2
        ball_yspeed = 0
        ball_xspeed = ball_xspeed * -1

    # bouncing off paddles
    if ball.x <= paddleA._Paddle__x + 10 and ball.y >= paddleA._Paddle__y and ball.y <= paddleA._Paddle__y + 60:
        ball_xspeed = ball_xspeed * -1
        ball_yspeed = (ball.y - (paddleA._Paddle__y + 20)) // 5

    if ball.x + 30 >= paddleB._Paddle2__x and ball.y >= paddleB._Paddle2__y and ball.y <= paddleB._Paddle2__y + 60:
        ball_xspeed = ball_xspeed * -1
        ball_yspeed = (ball.y - (paddleB._Paddle2__y + 20)) // 5
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    paddleA.draw(screen)
    paddleB.draw(screen)
    pygame.draw.ellipse(screen, GREEN, ball)
    draw_text(screen, "playerA: " + str(paddleA.score), 18, SCREEN_WIDTH // 4, 10)
    draw_text(screen, "playerB: " + str(paddleB.score), 18, SCREEN_WIDTH * 3 // 4, 10)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()