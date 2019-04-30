import pygame, sys, random, math
SCREEN_W, SCREEN_H = 800, 600

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
            print('7')
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


class CLS_photoship(object):
    def __init__(self):
        pygame.init()
        self.scr = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        pygame.display.set_caption('RT Photoship')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('STXINGKA.ttf',32)
        self.picList = []
        self.load_pic()
        self.picCurNum = 0
        self.spd = 5
        self.effNum = 0
    def load_pic(self):
        flist = ['xian01.jpg','xian02.jpg','xian03.jpg','xian04.jpg','trump.jpg']
        for fileName in flist:
            self.picList.append(CLS_pic(fileName))

    def play(self):
        self.picList[self.picCurNum].draw(self.scr)
        pygame.display.update()
        self.clock.tick(50)
    
    def keydown(self,key):
        if event.key in (32,pygame.K_RIGHT):
            self.picCurNum = (self.picCurNum +1)%\
                len(self.picList)
            self.picList[self.picCurNum].draw(self.scr,self.effNum,self.spd)
        elif event.key == pygame.K_LEFT:
            self.picCurNum =(self.picCurNum-1)%\
                len(self.picList)
            self.picList[self.picCurNum].draw(self.scr,self.effNum,self.spd)
        elif ord('0') <= event.key <= ord('9'):
            self.spd = event.key-48
        elif ord('a') <= event.key <= ord('z'):
            self.effNum = event.key - ord('a') +1

# -------------main---
pship = CLS_photoship()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pship.keydown(event.key)
    pship.play()

