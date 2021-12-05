from xml.etree.ElementTree import ElementTree

from color.converter import color_to_hex
from .. import create_svg_root, strip_namespace, ATTRIB_LABEL_WITH_NAMESPACE, ATTRIB_LABEL, ATTRIB_FILL, ATTRIB_STROKE, \
    is_valid_attrib_on


def render_svg_from_color_child_dict(dictionary):
    """
    Renders the output with objects within simplified html color groups
    """
    root = create_svg_root()
    for color, children in dictionary.items():
        group = ElementTree.Element('g')
        for child in children:
            strip_namespace(child)
            group.append(child)
        group.attrib[ATTRIB_LABEL_WITH_NAMESPACE] = color
        strip_namespace(group)
        root.append(group)
    return root


def colorize_group(group, color):
    group.attrib[ATTRIB_LABEL] = color
    for item in group:
        colorize_child(item, color)


def colorize_child(child, color):
    color = color_to_hex(color)
    if is_valid_attrib_on(child, ATTRIB_FILL):
        child.attrib[ATTRIB_FILL] = color
    elif is_valid_attrib_on(child, ATTRIB_STROKE):
        child.attrib[ATTRIB_STROKE] = color
