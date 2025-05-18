import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player_1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    player_1.add(drawable, updateable)
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # fps = 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()