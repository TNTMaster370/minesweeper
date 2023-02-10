from initialize import initialize_colour_palette, initialize_difficulty_list, initialize_display_size, \
    initialize_font_path
from display import display_title_page, display_difficulty_page, display_game_page

import pygame


def run_game_sequence(display, clock):
    colour_palette = initialize_colour_palette()
    difficulty_list = initialize_difficulty_list()
    font_path = initialize_font_path("FFFFORWARD.TTF")

    quit_game = display_title_page(display, font_path, colour_palette)
    if quit_game:
        return

    quit_game, difficulty = display_difficulty_page(display, font_path, colour_palette, difficulty_list)
    if quit_game:
        return

    quit_game = display_game_page(display, clock, font_path, colour_palette, difficulty_list, difficulty)
    if quit_game:
        return


def primary():
    screen_width, screen_height = initialize_display_size()

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    run_game_sequence(display, clock)
    pygame.quit()


if __name__ == "__main__":
    primary()
