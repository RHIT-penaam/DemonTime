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
        # self.image.set_colorkey((255, 255, 255)) 'has no effect'

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def primary_fire(self):
        new_bullet = bullet_neutral(self, self.screen, 41, self.y + self.image.get_height() / 2, 5, 4, 4)
        self.bullets.append(new_bullet)
        # add sound?

    def move(self, disp):
        self.y += int(disp)

    def remove_dead_bullets(self):
        for k in range(len(self.bullets) - 1, - 1, - 1):
            if self.bullets[k].has_boomed or self.bullets[k].x > 1500:
                del self.bullets[k]


class Demon:
    def __init__(self, screen, x, y, max_health, species, step):
        self.screen = screen
        self.x = screen.get_width()
        self.y = random.randint(0, screen.get_height())
        self.image_current = pygame.image.load('transparent demon')
        self.image_neut = pygame.image.load('transparent demon')
        self.image_bloodied = pygame.image.load('nipple_boy_transparent')
        self.image_dead = pygame.image.load('nipple_boy_transparent')
        self.health = max_health
        self.max = max_health
        self.species = species
        self.is_dead = False
        self.step = step

    def costume(self):
        if self.health // self.max > 0.5:
            self.image_current = self.image_neut
        elif self.health // self.max < 0:
            self.image_current = self.image_bloodied

    def draw(self):
        self.screen.blit(self.image_current, (self.x, self.y))

    def move(self):
        beans = random.randrange(2, 6, 1)
        self.step = random.randrange(0, beans, 1)
        self.x -= self.step

    def hit_by(self, bullet):
        hitbox = pygame.Rect(self.x, self.y, self.image_neut.get_width(), self.image_neut.get_height())
        if hitbox.collidepoint(bullet.x, bullet.y):
            self.health -= 5
        return hitbox.collidepoint(bullet.x, bullet.y)


class particle:
    def __init__(self, screen, x, y, size, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.color = color
        self.the_end = 30

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
        self.the_end -= 1

    def move(self):
        self.x += random.randrange(-4, 6)
        self.y += random.randrange(-4, 4) + 1


class gibs:
    def __init__(self, screen):
        self.splatters = []
        self.screen = screen
        self.conut = 0
        self.bloodlets = []

    def make_gib(self, x, y):
        tony = splatter(self.screen, 32, x, y)
        self.splatters += [tony]

    def make_blood(self, x, y):
        antonio = particle(self.screen, x, y, 1, (255, 30, 40))
        self.bloodlets += [antonio]

    def move(self):
        for splat in self.splatters:
            splat.move()
        for bleed in self.bloodlets:
            bleed.move()

    def draw(self):
        self.conut = 0
        for splat in self.splatters:
            self.conut += 1
            splat.draw()
            splat.the_end -= 1
            if splat.the_end <= 0:
                del self.splatters[self.conut - 1]
        self.conut = 0
        for blood in self.bloodlets:
            self.conut += 1
            blood.draw()
            if blood.the_end <= 0:
                del self.bloodlets[self.conut - 1]


class splatter:
    def __init__(self, screen, intensity, x, y):
        self.meat_image = pygame.image.load('output-onlinepngtools (1).png')
        self.bone_image = pygame.image.load('bone_gib.png')
        self.current_image = pygame.image.load('bone_gib.png')
        self.x = x
        self.y = y
        self.dx = random.randrange(-3, 3)
        self.dy = random.randrange(-3, 3)
        self.screen = screen
        self.type = random.randrange(1, 3)
        self.the_end = random.randrange(5, 30, 5)
        if self.type == 1:
            self.current_image = self.meat_image
        else:
            self.current_image = self.bone_image

    def draw(self):
        self.screen.blit(self.current_image, (self.x, self.y))

    def move(self):
        self.dx = random.randrange(-3, 3)
        self.dy = random.randrange(-3, 3)
        self.x += self.dx
        self.y += self.dy + 1


class Horde:
    def __init__(self, screen, num_enemies):
        self.horde = []

        #         Implement death wail
        for h in range(num_enemies):
            for d in range(10):
                self.horde.append(
                    Demon(screen, 1200 * d, random.randrange(200, 300) * h, 30, "mouth", random.randrange(1, 3, 1)))

    #
    @property
    def is_defeated(self):
        return len(self.horde) == 0

    def move(self):
        for demon in self.horde:
            demon.move()

    def draw(self):
        for demon in self.horde:
            demon.draw()

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
        pygame.draw.line(self.screen, (250, random.randrange(10, 150, 10), 70), (self.x, self.y),
                         (self.x + self.leng, self.y), self.size)


class Scoreboard(object):

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        score_string = "Score: {}".format(self.score)
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))


class Demonwing:
    def __init__(self, screen, x, y, max_health, species, speed):
        self.screen = screen
        self.max_health = max_health
        self.species = species
        self.speed = speed
        self.x = x
        self.y = y
        self.incinerate = []
        self.count = 0

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color('pink'), pygame.Rect(self.x, self.y, 10, 10))

    def move(self):
        self.x -= self.speed
        self.count += 1

    def spitfire(self):
        flame = Hellfire(self.screen, self.x, self.y, 5, 5, 2)
        self.incinerate.append(flame)


#
class Hellfire:
    def __init__(self, screen, x, y, len, width, spd):
        self.screen = screen
        self.x = x
        self.y = y
        self.len = len
        self.width = width
        self.spd = spd
        print("start")

    def move(self):
        self.x -= self.spd
        print("move")

    def draw(self):
        print('pew!')
        pygame.draw.line(self.screen, (1, 250, 1), (self.x - self.len, self.y), (self.x + 4, self.y), self.width)


#

def main():
    pygame.init()
    clock = pygame.time.Clock()
    # background = pygame.image.load("unknown.png")
    pygame.display.set_caption("Mike's Rainy Day in Hell")
    is_game_over = False
    screen = pygame.display.set_mode((1500, 780))
    # screen.fill((100, 100, 100))
    # screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 25)
    instruction_text = 'press r to play again...'
    text_color = (255, 0, 0)
    instructions_image = font.render(instruction_text, True, text_color)
    hero = MikeDemonSlayer(screen, 20, 590)
    incanus = Demon(screen, 1000, 200, 30, "teeth", random.randrange(1, 3, 1))
    bonnibel = Demonwing(screen, 1100, 200, 20, 'fury', 3)
    # throng = Horde(screen, num_enemies)
    game_over_image = pygame.image.load('istockphoto-1193545103-612x612.jpg')
    num_enemies = 1
    throng = Horde(screen, num_enemies)
    offal = gibs(screen)
    scoreboard = Scoreboard(screen)
    main_title = pygame.image.load('pixil-frame-0 (1).png')
    screen.blit(main_title, (500,100))
    while True:
        clock.tick(60)
        hero.draw()
        # screen.blit(background, (0, 0))
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                hero.primary_fire()
                # bonnibel.spitfire()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_r]:
                main()
        if is_game_over:
            screen.blit(game_over_image, (500, 226))
            screen.blit(instructions_image, (500, 500))
            pygame.display.update()
            continue

        screen.fill((0, 0, 0))
        screen.blit(main_title, (500, 100))
        pressed_keys = pygame.key.get_pressed()

        hero.draw()
        # incanus.move()
        # incanus.draw()
        bonnibel.move()
        bonnibel.draw()
        # if bonnibel.count >= 0:
        #     bonnibel.spitfire()
        for dink in bonnibel.incinerate:
            dink.move()
            dink.draw()

        throng.move()
        throng.draw()
        # if is_game_over:
        #     screen.blit(game_over_image, (500, 226))
        #     pygame.display.update()
        #     continue
        for bullet in hero.bullets:
            bullet.move()
            bullet.draw()
            hero.remove_dead_bullets()
        counter = 0
        offal.move()
        offal.draw()
        for demon in throng.horde:
            if demon.x < hero.image.get_width():
                is_game_over = True
            for bullet in hero.bullets:
                if bullet.x >= screen.get_width():
                    bullet.has_boomed = True
                if demon.hit_by(bullet):
                    bullet.has_boomed = True
                    scoreboard.score += 100

                    for k in range(6):
                        offal.make_gib(demon.x, demon.y)
                        offal.make_blood(demon.x, demon.y)
                        offal.make_blood(demon.x, demon.y)
                        offal.make_blood(demon.x, demon.y)
                    del throng.horde[counter]

                if bullet.has_boomed == True:
                    del bullet
            counter = counter + 1
            # del incanus

        if throng.is_defeated:
            num_enemies += 1
            throng = Horde(screen, num_enemies)

        if pressed_keys[pygame.K_UP]:
            hero.move(-5)
            print("up")

        if pressed_keys[pygame.K_DOWN]:
            hero.move(5)
            print("down")
        if pressed_keys[pygame.K_z]:
            print(hero.bullets)

        scoreboard.draw()
        pygame.display.update()


main()
