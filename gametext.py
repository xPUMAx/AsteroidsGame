import pygame
from constants import *

# Game text rendering and display functions
def render_title(screen, font):
    title_text = font.render(TITLE_TEXT, True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 5))

def render_author(screen, font):
    author_text = font.render(AUTHOR_TEXT, True, (255, 255, 255))
    screen.blit(author_text, (SCREEN_WIDTH // 2 - author_text.get_width() // 2, (SCREEN_HEIGHT // 5) * 2))

def render_gameover(screen, font):
    gameover_text = font.render(GAMEOVER_TEXT, True, (255, 0, 0))
    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, SCREEN_HEIGHT // 3))

def render_score(screen, font, score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Display score at the top-left corner

def render_end_score(screen, font, score):
    end_score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(end_score_text, (SCREEN_WIDTH // 2 - end_score_text.get_width() // 2, (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 5)))