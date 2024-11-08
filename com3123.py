
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

pastel_colors = [
    (255, 182, 193),
    (255, 218, 185),
    (173, 216, 230),
