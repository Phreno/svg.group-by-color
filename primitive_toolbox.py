from xml.etree import ElementTree

from color_toolbox import color_to_hex

GROUP_TAG = '{http://www.w3.org/2000/svg}g'
ATTRIB_LABEL = '{http://www.inkscape.org/namespaces/inkscape}label'
ATTRIB_STROKE = 'stroke'
ATTRIB_FILL = 'fill'


def create_svg_root():
    root = ElementTree.Element('svg')
    root.set('xmlns', 'http://www.w3.org/2000/svg')
    root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
    return root


def save_svg_root(root, output):
    """
    Writes the svg over the specified output
    :param root: the svg
    :param output: the output path
    """
    tree = ElementTree.ElementTree(root)
    tree.write(output)


def render_svg_from_color_child_dict(dictionary):
    """
    Renders the output with objects within simplified html color groups
    """
    root = create_svg_root()
    for color, children in dictionary.items():
        group = ElementTree.Element('g')
        for child in children:
            group.append(child)
        group.attrib[ATTRIB_LABEL] = color
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


def is_valid_attrib_on(child, attribute):
    attribute_is_valid = attribute in child.attrib and child.attrib[attribute] != 'none'
    is_background = 'x' in child.attrib and 'y' in child.attrib and child.attrib['x'] == child.attrib['y'] == '0'
    return attribute_is_valid and not is_background
