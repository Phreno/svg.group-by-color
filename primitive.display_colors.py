#!/usr/bin/python3
import argparse
from xml.etree import ElementTree

from color_toolbox import print_html_color
from color_toolbox import sort_html_colors
from primitive_toolbox import GROUP_TAG
from primitive_toolbox import ATTRIB_LABEL


def print_colors(colors):
    """
    Print the specified colors to stdout.
    :param colors: the colors to print
    :return:
    """
    for color in colors:
        print_html_color(color, count_colors(args.svg_file, color))


def get_colors(svg_file):
    """
    Extract the colors from an svg file.
    :param svg_file: the svg_file to extract the colors from.
    :return: a list of colors
    """
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    colors = []
    for child in root:
        if child.tag == GROUP_TAG:
            color = child.attrib[ATTRIB_LABEL]
            colors.append(color)
    return colors


def count_colors(svg_file, color):
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    for child in root:
        if child.tag == GROUP_TAG and color == child.attrib[ATTRIB_LABEL]:
            return len(child)
        else:
            continue


def parse_args():
    """
    parse the arguments from the command line.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg_file', help='svg file path')
    return parser.parse_args()


args = parse_args()


def main():
    """
    The main function
    :return:
    """
    colors = get_colors(args.svg_file)
    print_colors(sort_html_colors(colors))


if __name__ == '__main__':
    main()
