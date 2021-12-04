#!/usr/bin/python3
import argparse
import xml.etree.ElementTree as ElementTree

from color.toolbox import color_to_hex
from svg.toolbox import extract_bezier_curve_from_path, GROUP_TAG_WITH_NAMESPACE, \
    ATTRIB_LABEL_WITH_NAMESPACE, render_points


def main():
    args = parse_args()
    root = apply_filter(args.svg, args.groups)
    tree = ElementTree.ElementTree(root)
    tree.write(args.output)


def apply_filter(svg, groups):
    tree = ElementTree.parse(svg)
    root = tree.getroot()
    next_step(root, groups)
    return root


def apply_dash_effect(node: ElementTree.Element):
    points = []
    for child in node:
        path = child.attrib['d']
        curve = extract_bezier_curve_from_path(path)
        points.extend( render_points(curve.plot(100), 1))
        node.remove(child)
    return points


def is_within_groups(groups, child):
    for group in groups:
        if child.tag == GROUP_TAG_WITH_NAMESPACE and child.attrib[ATTRIB_LABEL_WITH_NAMESPACE] == group:
            return True
    return False


def next_step(node: ElementTree, groups):
    for child in node:
        if is_within_groups(groups, child):
            print(child.attrib[ATTRIB_LABEL_WITH_NAMESPACE])
            points = apply_dash_effect(child)
            for point in points:
                ElementTree.SubElement(child, "ns0:path", {
                    'd': point,
                    'stroke': color_to_hex(child.attrib[ATTRIB_LABEL_WITH_NAMESPACE]),
                    'stroke-width': '0.5',
                    'stroke-opacity': '0.501961',
                })

        else:
            next_step(child, groups)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Apply a shaking effect to a svg file"
    )
    parser.add_argument("svg", help="input svg file")
    parser.add_argument("output", help="output svg file")
    parser.add_argument("groups", nargs="+", help="groups used to apply effect")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
