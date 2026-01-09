import pygame, random
from os import path

WIDTH = 480
HEIGHT = 600
FPS = 60 # high speed

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = (WHITE, RED, BRIGHT_RED, GREEN, BRIGHT_GREEN, BLUE, YELLOW)
image_dir = path.join(path.dirname(__file__),"images")

font_name = pygame.font.match_font('Helvetica')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) #anti-alias True grey and white pixels
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

# initialise pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #display surface
pygame.display.set_caption("Space Invaders!")
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite): #Pygame sprite object
    
    def __init__(self): #public procedure new() CONSTRUCTOR 
    #constructor is the initialiser method that sets up the object’s starting state for all its attributes
        pygame.sprite.Sprite.__init__(self) #call built in Sprite function
        
        #instance variables
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(player_img,(51,51))
        self.rect = self.image.get_rect() #define the rectangle bounding box
        self.rect.centerx = WIDTH / 2 #???????
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.lives = 3

    #update method
    def update(self): #what should happen each time the animation update loop happens 
        self.speedx = 0 #start stationary

        keystate = pygame.key.get_pressed() # check keystate
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x = self.rect.x + self.speedx

        #####???????????
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    #shoot method
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(mob_img,(66,48))
        #self.image.fill(mob_color)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 1
        self.speedx = 1

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.x >= WIDTH - self.rect.width:
           self.speedx = -1
        if self.rect.x <= 0:
            self.speedx = 1

        #####?????????
        if self.rect.top > HEIGHT + 10 or \
            self.rect.left < -25 or \
              self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            #self.speedy = random.randrange(1, 8)

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(ship_img,(51,51))
        #self.image.fill(mob_color)
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 100
        self.speedx = 5

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        if self.rect.x >= WIDTH - self.rect.width:
           self.speedx = -5
        if self.rect.x <= 0:
            self.speedx = 5

        #####?????????
        if self.rect.top > HEIGHT + 10 or \
            self.rect.left < -25 or \
              self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            #self.speedy = random.randrange(1, 8)

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(rocket_img,(30,30))
        #self.image.fill(mob_color)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 5

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.y > HEIGHT:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)

        #####?????????
        if self.rect.top > HEIGHT + 10 or \
            self.rect.left < -25 or \
              self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            #self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx =  x
        self.speedy = -10
    
    def update(self):
        self.rect.y = self.rect.y + self.speedy

        if self.rect.bottom <0:
            self.kill()
mob_img = pygame.image.load(path.join(image_dir,"greenalien.png")).convert_alpha()
ship_img = pygame.image.load(path.join(image_dir,"ship.png")).convert_alpha()
player_img = pygame.image.load(path.join(image_dir,"player.png")).convert_alpha()
rocket_img = pygame.image.load(path.join(image_dir,"rocket.png")).convert_alpha()
#Groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
shipmobs = pygame.sprite.Group()
rockets = pygame.sprite.Group()

player = Player() #Create instance of an object, player = new Player()
ship = Ship()
rocket = Rocket()
shipmobs.add(ship)
rockets.add(rocket)
all_sprites.add(player)
all_sprites.add(ship)
all_sprites.add(rocket)
for count in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
for count in range(2):
    r = Rocket()
    all_sprites.add(r)
    mobs.add(r)
score = 0
# Game loop 
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input i.e. EVENTS
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # check to see if bullet his mob?
    # kill the mob and kill the bullet
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob() #
        all_sprites.add(m)
        mobs.add(m)
        score = score + 1

    hits = pygame.sprite.groupcollide(shipmobs, bullets, True, True)
    for hit in hits:
        ship = Ship()
        all_sprites.add(ship)
        shipmobs.add(ship)
        score = score + 5


    # check to see if a mob hits the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.lives = player.lives - 1
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    if player.lives == 0:
        player.kill()
    if not player.alive():
        running = False

    hits = pygame.sprite.spritecollide(player, rockets, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.lives = player.lives - 1
        r = Rocket()
        all_sprites.add(r)
        mobs.add(r)
    if player.lives == 0:
        player.kill()
    if not player.alive():
        running = False
        
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen,"score: " + str(score),18,40,5)
    draw_text(screen,"lives: " + str(player.lives),18,WIDTH-40,5)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()