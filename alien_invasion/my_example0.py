# https://www.pygame.org/docs/ref/event.html#module-pygame.event
# https://www.pygame.org/docs/ref/key.html?highlight=k_right

import pygame

pygame.init()

# set mode, 이미지 두개 로드
screen_surf = pygame.display.set_mode((1280,720)) # screen_surf,img는 surface니까 rect를 가짐
ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')
# rect 위치를 초기화
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom # 여기서 제공하는 위치함수활용 -> 바닥의 중앙끼리 맞춰줌
alien_rect = pygame.rect.Rect(200,200,200,200)
# 총알 담는 바구니
bullet_rect = None
bullets = []
# alien 담는 바구니
aliens = []
for i in range(6):
    alien = pygame.rect.Rect(100+200*i,100,100,100)
    aliens.append(alien)

clock = pygame.time.Clock()

# 누르고 있을 때도 실행되도록
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
# alien이 자동으로 움직이도록
aliens_x_direction = 1 # 1은 오른쪽, -1은 왼쪽

while True: # 무한루프
    # 키, 마우스 이벤트를 여기에 넣을 것
    for event in pygame.event.get(): # 이게 리스트
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알 발사 (한 화면에서 5번 이하로 제한시키기)
                if len(bullets)<5:
                    bullet_rect = pygame.rect.Rect(0,0,5,30) # 총알만들기
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect) 
                elif event.key == pygame.K_q:
                    pygame.quit()
                    raise SystemExit
            if event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
            
    # 어떻게, 얼마나 움직일지
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
    elif up_pressed:
        ship_rect.y = ship_rect.y-2
        alien_rect.y = alien_rect.y-4
    elif down_pressed:
        ship_rect.y = ship_rect.y+2
        alien_rect.y = alien_rect.y+4
    if bullets:
        screen_rect = screen_surf.get_rect()
        # 한 화면에서 5번 이하로 제한시키기
        for bullet in bullets:
            if bullet.y<0:
                bullets.remove(bullet)
        for bullet in bullets:
            bullet_rect.y = bullet_rect.y - 10

    screen_rect = screen_surf.get_rect()
    alien_edge_reached = False
    for alien in aliens:
        alien.x += 2 * aliens_x_direction
        if alien.right >= screen_rect.width +50 or alien.left <= 0:
            alien_edge_reached = True

    if alien_edge_reached:
        aliens_x_direction *= -1
        for alien in aliens:
            alien.y += 10

    screen_surf.fill((0,0,0))  # Fill the display with a solid color (이전 화면 지우기)

    # 화면에 뿌리는 방법은 surface 위에 blit 아니면 fill
    screen_surf.blit(ship_img, ship_rect)
    #screen_surf.blit(alien_img, alien_rect) -> aliens 배열을 넣을거라서 이건 지우기
    if aliens: # aliens 배열 넣기
        for alien in aliens:
            screen_surf.blit(alien_img, alien)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet_rect) # pygame.draw.rect 속성맞춰서 적기

    # alien, bullet 충돌 시(colliderect : rect가 겹쳐지면), 둘다 사라지도록 
    for alien in aliens:
        for bullet in bullets:
            if pygame.rect.Rect.colliderect(alien,bullet):
                aliens.remove(alien)
                bullets.remove(bullet)
                if len(aliens)==0:
                    print("!!! THE END !!!")

    pygame.display.flip()  # Refresh on-screen display (이동 후의 화면으로 전환)
    clock.tick(60)        
