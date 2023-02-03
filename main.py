import pygame
pygame.init()

#Color, caption and logo
background_colour = (1,1,1)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')
screen.fill(background_colour)
pygame.display.flip()

#player image addition
player=pygame.image.load('player.png')
playerX=370
playerY=460

#player unction to display the image
def playerImg(x,y):
  screen.blit(player, (x, y))


icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)
running = True
while running:
  playerX += 0.1
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


  playerImg(playerX, playerY)
  pygame.display.update()