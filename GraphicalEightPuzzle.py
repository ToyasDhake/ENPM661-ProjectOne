import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from itertools import product

pygame.init()
dis = pygame.display.set_mode((900, 900))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)
ticks = 400

run = True
clock = pygame.time.Clock()
gameBoard = [[1, 8, 2], [4, 0, 3], [7, 6, 5]]
newBoard =  [[1, 8, 2], [4, 6, 3], [7, 0, 5]]


def populate(gameBoard):
    for i, j in product(range(3), range(3)):
        if gameBoard[i][j] is not 0:
            pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(j*300+10, i*300+10, 280, 280))
            textsurface = myfont.render(str(gameBoard[i][j]), False, (0, 0, 0))
            dis.blit(textsurface, (j*300+125, i*300+125))

def getLocationOfBlank(gameBoard):
    for i, j in product(range(3), range(3)):
        if gameBoard[i][j] is 0:
            return i, j

def animate(prevGameBoard, newGameBoard):
    xVel, yVel = 0, 0
    prevX, prevY = getLocationOfBlank(prevGameBoard)
    newX, newY = getLocationOfBlank(newGameBoard)
    if prevX < newX:
        yVel = -1
    elif prevX > newX:
        yVel = 1
    elif prevY < newY:
        xVel = -1
    elif prevY > newY:
        xVel = 1
    for count in range(300):
        dis.fill((0, 0, 0))
        for i, j in product(range(3), range(3)):
            if prevGameBoard[i][j] is not 0:
                if i is newX and j is newY:
                    pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(j * 300 + 10 + (xVel * count), i * 300 + 10 + (yVel * count), 280, 280))
                    textsurface = myfont.render(str(prevGameBoard[i][j]), False, (0, 0, 0))
                    dis.blit(textsurface, (j * 300 + 125 + (xVel * count), i * 300 + 125 + (yVel * count)))
                else:
                    pygame.draw.rect(dis, (255, 255, 255), pygame.Rect(j*300+10, i*300+10, 280, 280))
                    textsurface = myfont.render(str(prevGameBoard[i][j]), False, (0, 0, 0))
                    dis.blit(textsurface, (j*300+125, i*300+125))
        pygame.display.flip()
        clock.tick(ticks)



animate(gameBoard, newBoard)

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     dis.fill((0, 0, 0))
#     animate(gameBoard, newBoard)
#     pygame.display.flip()
#     clock.tick(60)

pygame.quit()