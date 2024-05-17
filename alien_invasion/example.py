# https://www.pygame.org/docs/ref/event.html#module-pygame.event
# https://www.pygame.org/docs/ref/key.html?highlight=k_right

import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720)) # screen_surf,img는 surface니까 rect를 가짐
ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom # 여기서 제공하는 위치함수활용 -> 바닥의 중앙끼리 맞춰줌
alien_rect = pygame.rect.Rect(200,200,200,200)
bullet_rect = None
bullets = []

bullet_rect = pygame.rect.Rect(0,0,5,30) # 총알만들기
bullet_rect.midbottom = ship_rect.midtop
clock = pygame.time.Clock()
# 누르고 있을 때도 실행되도록
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

while True: # 무한루프
    # Process player inputs.
    # 키, 마우스 이벤트를 여기에 넣을 것
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알 발사
                bullet_rect.midbottom = ship_rect.midtop
                bullets.append(bullet_rect)
            if event.key == pygame.K_RIGHT:
                right_pressed = True
                ship_rect.x = ship_rect.x+10
                alien_rect.x = alien_rect.x+20
            elif event.key == pygame.K_LEFT:
                left_pressed = True
                ship_rect.x = ship_rect.x-10
                alien_rect.x = alien_rect.x-20
            elif event.key == pygame.K_UP:
                up_pressed = True
                ship_rect.y = ship_rect.y-10
                alien_rect.y = alien_rect.y-20
            elif event.key == pygame.K_DOWN:
                down_pressed = True
                ship_rect.y = ship_rect.y+10
                alien_rect.y = alien_rect.y+20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False


    # Do logical updates here.
    # 어떻게, 얼마나 움직일지
    if right_pressed:
        ship_rect.x = ship_rect.x+2
        alien_rect.x = alien_rect.x+4
    elif left_pressed:
        ship_rect.x = ship_rect.x-2
        alien_rect.x = alien_rect.x-4
    elif up_pressed:
        ship_rect.y = ship_rect.y-2
        alien_rect.y = alien_rect.y-4
    elif down_pressed:
        ship_rect.y = ship_rect.y+2
        alien_rect.y = alien_rect.y+4
    if bullets:
        for bullet in bullets:
            bullet_rect.y = bullet_rect.y - 5

    screen_surf.fill((0,0,0))  # Fill the display with a solid color (이전 화면 지우기)

    # Render the graphics here.
    # 화면에 뿌리는 방법은 blit 아니면 fill
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet_rect) # pygame.draw.rect 속성맞춰서 적기

    pygame.display.flip()  # Refresh on-screen display (이동 후의 화면으로 전환)
    clock.tick(60)         # wait until next frame (at 60 FPS)
