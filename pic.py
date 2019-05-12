import pygame, sys, random, math
SCREEN_W, SCREEN_H = 1024, 768

class CLS_pic(object):
    def __init__(self,fileName):
        img = pygame.image.load(fileName)
        self.img = pygame.transform.scale(img,(SCREEN_W,SCREEN_H))
        self.x,self.y = 0,0
        self.w,self.h = self.img.get_size()
    def draw(self,scr, effNum =0, spd = 5):
        if effNum == 0 or spd == 0:
            scr.blit(self.img,(0,0))
        elif effNum == 1:
            for x in range(-SCREEN_W,0,spd):
                scr.blit(self.img,(x,0))
                pygame.display.update()
        elif effNum == 2:
            for y in range(-SCREEN_W,0,spd):
                scr.blit(self.img,(0,y))
                pygame.display.update()
        elif effNum == 3:
            for x in range(-SCREEN_W,0,spd*10):
                for y in range(-SCREEN_H,0,spd):
                    scr.blit(self.img,(x,y))
                    pygame.display.update()
        elif effNum == 4:
            for i in range(1,100,spd):
                scr.blit(self.img,(SCREEN_W/i,SCREEN_H/i))
                pygame.display.update()
        elif effNum == 5:
            for y in range(-SCREEN_H*4,0,spd):
                scr.blit(self.img,(0,SCREEN_H%y))
                pygame.display.update()     
        elif effNum == 6:
            for w in range(1,SCREEN_W,spd):
                h = int(w*SCREEN_H/SCREEN_W)
                img = pygame.transform.scale(self.img,(w,h))
                x = (SCREEN_W-w)/2
                y = (SCREEN_H-h)/2
                scr.blit(img,(x,y))
                pygame.display.update()
        elif effNum == 7:
            w,h= spd*8,int(SCREEN_H/SCREEN_W*spd*8)
            xNum,yNum = SCREEN_W//w,SCREEN_H//h
            mList = []
            for i in range(xNum*yNum): 
                mList.append(i)
            for i in range(xNum*yNum):
                num = random.choice(mList)
                mList.remove(num)
                x = num%yNum*w
                y = num//yNum*h
                scr.blit(self.img,(x,y),area=(x,y,w,h))
                pygame.display.update()
        elif effNum == 10:
            oldImg = scr.copy()
            for x in range(-SCREEN_W,0,spd):
                scr.blit(self.img,(x,0))
                scr.blit(oldImg,(x+SCREEN_W,0))
                pygame.display.update()

        elif effNum == 11:
            oldImg = scr.copy()
            for x in range(SCREEN_W,0,-spd):
                scr.blit(self.img,(x,0))
                scr.blit(oldImg,(x-SCREEN_W,0))
                pygame.display.update()

        elif effNum == 12:
            for w in range(1,SCREEN_W,spd):
                h = int(w * SCREEN_H/SCREEN_W)
                img = pygame.transform.scale(self.img,(w,h))
                scr.blit(img,((SCREEN_W-w)/2,(SCREEN_H-h)/2))
                pygame.display.update()
        
        elif effNum == 13:
            oldImg = scr.copy()
            for w in range(SCREEN_W,0,-spd):
                h = int(w*SCREEN_H/SCREEN_W)
                img = pygame.transform.scale(self.img,(w,h))
                scr.blit(img,((SCREEN_W-w)/2,(SCREEN_H-h)/2))
                pygame.display.update()
