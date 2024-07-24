import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 80
PLAYER_SPEED = 5
PLAYER_COLOR = (255, 0, 0)
ROAD_WIDTH = 200
ROAD_COLOR = (50, 50, 50)
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 30
OBSTACLE_COLOR = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Road Rash Game")

player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 20

road_x = (SCREEN_WIDTH - ROAD_WIDTH) // 2

obstacles = []

clock = pygame.time.Clock()

def create_obstacle():
    obstacle_x = random.randint(road_x, road_x+ROAD_WIDTH)
    obstacle_y = 0
    obstacles.append((obstacle_x, obstacle_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED

    player_x = max(0, min(player_x, SCREEN_WIDTH - PLAYER_WIDTH))

    if road_x > SCREEN_WIDTH:
        road_x = 0
        
    if random.randint(1, 100) < 2:
        create_obstacle()
        
    for i, (obstacle_x, obstacle_y) in enumerate(obstacles):
        obstacles[i] = (obstacle_x, obstacle_y + 5)
        
    obstacles = [(x, y) for x, y in obstacles if y < SCREEN_HEIGHT]

    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for obstacle_x, obstacle_y in obstacles:
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        if player_rect.colliderect(obstacle_rect):
            running = False 

    screen.fill(WHITE)

    pygame.draw.rect(screen, ROAD_COLOR, (road_x, 0, ROAD_WIDTH, SCREEN_HEIGHT))

    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    for obstacle_x, obstacle_y in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
