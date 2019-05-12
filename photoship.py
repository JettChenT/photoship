# photoship
from pic import *
class CLS_photoship(object):
    def __init__(self):
        pygame.init()
        self.scr = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        pygame.display.set_caption('RT Photoship')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('STXINGKA.ttf',32)
        self.picList =[]
        self.spd = 5
        self.guideList = []
        self.guideID = 0
        self.font = pygame.font.Font('STXINGKA.TTF',32)
        self.mousePos = 0,0
    def add_guide(self,guide):
        guide.id = len(self.guideList)
        self.guideList.append(guide)

    def play(self):
        for guide in self.guideList:
            guide.draw(self.scr)
        pygame.draw.circle(self.scr,(0,0,99),self.mousePos,50,5)
        pygame.display.update()
        self.clock.tick()
        
    def keydown(self,key):
        pass
    def mouse_down(self,pos,btn):
        self.guideList[self.guideID].mouse_down(pos,btn)
    def mouse_up(self,pos,btn):
        self.guideList[self.guideID].mouse_up(pos,btn)
    def mouse_motion(self,pos):
        self.guideList[self.guideID].mouse_motion(pos)

class CLS_guide(object):
    def __init__(self,picName):
        self.pic = CLS_pic(picName)
        self.btnList = []
        self.id = 0
    def draw(self,scr):
        if pship.guideID != self.id:
            return
        scr.blit(self.pic.img,(0,0))
        for btn in self.btnList:
            btn.draw(scr)
    def add_button(self,name,picFile,x,y,guideID):
        b = CLS_button(name,picFile,x,y,guideID)
        self.btnList.append(b)
    def mouse_down(self,pos,button):
        for btn in self.btnList:
            btn.mouse_down(pos,button)

    def mouse_up(self,pos,button):
        for btn in self.btnList:
            btn.mouse_up(pos,button)
    def mouse_motion(self,pos):
        self.mousePos = pos

class CLS_button(object):
    def __init__(self,name,picFile,x,y,guideID):
        self.name = name
        self.img = pygame.image.load(picFile)
        self.img.set_colorkey((38,38,38))
        self.w,self.h = self.img.get_width()//2,self.img.get_height()
        self.x, self.y = x,y
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.status = 0
        self.guideID = guideID
    def draw(self,scr):
        scr.blit(self.img,(self.x,self.y),(self.status*self.rect.w,0,self.rect.w,self.rect.h))
    def mouse_down(self,pos,button):
        if self.rect.collidepoint(pos):
            self.status = 1
    def mouse_up(self,pos,button):
        self.status = 0
        if not self.rect.collidepoint(pos):
            return
        if self.name == 'U':
            pship.guideList[self.guideID].pic.draw(pship.scr,12,pship.spd)
        elif self.name == 'D':
            pship.guideList[self.guideID].pic.draw(pship.scr,13,pship.spd)
        elif self.name == 'L':
            pship.guideList[self.guideID].pic.draw(pship.scr,10,pship.spd)
        elif self.name == 'R':
            pship.guideList[self.guideID].pic.draw(pship.scr,11,pship.spd)

        pship.guideID = self.guideID
def add_btn(btn1,direction,btn2):
    if direction == 'U':
        btn1.add_button('U','bUp.bmp',SCREEN_W//2-35,20,btn2.id)
        btn2.add_button('D','bDown.bmp',SCREEN_W//2-35,SCREEN_H-100,btn1.id)
    elif direction == 'D':
        btn1.add_button('D','bDown.bmp',SCREEN_W//2-35,SCREEN_H-100,btn2.id)
        btn2.add_button('U','bUp.bmp',SCREEN_W//2-35,20,btn1.id)
    elif direction == 'L':
        btn1.add_button('L','bLeft.bmp',20,SCREEN_H//2-35,btn2.id)
        btn2.add_button('R','bRight.bmp',SCREEN_W-100,SCREEN_H//2-35,btn1.id)
    elif direction == 'R':
        btn2.add_button('L','bLeft.bmp',20,SCREEN_H//2-35,btn1.id)
        btn1.add_button('R','bRight.bmp',SCREEN_W-100,SCREEN_H//2-35,btn2.id)
#----init-----
pship = CLS_photoship()
def xian():
    G01 = CLS_guide('xian01.jpg')
    pship.add_guide(G01)
    G02 = CLS_guide('xian02.jpg')
    pship.add_guide(G02)
    G03 = CLS_guide('xian03.jpg')
    pship.add_guide(G03)
    G04 = CLS_guide('xian04.jpg')
    pship.add_guide(G04)
    add_btn(G01,'U',G02)
    add_btn(G01,'L',G03)
    add_btn(G01,'R',G04)
def house():
    bookroom = CLS_guide('bookroom.jpg')
    pship.add_guide(bookroom)
    balcony = CLS_guide('balcony.jpg')
    pship.add_guide(balcony)
    chair = CLS_guide('chair.jpg')
    pship.add_guide(chair)
    laundry = CLS_guide('laundry.jpg')
    pship.add_guide(laundry)
    add_btn(bookroom,'U',balcony)
    add_btn(balcony,'L',chair)
    add_btn(chair,'L',laundry)
house()
# -------------main---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pship.keydown(event.key)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            pship.mouse_down(event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            pship.mouse_up(event.pos,event.button)
        elif event.type == pygame.MOUSEMOTION:
            pship.mouse_motion(event.pos)
    pship.play()
