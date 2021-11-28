#!/usr/bin/python3
import argparse
from xml.etree import ElementTree

from toolbox import GROUP_TAG, ATTRIB_LABEL, save_svg_root, colorize_group


def replace_colors(svg_file, old, new):
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    next_step(root, old, new)
    return root


def next_step(node, old, new):
    for child in node:
        if child.tag == GROUP_TAG:
            if ATTRIB_LABEL in child.attrib and child.attrib[ATTRIB_LABEL] == old:
                colorize_group(child, new)
            else:
                next_step(child, old, new)
        else:
            next_step(child, old, new)


def parse_args():
    """
    parse the arguments from the command line.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg', help='svg file path')
    parser.add_argument('old', help='the color to replace')
    parser.add_argument('new', help='the color color replacing the old one')
    parser.add_argument('--output', default='output.svg', help='output file path')
    return parser.parse_args()


def main():
    """
    The main function
    :return:
    """
    root = replace_colors(args.svg, args.old, args.new)
    save_svg_root(root, args.output)


args = parse_args()
main()
