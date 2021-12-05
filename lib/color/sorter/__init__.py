from ..converter import hex_to_rgb_tuple, rgb_to_hex, hex_to_nearest_color_name, color_to_hex


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

