import re

from collections import namedtuple

from .. import Color, COLORS


def color_to_hex(color_name):
    """
    :param color_name: the name of the color
    :return: the hex representation of the color
    """
    return '#{:02x}{:02x}{:02x}'.format(*COLORS[color_name])


def color_to_nearest_color_name(color, colors=None):
    """
    :param colors: the list of available colors
    :param color: a RGB `color` code
    :return: the nearest html color name.
    """
    if colors is None:
        colors = COLORS
    r, g, b = color
    min_colors = {}
    for key, value in colors.items():
        r_c, g_c, b_c = value
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colors[(rd + gd + bd)] = key
    return min_colors[min(min_colors.keys())]




def hex_to_nearest_color_name(hex_color, colors=None):
    """
    :param colors: the list of available colors.
    :param hex_color: the color in hex format (ex: #123456)
    :return: the nearest html color name from a hex color
    """
    if colors is None:
        colors = COLORS
    if re.match(r'^#?[0-9a-f]{6}$', hex_color, re.IGNORECASE):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return color_to_nearest_color_name(Color(r, g, b), colors)



def hex_to_rgb_tuple(hex_color):
    """
    :hex_color: a string that represents a hex color (ex: "#123456")
    :return: a tuple of 3 integers that represents the rgb color
    """
    hex_color = str(hex_color)
    hex_color = hex_color[1:]
    hex_color = [hex_color[i:i + 2] for i in range(0, len(hex_color), 2)]
    hex_color = [int(hex_color[i], 16) for i in range(len(hex_color))]
    return tuple(hex_color)


def rgb_tuple_to_color(rgb):
    return Color(rgb[0], rgb[1], rgb[2])


def rgb_to_hex(rgb_color):
    """
    :rgb_color: a tuple of 3 integers that represents the rgb color
    :return: a string that represents a hex color (ex: "#123456")
    """
    rgb_color = [str(hex(rgb_color[i])) for i in range(len(rgb_color))]
    rgb_color = [rgb_color[i][2:] for i in range(len(rgb_color))]
    rgb_color = [rgb_color[i] if len(rgb_color[i]) == 2 else '0' + rgb_color[i] for i in range(len(rgb_color))]
    rgb_color = ''.join(rgb_color)
    rgb_color = '#' + rgb_color
    return rgb_color
