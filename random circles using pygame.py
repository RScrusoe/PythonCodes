import pygame
import random
import time
pygame.init()

white = (255,255,255)
width = 800
height = 600

running = 1
gameDisplay = pygame.display.set_mode((width,height))
gameDisplay.fill(white)
r = int(35*random.random())
x = int(width*random.random())
y = int(height*random.random())
def randomColor():
    return (255*random.random(),255*random.random(),255*random.random())
pygame.draw.circle(gameDisplay, randomColor(), (x,y), r)
l=[[x,y,r]]
ct=0
r = int(50*random.random())
while 1:
    
    flag = 1
    x = int(width*random.random())
    y = int(height*random.random())
    for i in l:

        d = ( (x-i[0])**2 + (y-i[1])**2 )**0.5
        if d < r+i[2]:
            
            flag = 0
            break
            #print(x,y,r, i, d,'   ',r+i[2])
            
            break
    if flag:
        pygame.draw.circle(gameDisplay, randomColor(), (x,y), r)
        pygame.display.update()
        ct+=1
        print(ct)
        time.sleep(0.1)
        l.append([x,y,r])
        
        r = int(50*random.random())
    
#print(l)




try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()
except SystemExit:
    pygame.quit()