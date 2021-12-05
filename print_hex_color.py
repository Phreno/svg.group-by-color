#!/usr/bin/python3
from color.printer import print_hex_color


def parse_args():
    """
    Parse command line arguments
    """
    import argparse
    parser = argparse.ArgumentParser(description='Print hex colors on the console')
    parser.add_argument('color', nargs='?', default='#000000', help='Color to print')
    return parser.parse_args()


def main():
    """
    Main function
    """
    args = parse_args()
    print_hex_color(args.color)


if __name__ == '__main__':
    main()
