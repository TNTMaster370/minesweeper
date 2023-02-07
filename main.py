import pygame
import ctypes
import os


def initialize_font_path(desired_font: str):
    for root, dirs, files in os.walk("C:\\"):
        for name in files:
            if name == desired_font:
                return os.path.abspath(os.path.join(root, name))
    raise FileNotFoundError


def display_title_page(display, font_path, colour_palette: dict):
    display_ratio = display.get_width() / display.get_height()

    text_size_list = [int(display_ratio*((1/15)*display.get_width())), int(display_ratio*((1/29)*display.get_width())),
                      int(display_ratio*((1/25)*display.get_width()))]
    text_y_coord_list = [int(0.34375*display.get_height()), int(0.48625*display.get_height()),
                         int(0.65625*display.get_height())]
    text_actual_list = ["Minesweeper", "Created by TNTMaster370", "Press any button to start"]

    display.fill(colour_palette["dark gray"])

    for size, y_coord, text_actual in zip(text_size_list, text_y_coord_list, text_actual_list):
        font = pygame.font.Font(font_path, size)
        text = font.render(text_actual, True, colour_palette["white"])
        text_boundaries = text.get_rect()
        text_boundaries.center = (display.get_width() // 2, y_coord)
        display.blit(text, text_boundaries)

    pygame.display.update()

    while True:
        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            return False
        if event.type == pygame.QUIT:
            return True


def primary():
    user_screen = ctypes.windll.user32
    monitor_width = user_screen.GetSystemMetrics(0)
    monitor_height = user_screen.GetSystemMetrics(1)

    screen_width = (1/2) * monitor_width
    if screen_width < (4/5) * monitor_height:
        screen_height = screen_width
    else:
        screen_height = (2/3) * monitor_height

    font_path = initialize_font_path("FFFFORWARD.TTF")

    colour_palette = {
        "red": (),
        "orange": (),
        "yellow": (),
        "green": (),
        "blue": (),
        "purple": (),
        "white": (255, 255, 255),
        "dark gray": (63, 63, 63),
        "black": (0, 0, 0)
    }

    quit = False

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    quit = display_title_page(display, font_path, colour_palette)


if __name__ == "__main__":
    primary()
