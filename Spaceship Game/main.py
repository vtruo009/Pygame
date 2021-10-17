import pygame
import os # gonna use osfs for file system
pygame.init()

x = 50
y = 50
VEL = 5
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55, 40)

# Load spaceship
YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Spaceship Game/Assets', 'spaceship_yellow.png'))
# Scale spaceship
YELLOW_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Spaceship Game/Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMG, (yellow.x, yellow.y)) # use blit to draw text/images on the screen
    WIN.blit(RED_SPACESHIP_IMG, (red.x, red.y))
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: # Left
            yellow.x -= VEL
    if keys_pressed[pygame.K_d]: # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w]: # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]: # Down
        yellow.y += VEL

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: # Left
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP]: # Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]: # Down
        red.y += VEL

def main():
    # Rect(x, y, width, height)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # Want to use this to control game so the running speed will be the same no matter what machine
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
