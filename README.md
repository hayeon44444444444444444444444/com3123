## com3123 com3123
com3123com3123

import pygame파이게임 가져오기
import time가져오기 시간
import random무작위 가져오기

pygame.init()pygame.init ()

white = (255, 255, 255)흰색 = (255, 255, 255)
black = (0, 0, 0)black = (0, 0, 0)
blue = (50, 153, 213)파란색 = (50, 153, 213)

dis_width = 600dis_width = 600
dis_height = 400dis_높이 = 400
dis = pygame.display.dis = pygame.display.set_mode((dis_width, dis_height))set_mode(((dis_width, dis_high))
pygame.display.pygame.display.set_caption('Snake Game')set_caption('뱀 게임')

clock = pygame.time.clock = pygame.time.Clock()시계()
snake_block = 10스네이크_블록 = 10
snake_speed = 15스네이크_스피드 = 15

font_style = pygame.font.font_style = pygame.font.SysFont("bahnschrift", 25)SysFont("bahnschrift", 25)
score_font = pygame.font.score_font = 파이게임.font.SysFont("comicsansms", 35)SysFont("코믹센스", 35)

pastel_colors = [파스텔_colors = [
    (255, 182, 193),    (255, 182, 193),
    (255, 218, 185),    (255, 218, 185),
    (173, 216, 230),    (173, 216, 230),
