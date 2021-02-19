import sys

import pygame

import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien

from pygame.sprite import  Group

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    settings = Settings()

    screen_size = (settings.screen_width, settings.screen_height)
    screen = pygame.display.set_mode(screen_size)

    ship = Ship(settings, screen)
    alien = Alien(settings, screen)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, aliens, bullets)


run_game()
