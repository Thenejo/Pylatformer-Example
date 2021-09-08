import pygame

class block:
    def __init__(self,x,y,res="data/res/tile.png",flippedX=False,flippedY=False,rectsizes=[0,0,8,8],col=(255,255,255)):
        self.rect=pygame.Rect(x+rectsizes[0],y+rectsizes[1],rectsizes[2],rectsizes[3])
        self.pos=[x,y]
        self.blockTexture=pygame.transform.flip(pygame.image.load(res).convert(),flippedX,flippedY)
        self.blockTexture.set_colorkey(col)
    def Render(self,window):
        window.blit(self.blockTexture,(self.pos[0],self.pos[1]))

