import pygame
import os

from pygame import Vector2, key
from pygame.constants import K_DOWN, K_SCROLLLOCK, K_UP, KEYDOWN, K_s, K_u, K_w
pygame.init()

WHITE = (255, 255, 255)
BLUE_GREY = (97, 124, 141)
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 300
FPS = 60
VEL = 10



# Setup game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

def draw_window(paddleA, paddleB, ball):
    WIN.fill(BLUE_GREY)

    pygame.draw.rect(WIN, WHITE, paddleA)
    pygame.draw.rect(WIN, WHITE, paddleB)
    pygame.draw.rect(WIN, WHITE, ball)

    pygame.display.update()

def handle_paddleA(keys_pressed, left_paddle):
    if keys_pressed[K_w] and left_paddle.y - VEL > 0:
        left_paddle.y -= VEL
    if keys_pressed[K_s] and left_paddle.y + VEL + PADDLE_HEIGHT < HEIGHT:
        left_paddle.y += VEL


def handle_paddleB(keys_pressed, right_paddle):
    if keys_pressed[K_UP] and right_paddle.y - VEL > 0:
        right_paddle.y -= VEL
    if keys_pressed[K_DOWN] and right_paddle.y + VEL + PADDLE_HEIGHT < HEIGHT:
        right_paddle.y += VEL

def main():
    left_paddle = pygame.Rect(0,HEIGHT/2 - 150, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 20, HEIGHT/2 - 150, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH/2 - 12, HEIGHT/2 - 12, 24, 24)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_paddleA(keys_pressed, left_paddle)
        handle_paddleB(keys_pressed, right_paddle)
        draw_window(left_paddle, right_paddle, ball)
        

if __name__ == '__main__':
    main()