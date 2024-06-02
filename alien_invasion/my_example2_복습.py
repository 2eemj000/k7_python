# https://www.pygame.org/docs/tut/newbieguide.html
# https://www.pygame.org/docs/ref/event.html#module-pygame.event
# surface > rect
import sys
import pygame

print('hello')
pygame.init()
screen_surf = pygame.display.set_mode(size=(800,640))
print(type(screen_surf),screen_surf.get_rect())
# .convert() : 빠르게 화면 렌더링
ship_img_surf = pygame.image.load('images/ship.bmp').convert()
print(type(ship_img_surf),ship_img_surf.get_rect())
# font.render는 텍스트를 렌더링하여 표면(Surface) 객체를 생성
font = pygame.font.SysFont(None,64)
font_surf = font.render(str(5678),True,'black')

bullets=[]
aliens=[]
bullet_rect = pygame.Rect(0,0,10,50)
bullets.append(bullet_rect)
print(bullet_rect)
clock = pygame.time.Clock()
# events는 리스트

while True:
    events = pygame.event.get()
    # print(type(events),events)
    # print(events[0].type) # 내부적으로 정해진 값
    # print(type(events[0]),dir(events[0].type))
    for e in events:
        print(e.type,type(e.type))
        if e.type == pygame.QUIT:
            # print('QUIT')
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            # print('KEYDOWN')
            print(e.key,type(e.key))
            if e.type == pygame.KEYUP:
                # print('KEYUP')
                print(e.key,type(e.key))
            elif e.type == pygame.K_SPACE:
                # sys.exit() # ctrl+.누르고 enter치면 자동으로 import해줌
                sys.exit()
    screen_surf.fill('white')
    screen_surf.blit(ship_img_surf, ship_img_surf.get_rect())
    screen_surf.blit(font_surf, (100,100, font_surf.get_rect().width, font_surf.get_rect().height))
    pygame.display.flip() # 이동 후의 화면으로 전환
    clock.tick(60)        
    
# print(pygame.QUIT)
# print(pygame.KEYDOWN)
# print(pygame.KEYUP)

