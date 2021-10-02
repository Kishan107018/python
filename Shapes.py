import pygame
from pygame.locals import *

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

window=pygame.display.set_mode((600,400))
screen=pygame.display.get_surface()


pygame.draw.rect(screen,red,(20,30,50,100)) #(20,30,50,100) first 20 and 30 value is use to fix the cordinate and 50 position value is for length of line and last 100 position is represent the width

pygame.draw.line(screen,green,(0,0),(400,100))#first (0,0) shows line starting cordinate and second(400,100) shows line ending cordinate

pygame.draw.polygon(screen,blue,((146,0),(291,106),(236,100)))# Three conrdinate of polygon it can be more than 3

pygame.draw.circle(screen,white,(300,20),50)#(300,20) which shows the cordinate and 50 shows the radius

pygame.draw.ellipse(screen,white,(20,300,10,50),1)#First and second value represent the (x,y)cordinate or center of circle and third position value is for width and fourth is for the height of the ellipse.

pygame.display.update()


pixel=pygame.PixelArray(screen)
pixel[380][280]=black
