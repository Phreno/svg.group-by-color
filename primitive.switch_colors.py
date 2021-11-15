#!/usr/bin/python3
import argparse
from xml.etree import ElementTree

from primitive_toolbox import GROUP_TAG, ATTRIB_LABEL, save_svg_root, colorize_group


def replace_colors(svg_file, old, new):
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    next_step(root, old, new)
    return root


def next_step(node, old, new):
    for child in node:
        if child.tag == GROUP_TAG:
            if child.attrib[ATTRIB_LABEL] == old:
                colorize_group(child, new)
            else:
                next_step(child, old, new)


def parse_args():
    """
    parse the arguments from the command line.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg_file', help='svg file path')
    parser.add_argument('old_color', help='the color to replace')
    parser.add_argument('new_color', help='the color color replacing the old one')
    parser.add_argument('--output', default='output.svg', help='output file path')
    args = parser.parse_args()
    return {
        'svg_file': args.svg_file,
        'old': args.old_color,
        'color': args.new_color,
        'output': args.output
    }


def main():
    """
    The main function
    :return:
    """
    result = parse_args()
    # TODO: `svg_file, old, color, output = parse_args()`
    # Some weird black magic runs to args init
    # can't retrieve args the proper way
    # needs to come back later with some caffeine
    svg_file = result['svg_file']
    old = result['old']
    new = result['color']
    output = result['output']
    root = replace_colors(svg_file, old, new)
    save_svg_root(root, output)


if __name__ == '__main__':
    main()
