import pygame
from pygame.locals import *
#intialization of modules
pygame.init()
#setting screen size for the game
screen=pygame.display.set_mode((700,500))
#(width,height)
pygame.display.set_caption("Doremon Jump")
#font
font=pygame.font.Font("freesansbold.ttf",20)
#color
white = (135,206,235)
black=(0,0,0)
doremon=pygame.image.load("obj1.png")
doremon=pygame.transform.scale(doremon,(85,98))
doremon2=pygame.image.load("obj2.png")
doremon2=pygame.transform.scale(doremon2,(85,98))
doremon3=pygame.image.load("obj3.png")
doremon3=pygame.transform.scale(doremon3,(85,98))
doremon4=pygame.image.load("obj4.png")
doremon4=pygame.transform.scale(doremon4,(85,98))
doremon5=pygame.image.load("obj5.png")
doremon5=pygame.transform.scale(doremon5,(85,98))
doremon6=pygame.image.load("obj6.png")
doremon6=pygame.transform.scale(doremon6,(85,98))
walk=[doremon,doremon,doremon,doremon,doremon2,doremon2,doremon2,doremon2,doremon3,doremon3,doremon3,doremon3,doremon3,doremon3,doremon3,doremon4,doremon4,doremon4,doremon5,doremon5,doremon5,doremon5,doremon6,doremon6,doremon6,doremon6]
background=pygame.image.load("background.png")
wall1=pygame.image.load("wall1.png")
wall1=pygame.transform.scale(wall1,(50,130))
wall2=pygame.image.load("wall2.png")
wall2=pygame.transform.scale(wall2,(75,130))
wall3=pygame.image.load("wall3.png")
wall3=pygame.transform.scale(wall3,(100,130))
def gameLoop():
    backx=0
    backy=0
    backvelocity= 0
    wallx=200
    wally=395
    doremonx=50
    doremony=395
    walkpoint=0
    jump=False
    score=0
    gravity=7
    game=False
    gameover=False
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    if doremony== 395:
                        jump=True
                        backvelocity =6
                        game=True
                if event.key==K_SPACE:
                    gameLoop()
        if backx < -700:
            backx = 0 
        if wallx < -1600:
            wallx=750
    #when jump
        if 396>doremony>200:
            if jump==True:
                doremony-=7
        else:
                jump=False    
        if doremony<395:
            if jump==False:
                doremony+=gravity  
    #colllision
        if wallx<doremonx+100<wallx+70 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0
            game=False
            gameover=True
        if wallx+400<doremonx+100<wallx+470 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if wallx+800<doremonx+100<wallx+870 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if wallx+1200<doremonx+100<wallx+1270 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if game==True:
            score+=1
         
        text=font.render("Score: "+str(score),True,black)  
        end_text=font.render("Game Over. Press space to continue",True,black)
        screen.fill(white)
        screen.blit(text,[300,10])
    
        screen.blit(background,[backx,backy])
        screen.blit(background,[backx + 700,backy])
        if gameover==True:
            screen.blit(end_text,[200,250])
        screen.blit(walk[walkpoint],[doremonx,doremony])
        
        backx-=backvelocity
        wallx-=backvelocity
        if game==True:
            walkpoint+=1
        if walkpoint>24:
            walkpoint=0
    
        screen.blit(wall2,[wallx,wally])
        screen.blit(wall1,[wallx+400,wally])
        screen.blit(wall3,[wallx+800,wally])
        screen.blit(wall2,[wallx+1200,wally])
        pygame.display.update()
gameLoop()       