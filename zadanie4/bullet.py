import pygame
#import gun


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        # self.image2 = pygame.image.load('image/triangle (1).png')
        # self.rect = self.image2.get_rect()
        self.rect = pygame.Rect(0,0,2,12)
        color = (139, 195, 74)
        self.color = color
        self.speed = 1.5
        # self.rect.centerx = gun.rect.centerx
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        # self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.image2, self.rect)
        # self.screen.blit(self.image2, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)
