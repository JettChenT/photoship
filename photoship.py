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
    def add_guide(self,guide):
        guide.id = len(self.guideList)
        self.guideList.append(guide)

    def load_pic(self):
        flist = ['xian01.jpg','xian02.jpg','xian03.jpg','xian04.jpg','trump.jpg']
        for fileName in flist:
            self.picList.append(CLS_pic(fileName))

    def play(self):
        for guide in self.guideList:
            guide.draw(self.scr)
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
