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
    title_font = pygame.font.Font(None, SCREEN_HEIGHT // 5)  # Create a font object for the title
    author_font = pygame.font.Font(None, SCREEN_HEIGHT // 15)  # Create a font object for the subtitle
    score_font = pygame.font.Font(None, SCREEN_HEIGHT // 30)  # Create a font object for the score
    end_score_font = pygame.font.Font(None, SCREEN_HEIGHT // 15)  # Create a font object for the end score
    gameover_font = pygame.font.Font(None, SCREEN_HEIGHT // 10)  # Create a font object for the game over text
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
            elif event.type == pygame.KEYDOWN:
                show_title = False  # Hide the title screen when a key is pressed

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
                        render_score(screen, score_font, player_score)  # Update the score display
                        asteroid.kill()
                        shot.kill()

            # Check for collisions with the player, end game if collision occurs
            if object.check_collision(player) and (object != player and not isinstance(object, Shot)):
                show_gameover = True  # Show game over screen
                player.kill()

        #DISPLAY GAME TEXT
        if show_title:
            # Display the title screen
            render_title(screen, title_font)
            render_author(screen, author_font)
        elif show_gameover:
            # Display the game over screen
            render_gameover(screen, gameover_font)
            render_end_score(screen, end_score_font, player_score)
        else: 
            render_score(screen, score_font, player_score)  # Draw the score text

        pygame.display.flip()  # Update the display   


if __name__ == "__main__":
    main()
