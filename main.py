import pygame,sys
from player import Player

class Game:
    # กลุ่มรวม Sprite ทั้งหมด (ผู้เล่น,สิ่งกีดขวาง,เอเลี่ยน)
    # เป็น Framework ของเกม 
    # ปล.Sprite คือ ภาพบิตแม็ปสองมิติที่รวมกันเป็นฉากขนาดใหญ่เเละประกอบเข้าด้วยกันกับชิ้นส่วนอื่น เช่น พื้นหลัง
    # ปล.Framework คือ "กรอบการทำงาน" จุดประสงค์ของมันก็เพื่อกำหนดรูปแบบ และวิธีการเขียนโค้ดให้เป็นไปตามกรอบ (Framework) หรือมีระเบียบ ระบบ
    def __init__(self):
        player_sprite = Player((300,300))
        self.player = pygame.sprite.GroupSingle(player_sprite)
    
    # Update กลุ่ม Sprite ทั้งหมด
    # วาด กลุ่ม Sprite ทั้งหมด
    def run(self):
        pass

if __name__ == '__main__': # เนื่องจากมีหลาย file ดังนั้นตัวนี้จะช่วยในการให้ไม่ไปรันโค้ดที่เราไม่ตั้งใจจะรัน
    pygame.init() # เริ่มต้นโมดูลของ pygame ทั้งหมด เเละ ไว้ใช้สำหรับ run เกมชนิดต่างๆ
    screen_width = 600 # ขนาดความกว้างของหน้าจอ
    screen_height = 600 # ขนาดความสูงของหน้าจอ
    screen = pygame.display.set_mode((screen_width,screen_height)) # ขนาดหน้าจอ
    clock = pygame.time.Clock() # การกำหนดความเร็วในการทำงานของ loop => ตัวกำหนดค่า fps 
    game = Game() # ให้ game เป็น class Game

    # while loop = ให้เกมมีการอัพเดต
    # for loop   = ตรวจการกระทำของผู้ใช้ทั้งหมด
    while True:
        for event in pygame.event.get():
            # event การออกเกม
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30)) # กำหนดสีของ screen -> สีเขียวอ่อน
        game.run() # รันตัวเเปร game

        pygame.display.flip()
        clock.tick(60) # การกำหนดความเร็วในการทำงานของ loop => fps = 60