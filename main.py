# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
os.environ['SDL_VIDEODRIVER_WINDOW_POS'] = '0, 0'  # initialize the window in the center
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    pygame.display.set_caption("Asteroids Game")  # Set the window title

    gameClock = pygame.time.Clock()
    dt = 0  # Initialize delta time
    updateable = pygame.sprite.Group()  # Initialize sprite group for updateable objects
    drawable = pygame.sprite.Group()  # Initialize sprite group for drawable objects
    asteroids = pygame.sprite.Group()  # Initialize sprite group for asteroids
    shots = pygame.sprite.Group()  # Initialize sprite group for shots
    Player.containers = (updateable, drawable)  # Set the containers for Player class
    Shot.containers = (shots, drawable, updateable)  # Set the containers for Shot class
    Asteroid.containers = (asteroids, updateable, drawable)  # Set the containers for Asteroid class
    AsteroidField.containers = (updateable)  # Create an asteroid field instance

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Create a player instance
    asteroidfield = AsteroidField()  # Create an asteroid field instance

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gameClock.tick(60)/1000  # Limit the frame rate to 60 FPS and returns seconds to delta time
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        updateable.update(dt)  # Update the player
        for object in drawable:
            object.draw(screen)  # Draw objects on the screen

            # Check for shot collisions with asteroids
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.check_collision(shot):
                        asteroid.kill()
                        shot.kill()

            # Check for collisions with the player, end game if collision occurs
            if object.check_collision(player) and (object != player and not isinstance(object, Shot)):
                print("Game Over!")
                return

        pygame.display.flip()  # Update the display   


if __name__ == "__main__":
    main()
