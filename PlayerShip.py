import pygame, sys, math
from Ship import *
#ARGUMENTS 
#Image, Arsenal, Velocity, startPos, Health

class PlayerShip(Ship):
    def __init__(self, maxSpeed, startPos=[400,1000]):
        Ship.__init__(self,"ball.png",[0,0], startPos)
        self.maxSpeed = maxSpeed
        self.goal = [0,0]

        self.frame = 0;
        self.images = self.imagesE
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.aniTimer = 0
        self.aniTimerMax = 60/4
        
        self.maxSpeed = maxSpeed
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos

    def go(self, d):
        if d == "north":
            self.speedy = -self.maxSpeed
            self.images = self.imagesN
        if d == "south":
            self.speedy = self.maxSpeed
            self.images = self.imagesS
        if d == "west":
            self.speedx = -self.maxSpeed
            self.images = self.imagesW
        if d == "east":
            self.speedx = self.maxSpeed
            self.images = self.imagesE
            
        if d == "northU":
            self.speedy = 0
        if d == "southU":
            self.speedy = 0
        if d == "westU":
            self.speedx = 0
        if d == "eastU":
            self.speedx = 0


    def update(self, size):
        Ship.update(self, size)
        self.animate()
        
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
                
            self.image = self.images[self.frame]

    def headTo(self, pos):
        self.goal = pos
        if self.rect.centerx > pos[0]:
            self.speedx = -self.maxSpeed
        elif self.rect.centerx < pos[0]:
            self.speedx = self.maxSpeed
        else:
            self.speedx = 0
            
        if self.rect.centery > pos[1]:
            self.speedy = -self.maxSpeed
        elif self.rect.centery < pos[1]:
            self.speedy = self.maxSpeed
        else:
            self.speedy = 0
            
        print self.speedx, self.speedy
        
        
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
