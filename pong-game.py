import pygame
pygame.init()

circleX = 320
circleY = 180

xspeed = 1
yspeed = 1

run = True

life = 3

win = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Pong game")

while run:
    pygame.time.delay(5)

    if life == 3:
        win.fill((0,255,0))
    elif life == 2:
        win.fill((0,0,255))
    elif life == 1:
        win.fill((255,0,0))
    else:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(win, (255,255,255), (circleX, circleY), 20, 20)
    pygame.draw.rect(win, (0,0,0), (pygame.mouse.get_pos()[0]-75, 350, 150, 10))

    circleX += xspeed
    circleY += yspeed

    if circleX < 20 or circleX > 640-20:
        xspeed = xspeed * -1

    if circleY < 20:
        yspeed = yspeed * -1

    if circleY > 340:
        yspeed = yspeed * -1
        if circleX < pygame.mouse.get_pos()[0]-90 or circleX > pygame.mouse.get_pos()[0]+90:
            life -= 1

    pygame.display.update()

pygame.quit()