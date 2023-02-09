from initialize import initialize_display_size, initialize_font_path
from display import display_title_page, display_difficulty_page

import pygame


def primary():
    screen_width, screen_height = initialize_display_size()
    font_path = initialize_font_path("FFFFORWARD.TTF")

    colour_palette = {
        "red":       (245, 65,  65),
        "orange":    (),
        "yellow":    (),
        "green":     (),
        "blue":      (),
        "purple":    (),
        "white":     (255, 255, 255),
        "dark gray": (63,  63,  63),
        "black":     (0,   0,   0)
    }

    difficulty_list = {
        "Easy":    (9,  9,  10),
        "Medium":  (16, 16, 40),
        "Hard":    (30, 16, 99),
        "Extreme": (30, 24, 180)
    }

    quit = False

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    quit = display_title_page(display, font_path, colour_palette)
    if quit:
        return

    difficulty = display_difficulty_page(display, font_path, colour_palette)
    if difficulty == "QUIT":
        return

    print(difficulty)


if __name__ == "__main__":
    primary()
