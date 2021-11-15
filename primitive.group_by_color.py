#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ElementTree
from collections import defaultdict

from color_toolbox import get_html_color_name_from_hex, COLORS
from color_toolbox import html_color_to_hex
from primitive_toolbox import GROUP_TAG, save_svg_root, render_svg_from_color_child_dict


def get_color_dict(svg_file, model, colors):
    """
    Creates a dictionary mapping based on available colors in the svg file.
    Colors are processed on the stroke attribute or the fill attribute.
    :param colors: the available colors to process
    :param svg_file: the file to process
    :param model: "stroke" or "fill"
    :return: a dictionary mapping a color name to a svg group element.
    """
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    dictionary = defaultdict(list)
    return next_step(root, model, dictionary, colors)


def next_step(node, model, dictionary, colors):
    """
    Do the `get_color_dict` recursion
    :param colors:  the available colors to process
    :param dictionary: the dictionary mapping a color name to a svg group element.
    :param node: current node in the tree
    :param model: "stroke" or "fill"
    :return: the current node's dictionary
    """
    for child in node:
        if child.tag == GROUP_TAG:
            next_step(child, model, dictionary, colors)
        else:
            if model in child.attrib:
                color = get_html_color_name_from_hex(child.attrib[model], colors)
                child.attrib[model] = html_color_to_hex(color)
                dictionary[color].append(child)
    return dictionary


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
    parser.add_argument('svg_file', help='svg file path')
    parser.add_argument('--model', default='stroke', help='stroke or fill')
    parser.add_argument('--output', default='out.svg', help='output file')
    parser.add_argument('--colors', nargs='+', default=None, help='colors to apply')
    args = parser.parse_args()
    return {
        'svg_file': args.svg_file,
        'model': args.model,
        'output': args.output,
        'colors': get_colors_from_args(args.colors)
    }


def main():
    """
    Gets the job done
    """
    svg_file, model, colors, output = parse_args()
    dictionary = get_color_dict(svg_file, model, colors)
    root = render_svg_from_color_child_dict(dictionary)
    save_svg_root(root, output)


if __name__ == '__main__':
    main()
