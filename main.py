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
        self.image = pygame.image.load('nipple_boy_transparent')
        self.image.set_colorkey((255, 255, 255))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def primary_fire(self):
        new_bullet = bullet_neutral(self, self.screen, 41, self.y + self.image.get_height() / 2, 4, random.randrange(3, 10), random.randrange(3, 10))
        self.bullets.append(new_bullet)
        # add sound?

    def move(self, disp):
        self.y += int(disp)

    # def remove_dead_bullets(self):
    #     for k in range(len(self.bullets), - 1, - 1, - 1):
    #         if self.bullets[k].has_boomed or self.bullets[k].x > 1200:
    #             del self.missiles[k]


class Demon:
    def __init__(self, screen, x, y, max_health, species):
        self.x = random.randint(screen.get_leng(), 0)
        self.y = random.randint(screen.get_height(), 0)
        self.screen = screen
        self.image_neut = pygame.image.load('Goofy_Mouth_Boy.png')
        self.image_bloodied = pygame.image.load('nipple_boy_transparent')
        self.image_dead = pygame.image.load('nipple_boy_transparent')
        self.health = max_health
        self.max = max_health
        self.species = species
        self.is_dead = False

    def draw(self):
        if self.health // self.max > 0.5:
            self.screen.blit(self.image_neut, (self.x, self.y))
        elif self.health // self.max < 0:
            self.screen.blit(self.image_bloodied, (self.x, self.y))
        else:
            self.screen.blit(self.image_bloodied, (self.x, self.y))
            self.is_dead = True

    def move(self):
        self.x -= 4
    def hit_by(self):
        hitbox = pygame.Rect(self.x, self.y, self.image_neut.get_width())

# class Horde:
#     def __init__(self, screen):
#         self.horde = []
#         Impliment death wail
        # for d in range(10):
        #     self.demons.append(Demon(screen, 1200, random.randrange(200, 300), 30, "mouth"))

    # @property
    # def is_defeated(self):
    #     return len(self.horde) == 0
    #
    # def move(self):
    #     for demon in self.horde:
    #         demon.move()
    #
    # def draw(self):
    #     for demon in self.horde:
    #         demon.draw()

    # Maybe implement a corpse cleaner upper, or maybe not

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
        pygame.draw.line(self.screen, (255, random.randrange(10, 200, 10), 70), (self.x, self.y), (self.x + self.leng, self.y), self.size)

class Scoreboard(object):
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)
    def draw(self):
        score_string = "Score: {}".format(self.score)
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))

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
    incanus = Demon(screen, 1000, 200, 30, "teeth")
    # throng = Horde(screen)


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

        incanus.move()
        incanus.draw()
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
