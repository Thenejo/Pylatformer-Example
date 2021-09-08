import pygame
from data.scripts.Entity import *
from data.scripts.Animation import *
from Player import *
import Block
import json,random


pygame.init()



window=pygame.Surface((64,64))
screen=pygame.display.set_mode((600,600))

mainClock=pygame.time.Clock()


charachter=Player(0,0,Texture("data/res/Player/Move/Move.png"))
#level Stuff
blocks=[]
hazards=[]
tile_size=8
curLev="Level1"
levelFile=open("Level.json","r")
levelData=json.loads(levelFile.read())
def loadlevel():
    for y in range(len(levelData[curLev])):
        for x in range(len(levelData[curLev][y])):
            if levelData[curLev][y][x]==1:
                blocks.append(Block.block(x*tile_size,y*tile_size))
            elif levelData[curLev][y][x]==2:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/dirt.png"))
            elif levelData[curLev][y][x]==3:
                charachter.pos[1]=y*tile_size
                charachter.pos[0]=x*tile_size
            elif levelData[curLev][y][x]==4:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/edge.png"))
            elif levelData[curLev][y][x]==5:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/cliff.png",True))
            elif levelData[curLev][y][x]==6:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/cliff.png"))
            elif levelData[curLev][y][x]==7:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/edge.png",True))
            elif levelData[curLev][y][x]==8:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/inbetween.png"))
            elif levelData[curLev][y][x]==9:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/inbetween.png",True))
            elif levelData[curLev][y][x]==11:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/tileR.png",True,False))
            elif levelData[curLev][y][x]==12:
                blocks.append(Block.block(x*tile_size,y*tile_size,"data/res/tileR.png",False,False))
            elif levelData[curLev][y][x]==13:
                hazards.append(Block.block(x*tile_size,y*tile_size,"data/res/spike.png",False,False,[4,5,3,4],(0,0,0)))
loadlevel()



isRunning=True

while isRunning:
    for e in pygame.event.get():
        charachter.InputDown(e)
        if e.type==pygame.QUIT:
            isRunning=False
    window.fill((105,109,109))
    #Do Stuff Here
    for b in blocks:
        b.Render(window)
    charachter.InputPressed()
    charachter.Run(blocks,window)
    pygame.transform.scale(window,(600,600),screen)
    pygame.display.update()
    mainClock.tick_busy_loop(60)
    print("fps: "+str(mainClock.get_fps()))
