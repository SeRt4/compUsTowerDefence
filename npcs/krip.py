import pygame.image
import pygame
import math

pygame.init()

WIDTH = 1920
HEIGHT = 1080
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1920, 1080))
road = [(100, 100), (200, 200), (100, 100), (910, 500), (658, 500), (237, 500)]
clock = pygame.time.Clock()


class Warrior:
    def __init__(self, x, y, road):
        self.type = 'running'
        self.road = road
        self.stop_road = 0
        self.speed = 5
        self.hp = 500
        self.place = self.x, self.y = x, y
        self.bounty = 100
        self.image = pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaur.png')
        self.rect = self.image.get_rect(topleft=self.place)
        self.anileft = [pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaurLeft.png'),
                        pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaurLeft(2.png'),
                        pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaurLeft(3).png')]
        self.aniright = [pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaur.png'),
                         pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaur(2.png'),
                         pygame.image.load('/Users/kompas/TowerOfDifence/towdef/npcs/skins/minotaurRight(3).png')]
        self.step = 0

    def draw(self):
        self.animation()
        screen.blit(self.image, self.rect)
        pygame.display.flip()

    def move(self):
        if self.road:
            dx, dy = 0, 0
            if math.sqrt(abs(self.rect.x - self.road[0][0]) ** 2 + abs(self.rect.y - self.road[0][1]) ** 2) <= self.speed:
                self.road.append(self.road.pop(0))
            H = math.sqrt((self.rect.x - self.road[0][0]) ** 2 + (self.rect.y - self.road[0][1]) ** 2)
            x = self.rect.x - self.road[0][0]
            y = self.rect.y - self.road[0][1]
            if H:
                cos = round(x / H, 2)
                sin = round(y / H, 2)
                if x != 0 and y != 0:
                    dx = -self.speed * cos
                    dy = -self.speed * sin
                if cos == 1:
                    dx = -self.speed
                if cos == -1:
                    dx = self.speed
                if sin == 1:
                    dy = -self.speed
                if sin == -1:
                    dy = self.speed
            self.rect.x += dx
            self.rect.y += dy

    def animation(self):
        if self.rect.x - self.road[0][0] >= 0:
            self.image = self.anileft[self.step]
        else:
            self.image = self.aniright[self.step]
        self.step += 1 if self.step != 2 else -2
        print(self.step)










a = Warrior(0, 0, road)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    a.draw()
    a.move()
    clock.tick(10)
    pygame.display.flip()

pygame.quit()
