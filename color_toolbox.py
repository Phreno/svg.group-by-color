import re

from collections import namedtuple

Color = namedtuple('Color', ['r', 'g', 'b'])

COLORS = {
    'Black': Color(0,0,0),
    'Maroon': Color(128,0,0),
    'Green': Color(0,128,0),
    'Olive': Color(128,128,0),
    'Navy': Color(0,0,128),
    'Purple': Color(128,0,128),
    'Teal': Color(0,128,128),
    'Silver': Color(192,192,192),
    'Grey': Color(128,128,128),
    'Red': Color(255,0,0),
    'Lime': Color(0,255,0),
    'Yellow': Color(255,255,0),
    'Blue': Color(0,0,255),
    'Fuchsia': Color(255,0,255),
    'Aqua': Color(0,255,255),
    'White': Color(255,255,255),
    'Grey0': Color(0,0,0),
    'NavyBlue': Color(0,0,95),
    'DarkBlue': Color(0,0,135),
    'Blue3': Color(0,0,175),
    'Blue3': Color(0,0,215),
    'Blue1': Color(0,0,255),
    'DarkGreen': Color(0,95,0),
    'DeepSkyBlue4': Color(0,95,95),
    'DeepSkyBlue4': Color(0,95,135),
    'DeepSkyBlue4': Color(0,95,175),
    'DodgerBlue3': Color(0,95,215),
    'DodgerBlue2': Color(0,95,255),
    'Green4': Color(0,135,0),
    'SpringGreen4': Color(0,135,95),
    'Turquoise4': Color(0,135,135),
    'DeepSkyBlue3': Color(0,135,175),
    'DeepSkyBlue3': Color(0,135,215),
    'DodgerBlue1': Color(0,135,255),
    'Green3': Color(0,175,0),
    'SpringGreen3': Color(0,175,95),
    'DarkCyan': Color(0,175,135),
    'LightSeaGreen': Color(0,175,175),
    'DeepSkyBlue2': Color(0,175,215),
    'DeepSkyBlue1': Color(0,175,255),
    'Green3': Color(0,215,0),
    'SpringGreen3': Color(0,215,95),
    'SpringGreen2': Color(0,215,135),
    'Cyan3': Color(0,215,175),
    'DarkTurquoise': Color(0,215,215),
    'Turquoise2': Color(0,215,255),
    'Green1': Color(0,255,0),
    'SpringGreen2': Color(0,255,95),
    'SpringGreen1': Color(0,255,135),
    'MediumSpringGreen': Color(0,255,175),
    'Cyan2': Color(0,255,215),
    'Cyan1': Color(0,255,255),
    'DarkRed': Color(95,0,0),
    'DeepPink4': Color(95,0,95),
    'Purple4': Color(95,0,135),
    'Purple4': Color(95,0,175),
    'Purple3': Color(95,0,215),
    'BlueViolet': Color(95,0,255),
    'Orange4': Color(95,95,0),
    'Grey37': Color(95,95,95),
    'MediumPurple4': Color(95,95,135),
    'SlateBlue3': Color(95,95,175),
    'SlateBlue3': Color(95,95,215),
    'RoyalBlue1': Color(95,95,255),
    'Chartreuse4': Color(95,135,0),
    'DarkSeaGreen4': Color(95,135,95),
    'PaleTurquoise4': Color(95,135,135),
    'SteelBlue': Color(95,135,175),
    'SteelBlue3': Color(95,135,215),
    'CornflowerBlue': Color(95,135,255),
    'Chartreuse3': Color(95,175,0),
    'DarkSeaGreen4': Color(95,175,95),
    'CadetBlue': Color(95,175,135),
    'CadetBlue': Color(95,175,175),
    'SkyBlue3': Color(95,175,215),
    'SteelBlue1': Color(95,175,255),
    'Chartreuse3': Color(95,215,0),
    'PaleGreen3': Color(95,215,95),
    'SeaGreen3': Color(95,215,135),
    'Aquamarine3': Color(95,215,175),
    'MediumTurquoise': Color(95,215,215),
    'SteelBlue1': Color(95,215,255),
    'Chartreuse2': Color(95,255,0),
    'SeaGreen2': Color(95,255,95),
    'SeaGreen1': Color(95,255,135),
    'SeaGreen1': Color(95,255,175),
    'Aquamarine1': Color(95,255,215),
    'DarkSlateGray2': Color(95,255,255),
    'DarkRed': Color(135,0,0),
    'DeepPink4': Color(135,0,95),
    'DarkMagenta': Color(135,0,135),
    'DarkMagenta': Color(135,0,175),
    'DarkViolet': Color(135,0,215),
    'Purple': Color(135,0,255),
    'Orange4': Color(135,95,0),
    'LightPink4': Color(135,95,95),
    'Plum4': Color(135,95,135),
    'MediumPurple3': Color(135,95,175),
    'MediumPurple3': Color(135,95,215),
    'SlateBlue1': Color(135,95,255),
    'Yellow4': Color(135,135,0),
    'Wheat4': Color(135,135,95),
    'Grey53': Color(135,135,135),
    'LightSlateGrey': Color(135,135,175),
    'MediumPurple': Color(135,135,215),
    'LightSlateBlue': Color(135,135,255),
    'Yellow4': Color(135,175,0),
    'DarkOliveGreen3': Color(135,175,95),
    'DarkSeaGreen': Color(135,175,135),
    'LightSkyBlue3': Color(135,175,175),
    'LightSkyBlue3': Color(135,175,215),
    'SkyBlue2': Color(135,175,255),
    'Chartreuse2': Color(135,215,0),
    'DarkOliveGreen3': Color(135,215,95),
    'PaleGreen3': Color(135,215,135),
    'DarkSeaGreen3': Color(135,215,175),
    'DarkSlateGray3': Color(135,215,215),
    'SkyBlue1': Color(135,215,255),
    'Chartreuse1': Color(135,255,0),
    'LightGreen': Color(135,255,95),
    'LightGreen': Color(135,255,135),
    'PaleGreen1': Color(135,255,175),
    'Aquamarine1': Color(135,255,215),
    'DarkSlateGray1': Color(135,255,255),
    'Red3': Color(175,0,0),
    'DeepPink4': Color(175,0,95),
    'MediumVioletRed': Color(175,0,135),
    'Magenta3': Color(175,0,175),
    'DarkViolet': Color(175,0,215),
    'Purple': Color(175,0,255),
    'DarkOrange3': Color(175,95,0),
    'IndianRed': Color(175,95,95),
    'HotPink3': Color(175,95,135),
    'MediumOrchid3': Color(175,95,175),
    'MediumOrchid': Color(175,95,215),
    'MediumPurple2': Color(175,95,255),
    'DarkGoldenrod': Color(175,135,0),
    'LightSalmon3': Color(175,135,95),
    'RosyBrown': Color(175,135,135),
    'Grey63': Color(175,135,175),
    'MediumPurple2': Color(175,135,215),
    'MediumPurple1': Color(175,135,255),
    'Gold3': Color(175,175,0),
    'DarkKhaki': Color(175,175,95),
    'NavajoWhite3': Color(175,175,135),
    'Grey69': Color(175,175,175),
    'LightSteelBlue3': Color(175,175,215),
    'LightSteelBlue': Color(175,175,255),
    'Yellow3': Color(175,215,0),
    'DarkOliveGreen3': Color(175,215,95),
    'DarkSeaGreen3': Color(175,215,135),
    'DarkSeaGreen2': Color(175,215,175),
    'LightCyan3': Color(175,215,215),
    'LightSkyBlue1': Color(175,215,255),
    'GreenYellow': Color(175,255,0),
    'DarkOliveGreen2': Color(175,255,95),
    'PaleGreen1': Color(175,255,135),
    'DarkSeaGreen2': Color(175,255,175),
    'DarkSeaGreen1': Color(175,255,215),
    'PaleTurquoise1': Color(175,255,255),
    'Red3': Color(215,0,0),
    'DeepPink3': Color(215,0,95),
    'DeepPink3': Color(215,0,135),
    'Magenta3': Color(215,0,175),
    'Magenta3': Color(215,0,215),
    'Magenta2': Color(215,0,255),
    'DarkOrange3': Color(215,95,0),
    'IndianRed': Color(215,95,95),
    'HotPink3': Color(215,95,135),
    'HotPink2': Color(215,95,175),
    'Orchid': Color(215,95,215),
    'MediumOrchid1': Color(215,95,255),
    'Orange3': Color(215,135,0),
    'LightSalmon3': Color(215,135,95),
    'LightPink3': Color(215,135,135),
    'Pink3': Color(215,135,175),
    'Plum3': Color(215,135,215),
    'Violet': Color(215,135,255),
    'Gold3': Color(215,175,0),
    'LightGoldenrod3': Color(215,175,95),
    'Tan': Color(215,175,135),
    'MistyRose3': Color(215,175,175),
    'Thistle3': Color(215,175,215),
    'Plum2': Color(215,175,255),
    'Yellow3': Color(215,215,0),
    'Khaki3': Color(215,215,95),
    'LightGoldenrod2': Color(215,215,135),
    'LightYellow3': Color(215,215,175),
    'Grey84': Color(215,215,215),
    'LightSteelBlue1': Color(215,215,255),
    'Yellow2': Color(215,255,0),
    'DarkOliveGreen1': Color(215,255,95),
    'DarkOliveGreen1': Color(215,255,135),
    'DarkSeaGreen1': Color(215,255,175),
    'Honeydew2': Color(215,255,215),
    'LightCyan1': Color(215,255,255),
    'Red1': Color(255,0,0),
    'DeepPink2': Color(255,0,95),
    'DeepPink1': Color(255,0,135),
    'DeepPink1': Color(255,0,175),
    'Magenta2': Color(255,0,215),
    'Magenta1': Color(255,0,255),
    'OrangeRed1': Color(255,95,0),
    'IndianRed1': Color(255,95,95),
    'IndianRed1': Color(255,95,135),
    'HotPink': Color(255,95,175),
    'HotPink': Color(255,95,215),
    'MediumOrchid1': Color(255,95,255),
    'DarkOrange': Color(255,135,0),
    'Salmon1': Color(255,135,95),
    'LightCoral': Color(255,135,135),
    'PaleVioletRed1': Color(255,135,175),
    'Orchid2': Color(255,135,215),
    'Orchid1': Color(255,135,255),
    'Orange1': Color(255,175,0),
    'SandyBrown': Color(255,175,95),
    'LightSalmon1': Color(255,175,135),
    'LightPink1': Color(255,175,175),
    'Pink1': Color(255,175,215),
    'Plum1': Color(255,175,255),
    'Gold1': Color(255,215,0),
    'LightGoldenrod2': Color(255,215,95),
    'LightGoldenrod2': Color(255,215,135),
    'NavajoWhite1': Color(255,215,175),
    'MistyRose1': Color(255,215,215),
    'Thistle1': Color(255,215,255),
    'Yellow1': Color(255,255,0),
    'LightGoldenrod1': Color(255,255,95),
    'Khaki1': Color(255,255,135),
    'Wheat1': Color(255,255,175),
    'Cornsilk1': Color(255,255,216),
    'Grey100': Color(255,255,255),
    'Grey3': Color(8,8,8),
    'Grey7': Color(18,18,18),
    'Grey11': Color(28,28,28),
    'Grey15': Color(38,38,38),
    'Grey19': Color(48,48,48),
    'Grey23': Color(58,58,58),
    'Grey27': Color(68,68,68),
    'Grey30': Color(78,78,78),
    'Grey35': Color(88,88,88),
    'Grey39': Color(98,98,98),
    'Grey42': Color(108,108,108),
    'Grey46': Color(118,118,118),
    'Grey50': Color(128,128,128),
    'Grey54': Color(138,138,138),
    'Grey58': Color(148,148,148),
    'Grey62': Color(158,158,158),
    'Grey66': Color(168,168,168),
    'Grey70': Color(178,178,178),
    'Grey74': Color(188,188,188),
    'Grey78': Color(198,198,198),
    'Grey82': Color(208,208,208),
    'Grey85': Color(218,218,218),
    'Grey89': Color(228,228,228),
    'Grey93': Color(238,238,238),
}


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


def sort_hex_colors(colors):
    """
    :colors: a list of string that represents hex colors (ex: "#123456")
    :return: the same list ordered in a way that represent a gradient
    """
    colors = [hex_to_rgb_tuple(color) for color in colors]  # switching to rgb colors
    colors.sort(key=lambda rgb: (rgb[0], rgb[1], rgb[2]))
    return [rgb_to_hex(color) for color in colors]  # restore hex colors


def sort_html_colors(colors):
    """
    :param colors: the list of strings that represent html colors (ex: [gainsboro, red, aliceblue])
    :return: the color sorted in a way that represent a gradient
    """
    hex_colors_sorted = sort_hex_colors(map(color_to_hex, colors))
    return map(hex_to_nearest_color_name, hex_colors_sorted)


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
