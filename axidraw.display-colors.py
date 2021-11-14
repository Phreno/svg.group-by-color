#!/usr/bin/python3
import argparse
from xml.etree import ElementTree

from colors import print_color
from colors import sort_html_colors


def print_colors(colors):
    for color in colors:
        print_color(color)


def get_colors(svg_file):
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    colors = []
    for child in root:
        if child.tag == '{http://www.w3.org/2000/svg}g':
            color = child.attrib['{http://www.inkscape.org/namespaces/inkscape}label']
            colors.append(color)
    return colors


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('svg_file', help='svg file path')
    return parser.parse_args()


def main():
    """
    The main function
    :return:
    """
    args = parse_args()
    colors = get_colors(args.svg_file)
    print_colors(sort_html_colors(colors))


if __name__ == '__main__':
    main()
