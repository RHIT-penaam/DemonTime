import sys

import pygame

class MikeDemonSlayer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullets = []
        self.image = pygame.image.load('Nipple_Boy.jpg')

    def draw(self):
        self.screen.blit(self.image, (0, 0))

    def primary_fire(self):
        new_bullet = bullet_neutral(self.screen, 41, self.y)
        self.bullets.append(new_bullet)
        # add sound?
class Demon:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y



class bullet_neutral:
    def __init__(self, screen, x, y, speed, size, length):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.size = int(size)
        self.len = int(length)
        self.has_boomed = False


    def move(self):
        self.x += self.speed


    def draw(self):
        pygame.draw.line(self.screen, (255, 100, 70), (self.x, self.y), (self.x, self.y), self.size)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    background = pygame.image.load("unknown.png")
    pygame.display.set_caption("Mike's Rainy Day in Hell")
    screen = pygame.display.set_mode((1500, 780))
    # screen.fill((0, 0, 0))
    hero = MikeDemonSlayer(screen, 320, 590)
    screen.blit(background, (10, 10))


    while True:
        clock.tick(60)


        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                hero.primary_fire()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            hero.y -= 5



main()
