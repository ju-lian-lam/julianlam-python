import pygame, random

# Use a class to create a record structure
class Snowflake:
    colour = 0xFFFF00
    def __init__(self,x,y,speed,size)->None: #new
        #These are the fields or attributes
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__size = size
    #end constructor

    def fall(self):
        if self.__y > 500:
            self.__y = 0
            self.__x = random.randint(1,699)
        else:
            self.__y += self.__speed
        #end if
    #end procedure

    def draw(self,screen)->None:
        pygame.draw.rect(screen, Snowflake.colour,
                         [self.__x, self.__y, self.__size, self.__size], 
                         0)
    #end procedure

    def __str__(self)->str:
        return_str = f'Snowflake: x={self.__x}, y={self.__y}, speed={self.__speed}, size={self.__size}'
    def __repr__(self)->str:
        return f'Snowflake({self.__x},{self.__y},{self.__speed},{self.__size})'
    
    def setSpeed(self):
        self.__speed = 10
    # end procedure

    def getSpeed(self):
        return self.__speed
    # end function

    def setSize(self,size):
        self.__size = size
    # end procedure

    def getSize(self):
        return self.__size
    # end function

#end class


class Snowball(Snowflake):
    colour = 0xFFFFFF
    def __init__(self,x,y,speed,size,time)->None: #new
        super().__init__(x,y,speed,size)
        self.__time = time
        self.__counter = 0 
        Snowball.colour = 0xFFFFFF
    #end constructor

    def fall(self):
        super().fall()
        self.__counter = self.__counter + 1
        if self.__counter == self.__time * 60:
            self.setSize(self.getSize() + 3)
            self.__counter = 0
        # end if
    #end procedure
#end class


# Define some colors
BLACK = (0,0,0)
WHITE = (0xFF, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snowdrop OOP 1")

# Loop until the user clicks the close button.
gameOver = False
flakes = []
for _ in range(50):
    flakes.append(Snowflake(random.randint(1,490),random.randint(1,690),2,10))
#next _
balls = []
for _ in range(20):
    balls.append(Snowball(random.randint(1,490),random.randint(1,690),5,15,2))

first = flakes[0]
first.colour = 0x0000FF
first.setSpeed()
print(first.getSpeed())
print(first.colour)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    #set x and y coordinates

    for flake in flakes:
        flake.fall()
    #next flake

    for ball in balls:
        ball.fall()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for flake in flakes:
        flake.draw(screen)
    #next flake

    for ball in balls:
        ball.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()