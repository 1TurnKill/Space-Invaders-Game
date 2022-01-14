import pygame,sys

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("../graphics/player.png").convert_alpha() # ให้การนำไฟล์ภาพ player.png เข้า โดยนับจาก Folder หลัก -> Folder graphics -> player.png
        self.rect = self.image.get_rect(midbottom = pos) # ให้ self.image มีการสร้าง rect โดยยึดหลักพิกัดในเคลื่อนที่เป็น พิกัดตรงกลาง เเละมีการค่าเท่ากับ pos