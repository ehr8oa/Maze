from pygame import *
from random import *

init()

display.set_caption("Maze")
w = 800
h = 800
score = 0
font = font.SysFont('Arial', 35)
window = display.set_mode((w, h))
box_size = 40
clock = time.Clock()

class GameObject:
    def __init__(self, x, y, size, color, speed):
        self.rect = Rect(x, y, size, size)
        self.image = Surface((size, size))
        self.image.fill(color)
        self.speed = speed

class Player(GameObject):
    def control(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
            if self.collide():
                self.rect.x += self.speed
        if key_pressed[K_d] and self.rect.x < 760:
            self.rect.x += self.speed
            if self.collide():
                self.rect.x -= self.speed
        if key_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
            if self.collide():
                self.rect.y += self.speed
        if key_pressed[K_s] and self.rect.y < 760:
            self.rect.y += self.speed
            if self.collide():
                self.rect.y -= self.speed
    def collide(self):
        for box in box_list:
            if self.rect.colliderect(box.rect):
                return True
    
        for prize in prize_list:
            if self.rect.colliderect(prize.rect):
                prize_list.remove(prize)
                global score
                score += 1
        
        for enemy in enemy_h_list:
            if self.rect.colliderect(enemy.rect):
                player.rect.x = h//2
                player.rect.y = w//2
        
        for enemy in enemy_v_list:
            if self.rect.colliderect(enemy.rect):
                player.rect.x = h//2
                player.rect.y = w//2
                

class Enemy(GameObject):
    def h_walk(self):
        self.rect.x += self.speed
        if self.rect.x > w-box_size or self.rect.x < 0:
            self.speed *= -1

    def v_walk(self):
        self.rect.y += self.speed
        if self.rect.y > h-box_size or self.rect.y < 0:
            self.speed *= -1
        
    
box_list = []
empty_list = []
prize_list = []
for y in range(1,(h//box_size)-1) :
    for x in range(1,(w//box_size)-1):
        if randint(0,2) == 0:
            if x != (w//box_size)//2 and y != (h//box_size)//2:
                box = GameObject(x*box_size, y*box_size, box_size, (255, 0, 0),0)
                box_list.append(box)
        else:
            empty_list.append((x*box_size, y*box_size))

for i in range(0,11):
    x,y = choice(empty_list)
    empty_list.remove((x,y))
    prize = GameObject(x, y, box_size, (249, 215, 28), 0)
    prize_list.append(prize)
    
x,y = choice(empty_list)
player = Player(x, y, box_size, (0, 0, 255), 10)

enemy_0 = Enemy(0,h-box_size,box_size,(255,10,255),10)
enemy_1 = Enemy(0,0,box_size,(255,10,255),10)
enemy_2 = Enemy(0,0,box_size,(255,10,255),10)
enemy_3 = Enemy(w-box_size,0,box_size,(255,10,255),10)
enemy_4 = Enemy(w/2,0,box_size,(255,10,255),10)
enemy_5 = Enemy(0,h/2,box_size,(255,10,255),10)

enemy_h_list = [enemy_0,enemy_2,enemy_5]
enemy_v_list = [enemy_1,enemy_3,enemy_4]

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill((0, 0, 0))
    for box in box_list:
        window.blit(box.image, box.rect)
    for prize in prize_list:
        window.blit(prize.image, prize.rect)
    player.control()   
    
    for enemy in enemy_h_list:
        enemy.h_walk()
        window.blit(enemy.image, enemy.rect)

    for enemy in enemy_v_list:
        enemy.v_walk()
        window.blit(enemy.image, enemy.rect)

    window.blit(player.image, player.rect)

    score_text = font.render('Счет: '+ str(score),True, (255,255,255))
    window.blit(score_text, (20, 20))
    clock.tick(25)    
    display.update()
