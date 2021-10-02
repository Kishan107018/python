import pygame,sys
from pygame.locals import *

catx=10
caty=10
screen=0
 #This function is used for exit
def myquit():
    pygame.quit()
    sys.exit()

def check_input(events):
    global catx,caty,screen
    
    for event in events:
        if (event.type==QUIT):
            quit()
        else:
            if (event.type==KEYDOWN):
                if(event.key ==K_ESCAPE):
                    myquit()
                elif(event.key==K_LEFT):
                    catx-=15
                    print("Move Rect left")
                elif(event.key==K_UP):
                    caty+=15
                    print("Move rect Up")
                elif(event.key==K_DOWN):
                    caty-=15
                    print("Move rect Down")
                elif(event.key==K_RIGHT):
                    catx+=15
                    print("Move Rect Right")
                else:
                    print(event.key)
    
    screen.fill((255,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
  #  pygame.draw.rect(screen,(255,255,255),(caty,50,50,10))
    pygame.display.update()
    



def main():
    global screen
    #Initialize the pygame

    pygame.init()

    #Set the window
    window=pygame.display.set_mode((600,500))

    #set the screen
    screen=pygame.display.get_surface()

    #title of screen
    pygame.display.set_caption("The Snake Game")
    
    pygame.display.update()

    while True:
        check_input(pygame.event.get())

main()
    
