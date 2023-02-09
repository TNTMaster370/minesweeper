from draw import draw_text

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
        self._subtext_single_row = subtext_single_row  # subtext_single_row is a boolean for whether the subtext
        # of the button ("X x Y" and "Z mines") are parallel to each other, or are drawn on different lines with
        # separate y-coordinates. True means that the two texts are on the same y-coordinate.

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

        text_length = len(self._text_mines)
        if self._subtext_single_row:
            text_length += len(self._text_dimensions)
            text_x = int((((7*self._width*text_length) + (24*self._width)) / (40*text_length)) + self._x_coordinate)
            #           7wt + 24w       ; where w is the width, t is the length of the text, and
            # text_x =  --------- + x'  ; x' is the x-coordinate of the top-left corner of the
            #              40t          ; rectangle being drawn on. Equation is rounded down to
            #                           ; the ones place.

        text_y = int(self._height // (1.35 + (2.5 * dual_row_multiplier))) + self._y_coordinate
        text_size = int((16 / 36) * self._width / (int(text_length / 2) + 1))

        text, text_boundaries = draw_text(self._text_dimensions, text_x, text_y, colour_palette["white"],
                                          self._font_path,
                                          text_size)
        display.blit(text, text_boundaries)

        if self._subtext_single_row:
            text_x = (((79*text_length*self._width) + (90*self._width)) / (120*text_length)) + self._x_coordinate
            #          79tw + 90w       ; where x is the width, t is the length of the text, and
            # text_x = ---------- + x'  ; x' is the x-coordinate of the top-left corner of the
            #             120t          ; rectangle being drawn on. Equation is rounded down to
            #                           ; the ones place.

        text_y = int(self._height // (1.35 - (1.5 * dual_row_multiplier))) + self._y_coordinate

        text, text_boundaries = draw_text(self._text_mines, text_x, text_y, colour_palette["white"], self._font_path,
                                          text_size)
        display.blit(text, text_boundaries)

    def collision(self, click_x: int, click_y: int):
        if click_x < self._x_coordinate or click_x > (self._x_coordinate + self._width):
            return False
        if click_y < self._y_coordinate or click_y > (self._y_coordinate + self._height):
            return False

        return True

    @property
    def text_name(self):
        return self._text_name
