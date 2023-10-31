import pygame
import sys
import time
import ino
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                gun.mright = True
            elif event.key==pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                gun.mright = False
            elif event.key==pygame.K_a:
                gun.mleft = False

def update (bg_color, screen, gun, inos, bullets): #def update (bg_color, screen, gun, bullets):
    screen.fill(bg_color) #screen.fill(image)  #
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    for ino in inos.sprites():
        ino.draw(screen)
    #for inos in inos.sprites():
    #ino.draw(screen)
    #inos.draw()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((500-2*ino_width) / ino_width)
    number_ino_y = int((700-100*2*ino_height) / ino_height)

    for row_number in range(number_ino_y-2):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + 0.8 * ino.rect.height*row_number
            inos.add(ino)

def update_inos(stats,screen,gun,inos,bullets):
   #обновляет позицию пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats,screen,gun,inos,bullets)


def update_bullets(inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullets)
    collision = pygame.sprite.groupcollide(bullets,inos,True,True)
