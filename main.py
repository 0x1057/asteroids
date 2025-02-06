import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ticker = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()

    # static constainers fields to organize objects and what we do to them
    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    

    player_ship = Player(x, y)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # clear the screen
        screen.fill("black")
        
        # update player state
        updatable.update(dt)
        for an_asteroid in all_asteroids:
           if an_asteroid.collision_check(player_ship):
               print("Game over!")
               return

        # draw everything
        for item in drawable:
            item.draw(screen)

        # update display
        pygame.display.flip()

        # handling timing
        ticker.tick(60)
        dt = ticker.get_time() / 1000

if __name__ == "__main__":
    main()