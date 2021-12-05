#!/usr/bin/python3
from color import COLORS
from color.printer import print_html_color
from color.sorter import sort_html_colors


def parse_args():
    """
    Parse command line arguments
    """
    import argparse
    parser = argparse.ArgumentParser(description='Print html colors on the console')
    parser.add_argument('color', nargs='?', default='white', help='Color to print')
    parser.add_argument('-l', '--list', action='store_true', help='List all available colors')
    return parser.parse_args()


def main():
    """
    Main function
    """
    args = parse_args()
    if args.list:
        for color in sort_html_colors(COLORS.keys()):
            print_html_color(color)
    else:
        print_html_color(args.color)


if __name__ == '__main__':
    main()
