#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ElementTree
from collections import defaultdict

from color_toolbox import color_to_hex
from color_toolbox import hex_to_nearest_color_name, COLORS
from toolbox import GROUP_TAG_WITH_NAMESPACE, save_svg_root, render_svg_from_color_child_dict, \
    ATTRIB_FILL, \
    ATTRIB_STROKE, \
    is_valid_attrib_on


def get_color_dict(svg, colors):
    """
    Creates a dictionary mapping based on available colors in the svg file.
    Colors are processed on the stroke attribute or the fill attribute.
    :param svg: the svg document containing colors to process
    :param colors: the available colors to process
    :return: a dictionary mapping a color name to a svg group element.
    """
    tree = ElementTree.parse(svg)
    root = tree.getroot()
    dictionary = defaultdict(list)
    return next_step(root, dictionary, colors)


def next_step(node, dictionary, colors):
    """
    Do the `get_color_dict` recursion
    :param colors:  the available colors to process
    :param dictionary: the dictionary mapping a color name to a svg group element.
    :param node: current node in the tree
    :return: the current node's dictionary
    """
    for child in node:
        if child.tag == GROUP_TAG_WITH_NAMESPACE:
            next_step(child, dictionary, colors)
        else:
            add_to_dict(child, colors, dictionary)
    return dictionary


def add_to_dict(child, colors, dictionary):
    if is_valid_attrib_on(child, ATTRIB_FILL):
        update_child_and_append_to_dict(child, colors, dictionary, ATTRIB_FILL)
    elif is_valid_attrib_on(child, ATTRIB_STROKE):
        update_child_and_append_to_dict(child, colors, dictionary, ATTRIB_STROKE)


def update_child_and_append_to_dict(child, colors, dictionary, attribute):
    color = hex_to_nearest_color_name(child.attrib[attribute], colors)
    child.attrib[attribute] = color_to_hex(color)
    dictionary[color].append(child)


def get_colors_from_args(colors):
    if colors is None:
        return COLORS
    else:
        buffer = {}
        for color in colors:
            buffer[color] = COLORS[color]
        return buffer


def parse_args():
    """
    :return: the args from the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg', help='svg file path')
    parser.add_argument('--output', default='output.svg', help='output file')
    parser.add_argument('--colors', nargs='+', default=None, help='colors to apply')
    return parser.parse_args()


def main():
    """
    Gets the job done
    """
    dictionary = get_color_dict(args.svg, get_colors_from_args(args.colors))
    root = render_svg_from_color_child_dict(dictionary)
    save_svg_root(root, args.output)


args = parse_args()
main()
