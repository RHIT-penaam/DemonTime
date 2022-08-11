import sys

import pygame

class MikeDemonSlayer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullets = []

    def draw(self):

    def primary_fire(self):
        new_bullet =

class bullet_neutral:
    def __init__(self, screen, x, y, speed, size, len):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.size = int(size)
        self.len = int(len)
        self.has_boomed = False

    def move(self):
        self.x += speed

    def draw(self):
        pygame.draw.line(self.screen, (255, 100, 70), (self.x, self.y), (self.x, self.y), (self.x, self.y + self.len), self.size)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Mike's Rainy Day goes to Hell")
    screen = pygame.display.set_mode((640, 650))
    hero = MikeDemonSlayer(screen, 320, 590)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()


main()
