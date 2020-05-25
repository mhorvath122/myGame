import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('.\\Game\\R1.png'), pygame.image.load('.\\Game\\R2.png'), pygame.image.load('.\\Game\\R3.png'), pygame.image.load('.\\Game\\R4.png'), pygame.image.load('.\\Game\\R5.png'), pygame.image.load('.\\Game\\R6.png'), pygame.image.load('.\\Game\\R7.png'), pygame.image.load('.\\Game\\R8.png'), pygame.image.load('.\\Game\\R9.png')]
walkLeft = [pygame.image.load('.\\Game\\L1.png'), pygame.image.load('.\\Game\\L2.png'), pygame.image.load('.\\Game\\L3.png'), pygame.image.load('.\\Game\\L4.png'), pygame.image.load('.\\Game\\L5.png'), pygame.image.load('.\\Game\\L6.png'), pygame.image.load('.\\Game\\L7.png'), pygame.image.load('.\\Game\\L8.png'), pygame.image.load('.\\Game\\L9.png')]
bg = pygame.image.load('.\\Game\\bg.jpg')
char = pygame.image.load('.\\Game\\standing.png')

walkRight1 = [pygame.image.load('.\\Game\\R1_2.png'), pygame.image.load('.\\Game\\R2_2.png'), pygame.image.load('.\\Game\\R3_2.png'), pygame.image.load('.\\Game\\R4_2.png'), pygame.image.load('.\\Game\\R5_2.png'), pygame.image.load('.\\Game\\R6_2.png'), pygame.image.load('.\\Game\\R7_2.png'), pygame.image.load('.\\Game\\R8_2.png'), pygame.image.load('.\\Game\\R9_2.png')]
walkLeft1 = [pygame.image.load('.\\Game\\L1_2.png'), pygame.image.load('.\\Game\\L2_2.png'), pygame.image.load('.\\Game\\L3_2.png'), pygame.image.load('.\\Game\\L4_2.png'), pygame.image.load('.\\Game\\L5_2.png'), pygame.image.load('.\\Game\\L6_2.png'), pygame.image.load('.\\Game\\L7_2.png'), pygame.image.load('.\\Game\\L8_2.png'), pygame.image.load('.\\Game\\L9_2.png')]
char1 = pygame.image.load('.\\Game\\standing_2.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height, walkRight, walkLeft, char):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.char = char
        
    def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
                
            if self.left: 
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.char, (self.x,self.y))


def redrawGameWindow():
    win.blit(bg, (0,0)) 
    player1.draw(win)
    
    player2.draw(win)   
    
    pygame.display.update()

#mainloop
player1 = player(10, 400, 64, 64, walkRight, walkLeft, char)
player2 = player(450, 400, 64, 64, walkRight1, walkLeft1, char1)
run = True
while run:
    clock.tick(27)
     
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
     
    keys = pygame.key.get_pressed()
    
    #Character 1
    if keys[pygame.K_LEFT] and player1.x > 0:
        player1.x -= player1.vel 
        player1.left = True
        player1.right = False
    elif keys[pygame.K_RIGHT] and player1.x < (500 - player1.width):
        player1.x += player1.vel
        player1.right = True
        player1.left = False
    else:
        player1.right = False
        player1.left = False
        player1.walkCount = 0
    if not (player1.isJump):
       if keys[pygame.K_RETURN]:
            player1.isJump = True
            player1.right = False
            player1.left = False
            player1.walkCount = 0
    else:
        if player1.jumpCount >= -10:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1
        else: 
            player1.isJump = False
            player1.jumpCount = 10
        
        
     #Character 2   
    if keys[pygame.K_a] and player2.x > 0:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False   
    elif keys[pygame.K_d] and player2.x < (500 - player2.width):
        player2.x += player2.vel
        player2.right = True
        player2.left = False
    else:
        player2.right = False
        player2.left = False  
        player2.walkCount = 0
    if not (player2.isJump):    
        if keys[pygame.K_SPACE]:
            player2.isJump = True
            player2.right = False
            player2.left = False  
            player2.walkCount = 0
    else:
        if player2.jumpCount >= -10:
            neg1 = 1
            if player2.jumpCount < 0:
                neg1 = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg1
            player2.jumpCount -= 1
        else: 
            player2.isJump = False
            player2.jumpCount = 10
        
    redrawGameWindow()    
        
    
  
  
            
pygame.quit()