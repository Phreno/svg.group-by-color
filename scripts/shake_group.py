#!/usr/bin/python3
import argparse
import xml.etree.ElementTree as ElementTree

from lib.svg import GROUP_TAG_WITH_NAMESPACE, ATTRIB_LABEL_WITH_NAMESPACE
from lib.svg.geometry import extract_bezier_curve_from_path, render_stroke_from_points


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


def apply_noise_effect(node: ElementTree.Element):
    for child in node:
        path = child.attrib['d']
        curve = extract_bezier_curve_from_path(path)
        child.attrib['d'] = render_stroke_from_points(curve.plot(100), 1)


def is_within_groups(groups, child):
    for group in groups:
        if child.tag == GROUP_TAG_WITH_NAMESPACE and child.attrib[ATTRIB_LABEL_WITH_NAMESPACE] == group:
            return True
    return False


def next_step(node: ElementTree, groups):
    for child in node:
        if is_within_groups(groups, child):
            apply_noise_effect(child)
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
