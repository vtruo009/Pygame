import pygame
import os # gonna use osfs for file system
pygame.init()

x = 50
y = 50
VEL = 5
BULLET_VEL = 7
MAX_NUM_BULLETS = 3
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55, 40)
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# Load spaceship
YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('SpaceshipGame/Assets', 'spaceship_yellow.png'))
# Scale spaceship
YELLOW_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('SpaceshipGame/Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMG = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER) # Draw a black rectangle on this window
    WIN.blit(YELLOW_SPACESHIP_IMG, (yellow.x, yellow.y)) # use blit to draw text/images on the screen
    WIN.blit(RED_SPACESHIP_IMG, (red.x, red.y))
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL >= 0: # Left
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width <= BORDER.x: # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL >= 0: # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height <= HEIGHT - 15: # Down
        yellow.y += VEL

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL >= BORDER.x + BORDER.width: # Left was border.x + 10
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width <= WIDTH: # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL >= 0: # Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height <= HEIGHT - 15: # Down
        red.y += VEL

def main():
    # Rect(x, y, width, height)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # Want to use this to control game so the running speed will be the same no matter what machine
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(yellow_bullets) < MAX_NUM_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_SPACE and len(red_bullets) < MAX_NUM_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
