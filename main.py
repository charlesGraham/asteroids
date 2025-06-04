import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # grouping sprites
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.containers = (updateable, drawable)

    # add player to the drawable and updateable groups
    drawable.add(player)
    updateable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            screen.fill("black")

            for item in drawable:
                item.draw(screen)

            updateable.update(dt)

            pygame.display.flip()
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
