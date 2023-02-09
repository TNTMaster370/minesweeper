from initialize import initialize_colour_palette, initialize_difficulty_list, initialize_display_size, \
    initialize_font_path
from display import display_title_page, display_difficulty_page

import pygame


def primary():
    screen_width, screen_height = initialize_display_size()
    font_path = initialize_font_path("FFFFORWARD.TTF")
    colour_palette = initialize_colour_palette()
    difficulty_list = initialize_difficulty_list()

    quit = False

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    quit = display_title_page(display, font_path, colour_palette)
    if quit:
        return

    difficulty = display_difficulty_page(display, font_path, colour_palette, difficulty_list)
    if difficulty == "QUIT":
        return

    print(difficulty)


if __name__ == "__main__":
    primary()
