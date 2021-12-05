from xml.etree.ElementTree import ElementTree

GROUP_TAG_WITH_NAMESPACE = '{http://www.w3.org/2000/svg}g'
ATTRIB_LABEL_WITH_NAMESPACE = '{http://www.inkscape.org/namespaces/inkscape}label'
ATTRIB_LABEL = 'label'
GROUP_TAG = 'g'
ATTRIB_STROKE = 'stroke'
ATTRIB_FILL = 'fill'


def create_svg_root():
    root = ElementTree.Element('svg')
    root.set('xmlns', 'http://www.w3.org/2000/svg')
    root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
    return root


def strip_namespace(element: ElementTree.Element):
    prefix, has_namespace, postfix = element.tag.partition('}')
    if has_namespace:
        element.tag = postfix


def remove_all_namespaces(node: ElementTree.Element):
    for child in node:
        strip_namespace(child)
        remove_all_namespaces(child)


def is_valid_attrib_on(child, attribute):
    attribute_is_valid = attribute in child.attrib and child.attrib[attribute] != 'none'
    is_background = 'x' in child.attrib and 'y' in child.attrib and child.attrib['x'] == child.attrib['y'] == '0'
    return attribute_is_valid and not is_background
