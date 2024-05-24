import pygame


class Ship:
    def __init__(self, screen_surf):
        self.ship_img_surf = pygame.image.load('images/ship.bmp').convert()
        self.ship_rect = self.ship_img_surf.get_rect()
        self.screen_surf = screen_surf

    def render(self):
        self.screen_surf.blit(self.ship_img_surf, self.ship_rect)

    def move_midbottom(self):
        self.ship_rect.midbottom = self.screen_surf.get_rect().midbottom

    def handle_event(slef):
        if right_pressed:
            screen_rect = screen_surf.get_rect()
            if ship_rect.x < screen_rect.width - ship_rect.width: # 벗어나지 않도록
                ship_rect.x = ship_rect.x+2
            if alien_rect.x < screen_rect.width - alien_rect.width + 200: # 벗어나지 않도록
                alien_rect.x = alien_rect.x+4
        elif left_pressed:     
            if 0<ship_rect.x:  # 벗어나지 않도록
                ship_rect.x = ship_rect.x-2
            if 0<alien_rect.x:  # 벗어나지 않도록
                alien_rect.x = alien_rect.x-4

    def get_rect(self):
        return
