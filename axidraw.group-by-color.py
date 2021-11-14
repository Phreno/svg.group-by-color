#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ElementTree

from collections import defaultdict
from colors import get_html_color_name_from_hex, COLORS
from colors import html_color_to_hex


def get_color_dict(svg_file, model, colors):
    """
    Creates a dictionary mapping based on available hex_colors in the svg file.
    Colors are processed on the stroke attribute or the fill attribute.
    :param colors: the available colors to process
    :param svg_file: the file to process
    :param model: "stroke" or "fill"
    :return: a dictionary mapping a color name to a svg child element.
    """
    tree = ElementTree.parse(svg_file)
    root = tree.getroot()
    dictionary = defaultdict(list)
    return next_step(root, model, dictionary, colors)


def next_step(node, model, dictionary, colors):
    """
    Do the `get_color_dict` recursion
    :param colors:  the available colors to process
    :param dictionary: the dictionary mapping a color name to a svg child element.
    :param node: current node in the tree
    :param model: "stroke" or "fill"
    :return: the current node's dictionary
    """
    for child in node:
        if child.tag == '{http://www.w3.org/2000/svg}g':
            next_step(child, model, dictionary, colors)
        else:
            if model in child.attrib:
                color = get_html_color_name_from_hex(child.attrib[model], colors)
                child.attrib[model] = html_color_to_hex(color)
                dictionary[color].append(child)
    return dictionary


def render_svg(dictionary):
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
    root = render_svg(dictionary)
    save_svg(root, output)


if __name__ == '__main__':
    main()
