#############################################
# Universidad Tecnica Particular de Loja    #
#############################################
# Professor:                                #
# Rodrigo Barba        lrbarba@utpl.edu.ec  #
#############################################
# Students:                                 #
# Jonathan Torres      jptorres6@utpl.edu.ec#
#############################################
#librarys
import sys
import pygame
import random
from pygame.locals import *
import cv2
import numpy as np
#-----------------------------------------------------------------------------------------------------------------

# Select menu color
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)

pygame.init() # Start imagen
fuente1= pygame.font.SysFont("Arial", 25, True, False)
# Screen dimension 500,400
pantalla=pygame.display.set_mode((500,400))    
pygame.display.set_caption("Elije el color") # Title of the window
#ceate a clock to control fps
reloj1=pygame.time.Clock()
info0=fuente1.render("Elija el color para jugar ...",0,(0,0,0)) # Present the text selec color
# load images
verde1=pygame.image.load('images\Verde.png')
verde2=pygame.image.load("images\Verde1.png")
amarillo1=pygame.image.load("images\Amarillo.png")
amarillo2=pygame.image.load("images\Amarillo1.png")
rojo1=pygame.image.load("images\Rojo.png")
rojo2=pygame.image.load("images\Rojo1.png")      
boton1=Boton(verde1,verde2,200,100)
boton2=Boton(amarillo1,amarillo2,200,200)
boton4=Boton(rojo1,rojo2,200,300)
boton3=Boton(info0,info0,90,30)
cursor1=Cursor()
    
blanco=(255,255,255) # color of screen white
colordefondo=blanco
   
salir=False
#LOOP PRINCIPAL
while salir!=True:
    #all events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                #Put the range with color green
                color_bajos = np.array([49,50,50], dtype=np.uint8)
                color_altos = np.array([100, 255, 210], dtype=np.uint8)
                salir=True
            if cursor1.colliderect(boton2.rect):
                #Put the range with color yellow
                color_bajos = np.array([16,76,72], dtype=np.uint8)
                color_altos = np.array([30, 255, 210], dtype=np.uint8)
                salir=True
            if cursor1.colliderect(boton4.rect):
                #Put the range with color red 
                color_bajos = np.array([160,100,100], dtype=np.uint8)
                color_altos = np.array([179,255,255], dtype=np.uint8)
                salir=True

            if cursor1.colliderect(boton3.rect):
                salir=True
            
        # pygame.QUIT( cruz de la ventana)
        if event.type == pygame.QUIT:
            salir=True
        
    reloj1.tick(20)#20fps
    pantalla.fill(colordefondo) # white        
    cursor1.update()
    boton1.update(pantalla,cursor1)
    boton2.update(pantalla, cursor1)
    boton4.update(pantalla, cursor1)
    boton3.update(pantalla, cursor1)
        
    pygame.display.update() #display
        
pygame.quit()

pygame.init()

font = pygame.font.Font(None, 24)
pacman_img = pygame.image.load('images\pacman.jpg')
ghost_img = pygame.image.load('images\ghost.jpg')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((340, 400))

#Track pacman game state.
class Game:
    #Initialize game.
    def __init__(self):
        self.tiles_width = 17
        self.levels = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0,
             0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0,
             0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0,
             0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0,
             0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0,
             0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0,
             0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.reset()
    #Reset game to initial game state.
    def reset(self):
        self.running = True
        self.score = 0
        self.level = 0
        self.next_dir = 0
        self.pacman = [pygame.Rect(160, 260, 20, 20), 0]
        self.ghosts = [[pygame.Rect(20, 20, 20, 20), 0],
                       [pygame.Rect(300, 20, 20, 20), 2],
                       [pygame.Rect(20, 340, 20, 20), 0],
                       [pygame.Rect(300, 340, 20, 20), 2]]

    #Advance rectangle by given direction.
    def next_pos(self, next_dir, rect):
        if next_dir == 0: chng = (4, 0)
        if next_dir == 1: chng = (0, -4)
        if next_dir == 2: chng = (-4, 0)
        if next_dir == 3: chng = (0, 4)
        return rect.move(*chng)

    #Calculate tile index by rectangle.
    def rect_idx(self, rect):
        return (rect.top / 20) * self.tiles_width + (rect.left / 20)

    #Return True iff character rectangle is valid on tiles.
    def valid_pos(self, rect):
        
        prev_tile = self.levels[self.level][self.rect_idx(rect)]
        next_tile = self.levels[self.level][self.rect_idx(rect.move(19, 19))]
        on_track = rect.left % 20 == 0 or rect.top % 20 == 0
        return prev_tile != 0 and next_tile != 0 and on_track
    #Move character rectangle. Returns next character location and direction.
    def move_rect(self, next_dir, curr_dir, rect):
        next_rect = self.next_pos(next_dir, rect)
        if self.valid_pos(next_rect):
            return (next_rect, next_dir)
        else:
            next_rect = self.next_pos(curr_dir, rect)
            if self.valid_pos(next_rect):
                return (next_rect, curr_dir)
        return (rect, curr_dir)
    #Move pacman character.
    def move_pacman(self):
        rect, curr_dir = self.pacman
        tup = self.move_rect(self.next_dir, curr_dir, rect)
        self.pacman[0], self.pacman[1] = tup
    #Move ghost characters.
    def move_ghosts(self):
        def dist_pacman(rect):
            return ((rect.top - self.pacman[0].top) ** 2
                    + (rect.left - self.pacman[0].left) ** 2) ** 0.5

        def test_dir(new_dir, curr_dir, rect):
            next_tup = self.move_rect(new_dir, curr_dir, rect)
            return dist_pacman(next_tup[0])

        for tup in self.ghosts:
            rect = tup[0]
            curr_dir = next_dir = tup[1]
            if rect.top % 20 == 0 and rect.left % 20 == 0:

                # Uncomment for Ghost AI
                dist = [(test_dir(val, curr_dir, rect), val)
            for val in (0, 1, 2, 3)]
                min_dist = min(dist)
                next_dir = min_dist[1]

                next_dir = (curr_dir + random.choice((1, 3))) % 4

            tup[0], tup[1] = self.move_rect(next_dir, curr_dir, rect)
    #Update tiles, score and running based on pacman location.
    def update(self):
        self.next_dir = self.pacman[1]

        idx = self.rect_idx(self.pacman[0])
        if self.levels[self.level][idx] == 2:
            self.score += 1
            self.levels[self.level][idx] = 1

        has_food = any(val == 2 for val in self.levels[self.level])
        ghost_rects = [tup[0] for tup in self.ghosts]
        is_eaten = self.pacman[0].collidelist(ghost_rects) >= 0
        self.running = has_food and not is_eaten

    #Draw game on screen
    def draw(self):
        # Draw tiles

        for idx, val in enumerate(self.levels[self.level]):
            left = (idx % self.tiles_width) * 20
            top = (idx / self.tiles_width) * 20
            if val == 0:
                # Draws a blue square.
                color = (0, 0, 128)
                pygame.draw.rect(screen, color, (left, top, 20, 20))
            else:
                # Draw a black square.
                color = (0, 0, 0)
                pygame.draw.rect(screen, color, (left, top, 20, 20))
            if val == 2:
                # Draw a white dot.
                color = (255, 255, 255)
                pygame.draw.circle(screen, color, (left + 10, top + 10), 2)

        # Draw pacman.

        pacman_dir = pygame.transform.rotate(pacman_img, 90 * self.pacman[1])
        screen.blit(pacman_dir, self.pacman[0])

        # Draw ghosts.

        for val in self.ghosts:
            screen.blit(ghost_img, val[0])

        # Draw score.

        pygame.draw.rect(screen, (0, 0, 0), (0, 380, 100, 20))
        msg = 'Score: ' + str(self.score)
        text = font.render(msg , True, (255, 255, 255))
        screen.blit(text, (5, 382))

#Create a imagen with the size of the video
def img(img1,img2,xpos,ypos):
    rows2,cols2,channels2 = img2.shape
    rows1,cols1,channels1 = img1.shape
    print (str(rows2)+'x'+str(rows1))
    aux = np.zeros((rows2, cols2, 3), dtype = "uint8")
    for i in range(rows1):
        for j in range(cols1):
            aux[xpos+i,ypos+j]=img1[i,j]
    return aux
#Start the game
game = Game()
#Select camera
captura = cv2.VideoCapture(0)
#Load all images
arriba=cv2.imread("images\up2.png") 
abajo=cv2.imread("images\down2.png")
izquierda=cv2.imread("images\left2.png")
derecha=cv2.imread("images\Right2.png")
salir=cv2.imread("images\salir2.jpg")
reini=cv2.imread("images\Reiniciar2.png")
#all variables  
bdx=15;
bdy=150;
base=150;
altura=150;
radio=20;
c_punt=[0,0,0]
l_p=10;
#capture the video
_, imagen1 = captura.read()
#Ceate a mask with the directions, exit and restar
up=img(arriba,imagen1,bdx-150+base,bdy-50+base)
down=img(abajo,imagen1,bdx+150+base,bdy-50+base)
left=img(izquierda,imagen1,bdx+base,bdy-200+altura)
right=img(derecha,imagen1,bdx+base,bdy+100+altura)
exit=img(salir,imagen1,bdx-150+base,bdy+225+altura)
reiniciar=img(reini,imagen1,bdx+base+200,bdy-300+altura)
dire=cv2.add(up,down)
dire=cv2.add(dire,left)
dire=cv2.add(dire,right)
dire=cv2.add(dire,exit)
dire=cv2.add(dire,reiniciar)
while True:

    #Captue video and convert RGB -> HSV
    _, imagen1 = captura.read()
    imagen1 = cv2.flip(imagen1,1)
    imagen = cv2.add(imagen1,dire)    

    cv2.rectangle(imagen, (bdy+100+altura,bdx-150+base), (bdy-50+altura,bdx+base),(255,0,0), 2) #up  150x150 pxls
    cv2.rectangle(imagen, (bdy+100+altura,bdx+150+base ), (bdy-50+altura,bdx+300+base),(255,0,0), 2) #dowm 150x150 pxls
    cv2.rectangle(imagen, (bdy-50+altura,bdx+base), (bdy-200+altura,bdx+150+base),(255,0,0), 2) #left 150x150 pxls
    cv2.rectangle(imagen, (bdy+250+altura,bdx+base), (bdy+100+altura,bdx+150+base),(255,0,0), 2) #rigth 150x150 pxls
    cv2.rectangle(imagen, (bdy+325+altura,bdx-150+base), (bdy+225+altura,bdx-50+base),(0,0,255), 2) #exit 100x100 pxls
    cv2.rectangle(imagen, (bdy-300+altura,bdx+base+200 ), (bdy-200+altura,bdx+base+300),(255,0,0), 2) #Restar  100x100 pxls
    hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
    #Create a mask with the range of color that ou select
    mask = cv2.inRange(hsv, color_bajos, color_altos)
    #Filter all noise
    kernel = np.ones((6,6),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #Difuminate the mask
    blur = cv2.bilateralFilter(mask,9,75,75)
    edges = cv2.Canny(mask,1,2)
    #Found the center
    moments = cv2.moments(mask)
    area = moments['m00']
    event = pygame.event.poll()

    #Serch area
    if(area > 200000):      
        #Found the cente
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00']) 
        #Draw center of object
        cv2.circle(imagen,(x,y), radio, (c_punt), 5) 
        cv2.line(imagen,(x,y+radio-l_p),(x,y+radio+l_p),(c_punt),5)
        cv2.line(imagen,(x,y-radio-l_p),(x,y-radio+l_p),(c_punt),5)
        cv2.line(imagen,(x+radio-l_p,y),(x+radio+l_p,y),(c_punt),5)
        cv2.line(imagen,(x-radio-l_p,y),(x-radio+l_p,y),(c_punt),5)
        #Put in the imagen the action
        if(y>=(bdx-150+base) and y<=(bdx+base) and x>=(bdy-50+altura) and x<=(bdy+100+altura)):
            cv2.putText(imagen,"sube", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            game.next_dir = 1
        elif(y>=(bdx+150+base) and y<=(bdx+300+base) and x>=(bdy-50+altura) and x<=(bdy+100+altura)):
            cv2.putText(imagen,"baja", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            game.next_dir = 3
        elif(y>(bdx+base) and y<(bdx+base+150) and x>(bdy-200+altura) and x<(bdy-50+altura)):
            cv2.putText(imagen,"izquierda", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            game.next_dir = 2
        elif(y>(bdx+base) and y<(bdx+base+150) and x>(bdy+100+altura) and x<(bdy+250+altura)):
            cv2.putText(imagen,"derecha", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            game.next_dir = 0
        elif(y>(bdx+base+200) and y<(bdx+base+300) and x>(bdy-300+altura) and x<(bdy-200+altura)):
            cv2.putText(imagen,"Reiniciar", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            game.reset()
        elif(y>(bdx-150+base) and y<(bdx-50+base) and x>(bdy+225+altura) and x<(bdy+325+altura)):
            cv2.putText(imagen,"SALIR", (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, 0,0,0)
            pygame.event.post(pygame.event.Event(QUIT))
            break
    #Show the video
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    #Action
    if game.running:
        game.move_pacman()
        game.move_ghosts()
        game.update()
    game.draw()
    # Display next frame.
    pygame.display.flip()
    clock.tick(12)
cv2.destroyAllWindows()
