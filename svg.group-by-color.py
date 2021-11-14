#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ElementTree

from collections import defaultdict
from colors import get_html_color_name_from_hex
from colors import color_to_hex

dictionary = defaultdict(list)


def get_color_dict(svg_file, model):
    """
    Creates a dictionary mapping based on available colors in the svg file.
    Colors are processed on the stroke attribute or the fill attribute.
    :param svg_file: the file to process
    :param model: "stroke" or "fill"
    :return: a dictionary mapping a color name to a svg child element.
    """
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    return next_step(root, model)


def next_step(node, model):
    """
    Do the `get_color_dict` recursion
    :param node: current node in the tree
    :param model: "stroke" or "fill"
    :return: the current node's dictionary
    """
    for child in node:
        if child.tag == '{http://www.w3.org/2000/svg}g':
            next_step(child, model)
        else:
            if model in child.attrib:
                color = get_html_color_name_from_hex(child.attrib[model])
                child.attrib[model] = color_to_hex(color)
                dictionary[color].append(child)
    return dictionary


def render_svg():
    """
    Renders the output with objects within simplified html color groups
    """
    root = ElementTree.Element('svg')
    root.set('xmlns', 'http://www.w3.org/2000/svg')
    root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')

    for color, children in dictionary.items():
        group = ElementTree.Element('g')
        for child in children:
            group.append(child)
        group.attrib['{http://www.inkscape.org/namespaces/inkscape}label'] = color
        # group.attrib['{http://www.inkscape.org/namespaces/inkscape}groupmode'] = model
        root.append(group)
    return root


def save_svg(root, output):
    """
    Writes the svg over the specified output
    :param root: the svg
    :param output: the output path
    """
    tree = ElementTree.ElementTree(root)
    tree.write(output)


def parse_args():
    """
    :return: the args from the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('svg_file', help='svg file path')
    parser.add_argument('--model', default='stroke', help='stroke or fill')
    parser.add_argument('--output', default='out.svg', help='output file')
    return parser.parse_args()


def main():
    """
    Gets the job done
    """
    args = parse_args()
    get_color_dict(args.svg_file, args.model)
    root = render_svg()
    save_svg(root, args.output)


if __name__ == '__main__':
    main()
