import pygame
import random
import time
pygame.init()

white = (255,255,255)

running = 1
gameDisplay = pygame.display.set_mode((1300,700))
gameDisplay.fill(white)
r = int(35*random.random())
x = int(1300*random.random())
y = int(700*random.random())
def randomColor():
    return (255*random.random(),255*random.random(),255*random.random())
pygame.draw.circle(gameDisplay, randomColor(), (x,y), r)
l=[[x,y,r]]
ct=75
r = int(50*random.random())
while ct>0:
    flag = 1
    x = int(1300*random.random())
    y = int(700*random.random())
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
        time.sleep(0.1)
        l.append([x,y,r])
        ct-=1
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