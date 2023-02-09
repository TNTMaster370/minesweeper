import ctypes
import os


def initialize_colour_palette():
    return {
        "red":        (245, 65,  65),   # 3
        "orange":     (255, 163, 23),   # 7
        "gold":       (240, 191, 57),   # hidden tile, highlighted
        "husk":       (180, 157, 71),   # revealed tile, highlighted
        "yellow":     (240, 234, 57),   # 5
        "green":      (52,  170, 0),    # 2
        "cyan":       (0,   209, 209),  # 6
        "blue":       (0,   146, 227),  # 1
        "purple":     (165, 102, 247),  # 4
        "magenta":    (239, 85,  224),  # 8
        "brown":      (144, 95,  95),   # flags
        "white":      (255, 255, 255),
        "light gray": (234, 234, 234),  # mines
        "mid gray":   (184, 184, 184),  # revealed tile
        "dark gray":  (63,  63,  63),   # bg, hidden tile
        "black":      (0,   0,   0)
    }


def initialize_difficulty_list():
    return {
        "Easy":    (9,  9,  10),
        "Medium":  (16, 16, 40),
        "Hard":    (30, 16, 99),
        "Extreme": (30, 24, 180)
    }


def initialize_display_size():
    user_screen = ctypes.windll.user32
    monitor_width = user_screen.GetSystemMetrics(0)
    monitor_height = user_screen.GetSystemMetrics(1)

    screen_width = monitor_width / 2
    if screen_width < (4/5)*monitor_height:
        screen_height = 300
    else:
        screen_height = (2/3)*monitor_height

    return screen_width, screen_height


def initialize_font_path(desired_font: str):
    for root, dirs, files in os.walk("C:\\"):
        for name in files:
            if name == desired_font:
                return os.path.abspath(os.path.join(root, name))
    raise FileNotFoundError
