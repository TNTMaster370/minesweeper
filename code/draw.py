import pygame


def draw_text(text: str, x_coordinate: int, y_coordinate: int, colour: tuple, font_path: str, size: int):
    font = pygame.font.Font(font_path, size)
    text = font.render(text, True, colour)
    text_boundaries = text.get_rect()
    text_boundaries.center = (x_coordinate, y_coordinate)
    return text, text_boundaries
