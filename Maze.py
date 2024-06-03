import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Game")
done = False
x = 110
y = 110

startTime = 0
endTime = 0

bestTime = 0
currentTime = 0

hasPressKey = False
hasTakenTime = False

clock = pygame.time.Clock()
level = 1

def level1():
    global x,y,startTime,endTime,bestTime,currentTime,hasTakenTime,hasPressKey,clock,level
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y -= 3
        hasPressKey = True
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y += 3
        hasPressKey = True
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x -= 3
        hasPressKey = True
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x += 3
        hasPressKey = True

    # Drawing
    screen.fill((0, 0, 0))
    end = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1000, 112, 100, 100))
    playerImage = pygame.image.load('player.png').convert()
    p1 = playerImage.get_rect()
    p1.center = (x,y)
    screen.blit(playerImage, p1)
    # p1 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, 100, 100))

    if hasPressKey and not hasTakenTime:
        startTime = time.time()
        print(startTime)
        hasTakenTime = True

    if hasPressKey:
        stopwach = round(time.time() - startTime, 2)
        font = pygame.font.SysFont("comicsansms", 35, True, True)
        title = font.render("Time: " + str(stopwach), True, (255, 0, 0))
        screen.blit(title, (960, 30))

    # Text

    if not hasPressKey:
        # Game Name
        font = pygame.font.SysFont("comicsansms", 75, True, True)
        title = font.render("Maze Game", True, (255, 0, 0))
        screen.blit(title, (390, 50))

        # Start
        font = pygame.font.SysFont("comicsansms", 40, True, True)
        title = font.render("Start", True, (255, 0, 0))
        screen.blit(title, (110, 40))

        # End
        font = pygame.font.SysFont("comicsansms", 40, True, True)
        title = font.render("End", True, (255, 0, 0))
        screen.blit(title, (1012, 40))

        # Time best
        font = pygame.font.SysFont("comicsansms", 30, True, True)
        title = font.render("Best time: " + str(bestTime), True, (255, 0, 0))
        screen.blit(title, (390, 150))

        # Time current
        font = pygame.font.SysFont("comicsansms", 30, True, True)
        title = font.render("Current time: " + str(currentTime), True, (255, 0, 0))
        screen.blit(title, (390, 190))

    # Walls
    # top wall
    w1 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 0, 1200, 25))
    # left wall
    w2 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 0, 25, 900))
    # bottom wall
    w3 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 875, 1200, 25))
    # right wall
    w4 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(1175, 0, 25, 925))
    # Obstacle topLeft
    w5 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(300, 0, 25, 300))
    w6 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(300, 300, 350, 25))
    # middle line horizontal
    w7 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 500, 650, 25))
    # right vertical
    w8 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(900, 0, 25, 700))
    # bottom horizontal around
    w9 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(200, 700, 725, 25))

    # Collision
    if p1.colliderect(w1) or p1.colliderect(w2) or p1.colliderect(w3) or p1.colliderect(w4) or p1.colliderect(w5) \
            or p1.colliderect(w6) or p1.colliderect(w7) or p1.colliderect(w8) or p1.colliderect(w9):
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            y += 3
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            y -= 3
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            x += 3
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            x -= 3

    # End
    if p1.colliderect(end):

        x = 112
        y = 112
        endTime = time.time()
        print(endTime)
        hasPressKey = False
        currentTime = round(endTime - startTime, 2)
        if currentTime < bestTime or bestTime == 0:
            bestTime = currentTime
        level = 2
        hasTakenTime = False
        time.sleep(1)

def level2():
    global x, y, startTime, endTime, bestTime, currentTime, hasTakenTime, hasPressKey, clock, level
    x = 112
    y = 112

    startTime = 0
    endTime = 0

    bestTime = 0
    currentTime = 0

    hasPressKey = False
    hasTakenTime = False



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y -= 3
        hasPressKey = True
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y += 3
        hasPressKey = True
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x -= 3
        hasPressKey = True
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x += 3
        hasPressKey = True

    # Drawing
    screen.fill((0, 0, 0))
    end = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1000, 112, 100, 100))
    playerImage = pygame.image.load('player.png').convert()
    p1 = playerImage.get_rect()
    p1.x, p1.y = x, y
    screen.blit(playerImage, p1)
    p1 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, 100, 100))

    if hasPressKey and not hasTakenTime:
        startTime = time.time()
        print(startTime)
        hasTakenTime = True

    if hasPressKey:
        stopwach = round(time.time() - startTime, 2)
        font = pygame.font.SysFont("comicsansms", 35, True, True)
        title = font.render("Time: " + str(stopwach), True, (255, 0, 0))
        screen.blit(title, (960, 30))

    # # Text
    #
    if not hasPressKey:
        # Game Name
        font = pygame.font.SysFont("comicsansms", 75, True, True)
        title = font.render("Maze Game", True, (255, 0, 0))
        screen.blit(title, (390, 50))
        # # Start
        font = pygame.font.SysFont("comicsansms", 40, True, True)
        title = font.render("Start", True, (255, 0, 0))
        screen.blit(title, (110, 40))
        #
        # End
        font = pygame.font.SysFont("comicsansms", 40, True, True)
        title = font.render("End", True, (255, 0, 0))
        screen.blit(title, (1012, 40))

        ## Time best
        font = pygame.font.SysFont("comicsansms", 30, True, True)
        title = font.render("Best time: " + str(bestTime), True, (255, 0, 0))
        screen.blit(title, (390, 150))
        #
        # # Time current
        font = pygame.font.SysFont("comicsansms", 30, True, True)
        title = font.render("Current time: " + str(currentTime), True, (255, 0, 0))
        screen.blit(title, (390, 190))

    # Walls
    # top wall
    w1 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 0, 1200, 10))
    # left wall
    w2 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 0, 10, 900))
    # bottom wall
    w3 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 890, 1200, 10))
    # right wall
    w4 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(1190, 0, 10, 925))
    # under
    w5 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 175, 550, 10))
    # middle
    w6 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(800, 0, 10, 745))

    w7 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(0, 325, 275, 10))

    w8 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(475, 325, 185, 10))

    w9 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(615, 575, 190, 10))

    w10 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(615, 450, 10, 300))

    w11 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(475, 325, 10, 425))

    w12 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(175, 475, 300, 10))

    w13 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(150, 650, 175, 10))

    w14 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(325, 650, 10, 425))

    w15 = pygame.draw.rect(screen, (105, 139, 105), pygame.Rect(1000, 150, 10, 745))




    Collision
    if p1.colliderect(w1) or p1.colliderect(w2) or p1.colliderect(w3) or p1.colliderect(w4) or p1.colliderect(w5) \
            or p1.colliderect(w6) or p1.colliderect(w7) or p1.colliderect(w8) or p1.colliderect(w9):
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            y += 3
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            y -= 3
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            x += 3
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            x -= 3

    # End
    if p1.colliderect(end):
    #
        x = 112
        y = 112
        endTime = time.time()
        print(endTime)
        hasPressKey = False
        currentTime = round(endTime - startTime, 2)
        if currentTime < bestTime or bestTime == 0:
            bestTime = currentTime
        level = 2
        hasTakenTime = False
        time.sleep(1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move Player
    if level == 1:
        level1()

    pygame.display.flip()
    clock.tick(60)
