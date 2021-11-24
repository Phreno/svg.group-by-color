#!/usr/bin/python3

import re
import sys

from color.color_toolbox import Color
from color.color_toolbox import color_to_nearest_color_name


def main():
    """
    Main function.
    """
    color = sys.argv[1]
    if re.match(r'^#?[0-9a-f]{6}$', color, re.IGNORECASE):
        color = color.lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        print(color_to_nearest_color_name(Color(r, g, b)))
    else:
        print('Invalid color')


if __name__ == '__main__':
    main()
