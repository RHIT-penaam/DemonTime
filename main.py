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
