import os
os.environ['SDL_VIDEODRIVER_WINDOW_POS'] = '0, 0'  # initialize the window in the center
import pygame
from constants import *
from gametext import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize all imported pygame modules
    pygame.font.init()  # Initialize the font module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    pygame.display.set_caption("Asteroids Game")  # Set the window title

    #INITIALIZE GAME VARIABLES

    player_score  = 0  # Initialize player score  
    
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

    running = True
    show_title = True  # Flag to show the title screen
    show_gameover = False  # Flag to show the game over screen

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Quit the game
            
            if event.type == pygame.KEYDOWN:
                show_title = False  # Hide the title screen when a key is pressed
                if event.key == pygame.K_ESCAPE:
                    return  # Exit the game if ESC is pressed
                if event.key == pygame.K_RETURN and show_gameover:
                    # restart game
                    player_score = 0
                    show_gameover = False
                    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    asteroidfield.kill()  # Remove the old asteroid field
                    for asteroid in asteroids:
                        asteroid.kill()
                    asteroidfield = AsteroidField()

        dt = gameClock.tick(60)/1000  # Limit the frame rate to 60 FPS and returns seconds to delta time
        screen.fill((0, 0, 0))  # Fill the screen with black

        updateable.update(dt)  # Update the player
        for object in drawable:
            object.draw(screen)  # Draw objects on the screen

            # Check for shot collisions with asteroids
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.check_collision(shot):
                        asteroid.split()  # Split the asteroid if it is hit
                        player_score += asteroid.point_value()  # Increase player score
                        render_score(screen, player_score)  # Update the score display
                        asteroid.kill()
                        shot.kill()

            # Check for collisions with the player, end game if collision occurs
            if object.check_collision(player) and (object != player and not isinstance(object, Shot) and not show_title):
                show_gameover = True  # Show game over screen
                player.kill()

        #DISPLAY GAME TEXT
        if show_title: # Display the title screen
            render_title(screen)
            render_author(screen)
            render_instructions(screen)
        elif show_gameover: # Display the game over screen
            render_gameover(screen)
            render_end_score(screen, player_score)
            render_exit(screen)
            render_restart(screen)
        else:  # Draw the score text
            render_score(screen, player_score)

        pygame.display.flip()  # Update the display   


if __name__ == "__main__":
    main()
