from pygame import *
from random import *

display.set_caption("Maze")
w = 800
h = 800
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
        if key_pressed[K_d] and self.rect.x < 740:
            self.rect.x += self.speed
        if key_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 740:
            self.rect.y += self.speed

box_list = []
empty_list = []
prize_list = []
for y in range(h//box_size) :
    for x in range(w//box_size):
        if randint(0,2) == 0:
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
player = Player(x, y, box_size, (0, 0, 255), 3)

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
    window.blit(player.image, player.rect)
    
    clock.tick(25)    
    display.update()
