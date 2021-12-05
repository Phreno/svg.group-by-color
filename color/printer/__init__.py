from .. import COLORS
from ..converter import hex_to_rgb_tuple, rgb_tuple_to_color


def print_rgb_color(color, message=None):
    print('\x1b[48;2;{};{};{}m\x1b[38;2;{};{};{}m{}\x1b[0m'.format(
        color.r, color.g, color.b,
        color.r, color.g, color.b,
        ' ' * 10
    ), message)


def print_html_color(color_name, message=None):
    """
    Prints a square on the console with the given color on background
    :param message: complete the displayed label with a custom message
    :param color_name: the name of the color (ex: gainsboro)
    """
    color = COLORS[color_name]
    label = ('(' + str(message) + ')').ljust(7) + color_name.ljust(26) + str(color).ljust(30)
    print_rgb_color(color, label)


def print_hex_color(hex_color):
    rgb = hex_to_rgb_tuple(hex_color)
    print_rgb_color(rgb_tuple_to_color(rgb), hex_color)
