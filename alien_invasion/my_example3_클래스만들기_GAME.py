
import sys
import pygame

from my_example3_클래스만들기_ALIEN import Alien
from my_example3_클래스만들기_SHIP import Ship

class Game:
    def __init__(self, title):
        self.title = title
        pygame.init()

        self.create_screen()
        #print(type(screen_surf), screen_surf.get_rect())
        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

        self.aliens = []
        
        # alien = Alien(self.screen_surf)
        # alien.move(50, 50)
        # self.aliens.append(alien)
        for i in range(1,5):
            for j_ in range(10):
                alien = Alien(self.screen_surf)
                x_pos = 80+(80*2)*j
                y_pos = 50+(50*2)*i
                alien.move(x_pos,y_pos)
                self.aliens.append(alien)

        alien = Alien(self.screen_surf)
        alien.move(150, 150)
        self.aliens.append(alien)

        font = pygame.font.SysFont(None, 64)
        self.font_surf = font.render(
            str(5678), 
            True, 
            'black'
            )
        #print(font_surf.get_rect())

        self.bullets = []
        

        # bullet_rect = pygame.Rect(0, 0, 10, 50)
        # #print(bullet_rect)
        # self.bullets.append(bullet_rect)

        self.clock = pygame.time.Clock()

    def create_screen(self):
        self.screen_surf = pygame.display.set_mode(size=(800, 640))

    def start(self):
        while True:
            events = pygame.event.get() 
            for e in events:
                print(e.type, type(e.type))
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    pass
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_SPACE:
                        # sys.exit()
                        bullet = Bullet(self.screen_surf)
                        bullet.move_front_ship(self.ship.get_rect())
                        self.bullets.append(bullet)


            self.screen_surf.fill('white')
            self.ship.render()
            for alien in self.aliens:
                alien.render()
            for bullet in self.bullets:
                bullet.render()
            self.screen_surf.blit(self.font_surf, (100, 100, 
                                        self.font_surf.get_rect().width,
                                        self.font_surf.get_rect().height))   
            pygame.display.flip()
            self.clock.tick(60)

    def __str__(self):
       return self.title

