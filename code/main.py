from initialize import initialize_display_size, initialize_font_path

import pygame


class DifficultyButton:
    def __init__(self, x: int, y: int, width: int, height: int, font_path: str, text_name: str, text_dimensions: str,
                 text_mines: str, subtext_single_row: bool = False):
        self._x_coordinate = x
        self._y_coordinate = y
        self._width = width
        self._height = height
        self._font_path = font_path
        self._text_name = text_name
        self._text_dimensions = text_dimensions
        self._text_mines = text_mines
        self._subtext_single_row = subtext_single_row

    def draw_rectangle(self, display, colour_palette: dict):
        pygame.draw.rect(display, colour_palette["white"],
                         [self._x_coordinate, self._y_coordinate, self._width, self._height], 5)

        dual_row_multiplier = 0
        text_x = int(self._width // 2) + self._x_coordinate
        text_y = int(self._height // 3) + self._y_coordinate
        if self._subtext_single_row:
            text_y = int(self._height // 2.5) + self._y_coordinate
        if not self._subtext_single_row:
            dual_row_multiplier = 0.1

        text, text_boundaries = draw_text(self._text_name, text_x, text_y, colour_palette["white"], self._font_path,
                                          int((10 / 36) * self._width / (int(len(self._text_name) / 4) + 1)))
        display.blit(text, text_boundaries)

        k = len(self._text_mines)
        if self._subtext_single_row:
            k += len(self._text_dimensions)
            x_u = int(((3 * self._width * k) - (6 * self._width)) / (8 * k)) + self._x_coordinate - (
                        (1 / 10) * self._width)
            text_x = x_u

        text_y = int(self._height // (1.35 + (2.5*dual_row_multiplier))) + self._y_coordinate
        text_size = int((16 / 36) * self._width / (int(k / 2) + 1))

        text, text_boundaries = draw_text(self._text_dimensions, text_x, text_y, colour_palette["white"], self._font_path,
                                          text_size)
        display.blit(text, text_boundaries)

        if self._subtext_single_row:
            x_v = int(((18 * self._width) + (11 * self._width * k)) / (24 * k)) + self._x_coordinate + (
                        (1 / 5) * self._width)
            text_x = x_v

        text_y = int(self._height // (1.35 - (1.5*dual_row_multiplier))) + self._y_coordinate
        text, text_boundaries = draw_text(self._text_mines, text_x, text_y, colour_palette["white"], self._font_path,
                                          text_size)
        display.blit(text, text_boundaries)
        # '''

    def collision(self, click_x: int, click_y: int):
        if click_x < self._x_coordinate or click_x > (self._x_coordinate + self._width):
            return False
        if click_y < self._y_coordinate or click_y > (self._y_coordinate + self._height):
            return False

        return True

    @property
    def text_name(self):
        return self._text_name


def draw_text(text: str, x_coordinate: int, y_coordinate: int, colour: tuple, font_path: str, size: int):
    font = pygame.font.Font(font_path, size)
    text = font.render(text, True, colour)
    text_boundaries = text.get_rect()
    text_boundaries.center = (x_coordinate, y_coordinate)
    return text, text_boundaries


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


def display_difficulty_page(display, font_path, colour_palette: dict):
    display.fill(colour_palette["dark gray"])
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

    difficulty_button_series = [
        DifficultyButton(rectangle_gap, rectangle_gap, rectangle_width, rectangle_height, font_path, "Easy", "9 x 9",
                         "10 mines", bool(dual_row)),
        DifficultyButton(rectangle_width + 2 * rectangle_gap, rectangle_gap, rectangle_width, rectangle_height,
                         font_path, "Medium", "16 x 16", "40 mines", bool(dual_row)),
        DifficultyButton(dual_row_x + rectangle_gap, dual_row_y + rectangle_gap, rectangle_width, rectangle_height,
                         font_path, "Hard", "30 x 16", "99 mines", bool(dual_row)),
        DifficultyButton(dual_row_x + rectangle_width + 2 * rectangle_gap, dual_row_y + rectangle_gap, rectangle_width,
                         rectangle_height, font_path, "Extreme", "30 x 24", "180 mines", bool(dual_row))
    ]

    while True:
        for rectangle in difficulty_button_series:
            rectangle.draw_rectangle(display, colour_palette)

        pygame.display.update()

        event = pygame.event.wait()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for rectangle in difficulty_button_series:
                if rectangle.collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return rectangle.text_name
        if event.type == pygame.QUIT:
            return "QUIT"


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
