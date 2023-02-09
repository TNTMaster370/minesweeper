from DifficultyButton import DifficultyButton
from draw import draw_text

import pygame


def display_title_page(display, font_path, colour_palette: dict):
    display_ratio = display.get_width() / display.get_height()

    text_size_list = [int(display_ratio * ((1 / 15) * display.get_width())),
                      int(display_ratio * ((1 / 29) * display.get_width())),
                      int(display_ratio * ((1 / 25) * display.get_width()))]
    text_y_coord_list = [int(0.34375 * display.get_height()), int(0.48625 * display.get_height()),
                         int(0.65625 * display.get_height())]
    text_actual_list = ["Minesweeper", "Created by TNTMaster370", "Press any button to start"]

    display.fill(colour_palette["dark gray"])

    for size, y_coord, text_actual in zip(text_size_list, text_y_coord_list, text_actual_list):
        text, text_boundaries = draw_text(text_actual, display.get_width() // 2, y_coord, colour_palette["white"],
                                          font_path, size)
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


def display_difficulty_page(display, font_path, colour_palette: dict, difficulty_list: dict):
    display.fill(colour_palette["dark gray"])
    difficulty_button_series = []
    rectangle_gap = int((1 / 25) * display.get_width())

    dual_row = 0
    dual_row_multiplier = 0
    if 3 * display.get_height() >= 2 * display.get_width():
        dual_row = 1
        dual_row_multiplier = 6 / 25

    rectangle_width = int(((5 / 25) + dual_row_multiplier) * display.get_width())
    rectangle_height = int(((1 / 3) - (dual_row_multiplier / 3)) * display.get_height())
    dual_row_x = (1 - dual_row) * (2 * rectangle_width + 2 * rectangle_gap)
    dual_row_y = dual_row * (rectangle_height + rectangle_gap)

    x_list = [
        rectangle_gap, (rectangle_width + 2*rectangle_gap), (dual_row_x + rectangle_gap),
        (dual_row_x + rectangle_width + 2*rectangle_gap)
    ]
    y_list = [
        rectangle_gap, rectangle_gap, (dual_row_y + rectangle_gap), (dual_row_y + rectangle_gap)
    ]

    for index, key in enumerate(difficulty_list):
        difficulty_button_series.append(
            DifficultyButton(x_list[index], y_list[index], rectangle_width, rectangle_height, font_path,
                             key, f"{difficulty_list[key][0]} x {difficulty_list[key][1]}",
                             f"{difficulty_list[key][2]} mines", bool(dual_row))
        )

    while True:
        for rectangle in difficulty_button_series:
            rectangle.draw_rectangle(display, colour_palette)

        pygame.display.update()

        event = pygame.event.wait()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rectangle in difficulty_button_series:
                if rectangle.collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return False, rectangle.text_name
        if event.type == pygame.QUIT:
            return True, ""
