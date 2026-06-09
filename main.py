import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT +1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT +2
BLUE = pygame.color('blue')
LIGHTBLUE = pygame.color('lightblue')
DARKBLUE = pygame.color('darkblue')
YELLOW = pygame.color('yellow')
MAGENTA = pygame.color('magenta')
ORANGE = pygame.color('orange')
WHITE = pygame.color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choise([-1,1]), random.choise([-1,1])]
    def update(self):
        self.move.rect_ip(self.velocity)
        boundary_hit = False
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0]= -self.velocity[0]
            boundary_hit = True
        if self.rect.top<= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
all_sprites_list = pygame.sprite.group()
sp1 = Sprite(WHITE, 50, 50)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
