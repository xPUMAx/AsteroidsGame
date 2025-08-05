import pygame
from constants import *

pygame.font.init()  # Initialize the font module

# Game font variables
title_font = pygame.font.Font(None, SCREEN_HEIGHT // 5)  # Create a font object for the title
author_font = pygame.font.Font(None, SCREEN_HEIGHT // 15)  # Create a font object for the subtitle
instructions_font = pygame.font.Font(None, SCREEN_HEIGHT // 20)  # Create a font object for instructions
score_font = pygame.font.Font(None, SCREEN_HEIGHT // 30)  # Create a font object for the score
end_score_font = pygame.font.Font(None, SCREEN_HEIGHT // 15)  # Create a font object for the end score
gameover_font = pygame.font.Font(None, SCREEN_HEIGHT // 10)  # Create a font object for the game over text

# Game text rendering and display functions
def render_title(screen):
    title_text = title_font.render(TITLE_TEXT, True, (255, 255, 255))
    screen.blit(title_text, (get_text_horizontal_center_position(title_text), SCREEN_HEIGHT // 5))

def render_author(screen):
    author_text = author_font.render(AUTHOR_TEXT, True, (255, 255, 255))
    screen.blit(author_text, (get_text_horizontal_center_position(author_text), (SCREEN_HEIGHT // 5) * 2 - author_text.get_height()))

def render_gameover(screen):
    gameover_text = gameover_font.render(GAMEOVER_TEXT, True, (255, 0, 0))
    screen.blit(gameover_text, (get_text_horizontal_center_position(gameover_text), SCREEN_HEIGHT // 3))

def render_score(screen, score):
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Display score at the top-left corner

def render_end_score(screen, score):
    end_score_text = end_score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(end_score_text, (get_text_horizontal_center_position(end_score_text), (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 5)))

def render_instructions(screen):
    instructions_text = instructions_font.render(INSTRUCTIONS_TEXT, True, (255, 255, 255))
    screen.blit(instructions_text, (get_text_horizontal_center_position(instructions_text), SCREEN_HEIGHT - 20 - instructions_text.get_height()))

def render_exit(screen):
    exit_text = instructions_font.render(EXIT_TEXT, True, (255, 255, 255))
    screen.blit(exit_text, (get_text_horizontal_center_position(exit_text), SCREEN_HEIGHT - 20 - exit_text.get_height()))

def get_text_horizontal_center_position(text):
    return (SCREEN_WIDTH // 2 - text.get_width() // 2)