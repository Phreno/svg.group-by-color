#!/usr/bin/python3
import argparse
from xml.etree import ElementTree

from color.converter import color_to_hex
from svg.toolbox import GROUP_TAG, save_svg_root, is_valid_attrib_on, \
    ATTRIB_STROKE


def adjust_thickness(svg_file, color, thickness):
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    next_step(root, color, thickness)
    return root


def update_thickness(child, thickness):
    print(child.attrib, thickness)


def next_step(node, color, thickness):
    for child in node:
        if child.tag == GROUP_TAG:
            next_step(child, color, thickness)
        elif is_valid_attrib_on(child, 'stroke-width') and is_valid_attrib_on(child, ATTRIB_STROKE) and color_to_hex(
                color) == child.attrib[ATTRIB_STROKE]:
            child.attrib['stroke-width'] = thickness


def parse_args():
    """replace_colors
    parse the arguments from the command line.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg', help='svg file path')
    parser.add_argument('color', help='the color to replace')
    parser.add_argument('thickness', help='the color color replacing the old one')
    parser.add_argument('--output', default='output.svg', help='output file path')
    return parser.parse_args()


def main():
    """
    The main function
    :return:
    """
    root = adjust_thickness(args.svg, args.color, args.thickness)
    save_svg_root(root, args.output)


args = parse_args()
main()
