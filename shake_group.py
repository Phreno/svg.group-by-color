#!/usr/bin/python3
import argparse
import xml.etree.ElementTree as ElementTree

from toolbox import extract_bezier_curve_from_path, render_stroke_from_points, GROUP_TAG_WITH_NAMESPACE, \
    ATTRIB_LABEL_WITH_NAMESPACE


def main():
    args = parse_args()
    root = apply_filter(args.svg, args.group)
    tree = ElementTree.ElementTree(root)
    tree.write(args.output)


def apply_filter(svg, group):
    tree = ElementTree.parse(svg)
    root = tree.getroot()
    next_step(root, group)
    return root


def apply_noise_effect(node: ElementTree.Element):
    for child in node:
        path = child.attrib['d']
        curve = extract_bezier_curve_from_path(path)
        child.attrib['d'] = render_stroke_from_points(curve.plot(100), noise=True)


def next_step(node: ElementTree, group):
    for child in node:
        if child.tag == GROUP_TAG_WITH_NAMESPACE and child.attrib[ATTRIB_LABEL_WITH_NAMESPACE] == group:
            apply_noise_effect(child)
            return
        else:
            next_step(child, group)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Apply a shaking effect to a svg file"
    )
    parser.add_argument("svg", help="input svg file")
    parser.add_argument("output", help="output svg file")
    parser.add_argument("group", help="group used to apply effect")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
