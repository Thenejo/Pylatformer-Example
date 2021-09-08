import pygame
from Data.scripts.Entity import *
from Data.scripts.Animation import *
from Data.scripts.coreFunctions import *




class Player(entity):
    def __init__(self,x,y,startTexture):
        super().__init__(x,y,startTexture)
        animationList={"Idle":loadAnimationFromFolder("data/res/Player/Idle",frameTime=10),
                       "Move":loadAnimationFromFolder("data/res/Player/Move",frameTime=10),
                       "Fall":loadAnimationFromFolder("data/res/Player/Jump",frameTime=10)}
        self.animContoller=AnimatonController(animationList,"Idle")
        self.hsp=0.0
        self.vsp=0.0

        self.jumpHeight=0.9
        self.grv=0.13
        self.cayotiTime=10
        self.airTime=0
        self.jumpInput=False
        self.jumpTime=0.2*60
        self.jumpTimer=0
        self.acc=0.1
        self.speed=1
        self.horizontalInput=0
    def InputPressed(self):
        pressed_keys=pygame.key.get_pressed()
        self.horizontalInput=0
        if pressed_keys[pygame.K_RIGHT]:
            self.horizontalInput+=1
        if pressed_keys[pygame.K_LEFT]:
            self.horizontalInput-=1

    def InputDown(self,e):
        if e.type==pygame.KEYUP:
            if e.key==pygame.K_SPACE:
                self.jumpInput=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE and self.airTime<3+self.cayotiTime: #3 is because when you make the vsp=0 it takes 3 frames to touch the block againg
                self.jumpInput=True
                self.jumpTimer=self.jumpTime
                self.airTime+=self.cayotiTime
                #self.vsp=-self.jumpHeight
    def Run(self,tiles,window):
        self.jumpTimer-=1
        if self.jumpTimer<0:
            self.jumpInput=False
        self.hsp=lerp(self.hsp,self.horizontalInput*self.speed,self.acc)
        self.vsp+=self.grv
        if self.jumpInput:
            self.vsp=-self.jumpHeight
        print("X:",str(self.pos[0]))
        print("Y:",str(self.pos[1]))
        print("AirTime:",str(self.airTime))
        if self.hsp<0.05 and self.hsp> -0.05:
            self.animContoller.setState("Idle")
        else:
            if self.hsp>0:
                self.animContoller.flipAnims(False,False)
            else:
                self.animContoller.flipAnims(True,False)
            self.animContoller.setState("Move")
        if self.vsp>0.6:
            self.animContoller.setState("Fall")

        collisions=self.move([self.hsp,self.vsp],tiles)
        if collisions["right"] or collisions["left"]:
            self.hsp=0
        if collisions["top"] or collisions["bottom"]:
            self.vsp=0

        if collisions["bottom"]:
            self.airTime=0
        else:   
            self.airTime+=1
        self.sprite=self.animContoller.Run()
        self.render(window)
