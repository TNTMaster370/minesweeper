import ctypes
import os

'''
def primary():
    user_screen = ctypes.windll.user32
    monitor_width = user_screen.GetSystemMetrics(0)
    monitor_height = user_screen.GetSystemMetrics(1)

    screen_width = (1 / 2) * monitor_width
    if screen_width < (4 / 5) * monitor_height:
        # screen_height = screen_width
        screen_height = 300
    else:
        screen_height = (2 / 3) * monitor_height'''


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
