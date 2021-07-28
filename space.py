import pygame
import sys
import random
from time import sleep
from pygame.locals import *
from spaceship import *


pygame.init()


display_height = 480
display_width = 640

pygame.init()

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.display.set_caption("Space Invaders")

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 150)
red = (150, 0, 0)
green = (0, 150, 0)
bright_green = (255, 0, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

font = pygame.font.SysFont("Jokerman", 30)
largeText = pygame.font.SysFont("Comic Sans MS", 115)
mediumText = pygame.font.SysFont("Times", 20)
decorateText = pygame.font.SysFont("Jokerman", 40)
background = pygame.image.load("space.jpg")
