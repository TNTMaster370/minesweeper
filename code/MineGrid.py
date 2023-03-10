from draw import draw_text

import random
import pygame


def _generate_grid(length: int, height: int, mine_count: int, mine_positioning: tuple):
    grid_visual = []
    grid_answer = []

    for row in range(length):
        grid_visual.append([])
        grid_answer.append([])
        for _ in range(height):
            grid_visual[row].append("#")
            grid_answer[row].append(0)

    index = 0
    while index < mine_count:
        mine = (random.randint(0, length-1), random.randint(0, height-1))
        if grid_answer[mine[0]][mine[1]] != "X":
            grid_answer[mine[0]][mine[1]] = "X"
            index += 1

    for x in range(length):
        for y in range(height):
            if grid_answer[x][y] == "X":
                continue

            for z in mine_positioning:
                try:
                    if grid_answer[x+z[0]][y+z[1]] == "X":
                        grid_answer[x][y] += 1
                except IndexError:
                    pass

    return grid_visual, grid_answer


def _reveal_zeroes(grid_visual, grid_answer, mine_position, x: int, y: int):
    for pos_x, pos_y in mine_position:
        try:
            if grid_visual[x+pos_x][y+pos_y] != "#":
                continue
            grid_visual[x + pos_x][y + pos_y] = grid_answer[x + pos_x][y + pos_y]
            if grid_visual[x+pos_x][y+pos_y] == 0:
                grid_visual, grid_answer = _reveal_zeroes(grid_visual, grid_answer, mine_position, x+pos_x, y+pos_y)
        except IndexError:
            continue

    return grid_visual, grid_answer


class MineGrid:
    def __init__(self, display, length: int, height: int, mine_count: int, mine_positioning: tuple = None):
        self._length = length
        self._height = height
        self._mine_count = mine_count

        self._mine_position = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        if mine_positioning:
            self._mine_position = mine_positioning

        self._tile_size = int(display.get_height() / length)
        if length > height:
            self._tile_size = int(display.get_width() / length)
        elif length < height:
            self._tile_size = int(display.get_height() / height)

        self._offset = (((display.get_width() - (self._tile_size*self._length)) / 2),
                        ((display.get_height() - (self._tile_size*self._height)) / 2))

        self._grid_visual, self._grid_answer = _generate_grid(self._length, self._height, self._mine_count, self._mine_position)

    def draw_grid(self, display, clock, font_path, colour_palette):
        colour = ("", colour_palette["blue"], colour_palette["green"], colour_palette["red"], colour_palette["purple"],
                  colour_palette["yellow"], colour_palette["cyan"], colour_palette["orange"], colour_palette["magenta"])

        for x in range(self._length):
            for y in range(self._height):
                if self._grid_visual[x][y] == ("#" or "F"):
                    pygame.draw.rect(display, colour_palette["mid-dark gray"],
                                     [x*self._tile_size+self._offset[0], y*self._tile_size+self._offset[1], self._tile_size, self._tile_size])
                    pygame.draw.rect(display, colour_palette["white"],
                                     [x*self._tile_size+self._offset[0], y*self._tile_size+self._offset[1], self._tile_size, self._tile_size], 2)
                else:
                    pygame.draw.rect(display, colour_palette["mid gray"],
                                     [x*self._tile_size+self._offset[0], y*self._tile_size+self._offset[1], self._tile_size, self._tile_size])

                if self._grid_visual[x][y] == "#":
                    continue
                if self._grid_visual[x][y] == 0:
                    continue

                if self._grid_visual[x][y] == "X":
                    text, text_boundaries = draw_text("X", x*self._tile_size+self._offset[0], y*self._tile_size+self._offset[1],
                                                      colour_palette["light gray"], font_path, int(self._tile_size / 1.5))
                    display.blit(text, text_boundaries)

                elif self._grid_visual[x][y] == "F":
                    pygame.draw.rect(display, colour_palette["white"],
                                     [x * self._tile_size + self._offset[0] + ((3 / 10) * self._tile_size),
                                      y * self._tile_size + self._offset[1] + ((3 / 24) * self._tile_size),
                                      (1 / 5) * self._tile_size, (10 / 14) * self._tile_size])
                    pygame.draw.rect(display, colour_palette["brown"],
                                     [x * self._tile_size + self._offset[0] + ((1 / 5) * self._tile_size),
                                      y * self._tile_size + self._offset[1] + ((1 / 6) * self._tile_size),
                                      (3 / 5) * self._tile_size, (2 / 6) * self._tile_size])
                    pygame.draw.rect(display, colour_palette["white"],
                                     [x * self._tile_size + self._offset[0] + ((1 / 5) * self._tile_size),
                                      y * self._tile_size + self._offset[1] + ((11 / 14) * self._tile_size),
                                      (2 / 5) * self._tile_size, (1 / 7) * self._tile_size])

                else:
                    text, text_boundaries = draw_text(str(self._grid_visual[x][y]),
                                                      x * self._tile_size + self._offset[0] + (self._tile_size / 2),
                                                      y * self._tile_size + self._offset[1] + (self._tile_size / 2),
                                                      colour[self._grid_visual[x][y]], font_path, int(self._tile_size / 1.5))
                    display.blit(text, text_boundaries)

                pygame.draw.rect(display, colour_palette["white"],
                                 [x*self._tile_size+self._offset[0], y*self._tile_size+self._offset[1], self._tile_size, self._tile_size], 2)

    def check_flags(self):
        win_check = 0
        for x in range(self._length):
            for y in range(self._height):
                if self._grid_visual[x][y] == "F" and self._grid_answer[x][y] == "X":
                    win_check += 1

        if win_check == self._mine_count:
            return True

        return False

    def collision(self, click_x: int, click_y: int):
        if click_x < self._offset[0] or click_x > (self._offset[0] + (self._length * self._tile_size)):
            return -1, -1
        if click_y < self._offset[1] or click_y > (self._offset[1] + (self._height * self._tile_size)):
            return -1, -1

        for x in range(self._length):
            for y in range(self._height):
                if x*self._tile_size+self._offset[0] < click_x < (x+1)*self._tile_size+self._offset[0] \
                        and y*self._tile_size+self._offset[1] < click_y < (y+1)*self._tile_size+self._offset[1]:
                    return x, y

    def reveal_square(self, square_x: int, square_y: int):
        self._grid_visual[square_x][square_y] = self._grid_answer[square_x][square_y]

        if self._grid_visual[square_x][square_y] == 0:
            self._grid_visual, self._grid_answer = _reveal_zeroes(self._grid_visual, self._grid_answer,
                                                                 self._mine_position, square_x, square_y)

    def flag_square(self, square_x: int, square_y: int):
        if self._grid_visual[square_x][square_y] == "#":
            self._grid_visual[square_x][square_y] = "F"

        elif self._grid_visual[square_x][square_y] == "F":
            self._grid_visual[square_x][square_y] = "#"
