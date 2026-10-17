
import pygame
import os
import time
import random
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.update()
ground = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/ground.png")
bg = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/bg.png")
groundx = 00
class bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.listz = []
        self.index = 0
        self.counter = 0
        self.gravity = 1
        for i in range(3):
            birdi = pygame.image.load(f"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/bird{i+1}.png")
            birdi = pygame.transform.scale(birdi, (32, 32))
            self.listz.append(birdi)
        self.image = self.listz[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = ((100, 100))
    def animation(self):
        if click == True:
            '''print('yes')'''
            if self.rect.bottom < 600:
                self.rect.y += self.gravity
                self.gravity = self.gravity*1.01
                if klik == True:
                    self.gravity = 1
                    for i in range(100):
                        self.rect.y = self.rect.y - 1
                        
        self.counter = 0
        self.counter += 1
        limit = 5
        if self.counter > limit:
            self.counter = 0
            self.index += 1
            if self.index >= 3:
                self.index = 0
        self.image = self.listz[self.index]

class pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, UpOrDown, gap):
        super().__init__()
        self.image = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/pipe.png")
        self.rect = self.image.get_rect()
        self.score = 0
        if UpOrDown == 0:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - gap/2)
        if UpOrDown == 1:
            self.rect.topleft = (x, y + gap/2)

    def update(self):
        self.rect.x -= 2
        if self.rect.x <= 0:
            self.score += 1
            self.kill()

        
        
score = -1
lever = False
birdgroup = pygame.sprite.Group()
bird1 = bird()
birdgroup.add(bird1)
click = False
klik = False
pipegroup = pygame.sprite.Group()
gap = 250
gapreduction = random.randint(-20, 20)
reducegap = 1
variation = random.randint(350, 350)
counter = 0
timegap = 3000
ticks = pygame.time.get_ticks()
fast = 10
while 1 == 1:
    timenow = pygame.time.get_ticks()
    pipeup = pipe(700,variation+gapreduction,1,gap)
    pipedown = pipe(700,variation-gapreduction,0,gap)
    if timenow - ticks > timegap:
        pipegroup.add(pipeup)
        pipegroup.add(pipedown)
        gap -= gapreduction
        gapreduction = random.randint(-5, 6)
        counter += 10
        variation = random.randint(350 - counter, 350 + counter)
        if counter >= 300:
            counter = 300
        if gap <= 80:
            gap += gapreduction
        ticks = timenow - fast
        fast += 10
        score += 1
        if score >= 0:
            print(score)
    if pygame.sprite.groupcollide(birdgroup, pipegroup, False, False):
        click = False
        klik = False
        lever = True
    screen.blit(bg, (0, 0))
    screen.blit(ground, (groundx, 600))
    bird1.animation()
    birdgroup.draw(screen)
    pipegroup.draw(screen)
    pipegroup.update()
    klik = False
    groundx -= 5
    if groundx < -100:
        groundx = 0
    if lever == True:
        klik = False
        click = False
        score = score - 1
        if bird1.rect.y <= 600 - 32:
            bird1.rect.y += 5
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_f and lever == False:
                click = True
                klik = True
                '''print('kilk')'''
        if i.type == pygame.QUIT:
            pygame.quit()
