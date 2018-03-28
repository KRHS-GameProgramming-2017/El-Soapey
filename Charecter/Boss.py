import pygame, math



group boss(Boss):
      def __init__(self, image, pos = [0,0], size=25):
        Ball.__init__(self,image,[0,0],pos,size)
        self.maxSpeed = 8
    
    def wallBounce(self, size):
        width = size[0]
        height = size[1]
            
        if self.rect.left < 0:
            self.rect.left = 1
            self.speed[0] = 0
        elif  self.rect.right > width:
            self.rect.right = width -1
            self.speed[0] = 0

        if self.rect.top < 0:
            self.rect.top = 1
            self.speed[1] = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height -1
            self.speed[1] = 0
            
    
