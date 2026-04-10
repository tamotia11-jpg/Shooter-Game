import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (220, 50, 50)
BLUE  = (50, 100, 220)

clock = pygame.time.Clock()
FPS = 60

# Player
player = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 60, 40, 40)
player_speed = 5

bullets = []
bullet_speed = 8

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    pygame.display.flip()

def main():
    running = True
    shoot_cooldown = 0

    while running:
        clock.tick(FPS)
        shoot_cooldown = max(0, shoot_cooldown - 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed
        if keys[pygame.K_SPACE] and shoot_cooldown == 0:
            bullet = pygame.Rect(player.centerx - 3, player.top - 10, 6, 14)
            bullets.append(bullet)
            shoot_cooldown = 15

        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        draw()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
