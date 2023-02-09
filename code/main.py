from initialize import initialize_colour_palette, initialize_difficulty_list, initialize_display_size, \
    initialize_font_path
from display import display_title_page, display_difficulty_page

import pygame


def run_game_sequence(display):
    colour_palette = initialize_colour_palette()
    difficulty_list = initialize_difficulty_list()
    font_path = initialize_font_path("FFFFORWARD.TTF")
    quit = False

    quit = display_title_page(display, font_path, colour_palette)
    if quit:
        return

    difficulty = display_difficulty_page(display, font_path, colour_palette, difficulty_list)
    if difficulty == "QUIT":
        return

    print(difficulty)


def primary():
    screen_width, screen_height = initialize_display_size()

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    run_game_sequence(display)
    pygame.quit()


if __name__ == "__main__":
    primary()
