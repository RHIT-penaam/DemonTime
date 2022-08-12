import pygame
import sys
import time
import random

class MikeDemonSlayer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullets = []
        self.image = pygame.image.load('Nipple_Boy.jpg')
        self.image.set_colorkey((255, 255, 255))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def primary_fire(self):
        new_bullet = bullet_neutral(self, self.screen, 41, self.y, 4, 3, 5)
        self.bullets.append(new_bullet)
        # add sound?

    def move(self, disp):
        self.y += int(disp)
class Demon:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y



class bullet_neutral:
    def __init__(self, hero, screen, x, y, speed, size, leng):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.size = int(size)
        self.leng = int(leng)
        self.has_boomed = False
        self.hero = hero


    def move(self):
        self.x += self.speed


    def draw(self):
        pygame.draw.line(self.screen, (255, 100, 70), (self.x, self.y), (self.x + self.leng, self.y), self.size)
def main():
    pygame.init()
    clock = pygame.time.Clock()
    background = pygame.image.load("unknown.png")
    pygame.display.set_caption("Mike's Rainy Day in Hell")
    is_game_over = False
    screen = pygame.display.set_mode((1500, 780))
    screen.fill((100, 100, 100))
    screen.blit(background, (0, 0))
    hero = MikeDemonSlayer(screen, 20, 590)



    while True:
        clock.tick(60)
        hero.draw()
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                hero.primary_fire()
        pressed_keys = pygame.key.get_pressed()
        hero.draw()
        for bullet in hero.bullets:
            bullet.move()
            bullet.draw()
        if pressed_keys[pygame.K_UP]:
            hero.move(-1)
            print("up")

        if pressed_keys[pygame.K_DOWN]:
            hero.move(1)
            print("down")

        pygame.display.update()




main()
