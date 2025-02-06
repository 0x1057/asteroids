import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ticker = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_ship = Player(x, y)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # clear the screen
        screen.fill("black")

        # draw everything
        player_ship.draw(screen)

        # update display
        pygame.display.flip()

        # handling timing
        ticker.tick(60)
        dt = ticker.get_time() / 1000

if __name__ == "__main__":
    main()