import pygame

import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
def run():

	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Shooter. Defender")
	bg_color = (0,0,0)
	gun = Gun(screen)
	bullets = Group()
	#Создание группы пришельцев.
	inos = Group()
	controls.create_army(screen, inos)
	stats = Stats()

	while True:
		controls.events(screen, gun, bullets)
		gun.update_gun()
		controls.update(bg_color, screen, gun, inos, bullets)
		controls.update_bullets(screen, inos, bullets)
		controls.update_inos(stats, screen, gun, inos, bullets)


run()



