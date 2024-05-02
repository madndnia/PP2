import pygame
from datetime import datetime

pygame.init() 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load(r"C:\Users\Madina\Desktop\python1\Lab7\mickey-clock.jpg")
BG_WIDTH = 500
BG_HEIGHT = 500
BG_X_POS = (SCREEN_WIDTH / 2 - BG_WIDTH / 2)
BG_Y_POS = (SCREEN_HEIGHT / 2 - BG_HEIGHT / 2)

big_arrow = pygame.image.load(r"C:\Users\Madina\Desktop\python1\Lab7\big-arrow.png")
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.13
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pygame.transform.scale(big_arrow, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

# i modified it
small_arrow = pygame.image.load(r"C:\Users\Madina\Desktop\python1\Lab7\small-arrow.png")
SMALL_ARROW_WIDTH = 45
SMALL_ARROW_ASPECT_RATIO = 0.3
SMALL_ARROW_HEIGHT = SMALL_ARROW_WIDTH / SMALL_ARROW_ASPECT_RATIO
small_arrow = pygame.transform.scale(small_arrow, (SMALL_ARROW_WIDTH, SMALL_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER

#i modified it
small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = CENTER

running = True
while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  angle_m = datetime.now().minute * -6
  angle = datetime.now().second * -6
# Clear the screen and draw background
  screen.fill(WHITE)
  screen.blit(bg, (BG_X_POS, BG_Y_POS))

# Draw and rotate the big arrow
  rotated_big_arrow = pygame.transform.rotate(big_arrow, angle)
  rotated_big_arrow_rect = rotated_big_arrow.get_rect()
  rotated_big_arrow_rect.center = big_arrow_rect.center
  screen.blit(rotated_big_arrow, rotated_big_arrow_rect)

# Draw and rotate the small arrow
  rotated_small_arrow = pygame.transform.rotate(small_arrow, angle_m)
  rotated_small_arrow_rect = rotated_small_arrow.get_rect()
  rotated_small_arrow_rect.center = small_arrow_rect.center
  screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

# Screen updating
  pygame.display.flip()
  clock.tick(FPS)




