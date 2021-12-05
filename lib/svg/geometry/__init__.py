import random
import re

from lib.geometry.curve.bezier import BezierCurve
from lib.geometry.point import Point


# Given an array of points, render the corresponding svg stroke path
# if noise, randomize the point position
def render_stroke_from_points(points, noise):
    path = "M " + str(points[0].x) + " " + str(points[0].y) + " "
    for i in range(1, len(points)):
        if noise:
            path += "L " + str(points[i].x + random.randint(-noise, noise)) + " " + str(
                points[i].y + random.randint(-noise, noise)) + " "
        else:
            path += "L " + str(points[i].x) + " " + str(points[i].y) + " "
    return path


def render_points(points, noise):
    paths = []
    for point in points:
        if noise:
            path = "M " \
                   + "{:.6f}".format(point.x + random.randint(-noise, noise)) + " " + "{:.6f}".format(
                point.y + random.randint(-noise, noise)) \
                   + " L " \
                   + "{:.6f}".format(point.x + random.randint(-noise, noise)) + " " + "{:.6f}".format(
                point.y + random.randint(-noise, noise))
        else:
            path = "M " + str(point.x) + " " + str(point.y)
        paths.append(path)
    return paths


# Given an Svg stroke path with a curve, extract the corresponding bezier curve
# ex:
# Input "M 16 144 Q 73 33, 144 133
# Output BezierCurve(Point(16, 144), Point(73, 33), Point(144, 133))
def extract_bezier_curve_from_path(path):
    # Extract the points
    points = re.sub("([a-zA-Z] |,)", ' ', path).split()
    # Extract the points
    p0 = Point(float(points[0]), float(points[1]))
    p1 = Point(float(points[2]), float(points[3]))
    p2 = Point(float(points[4]), float(points[5]))
    return BezierCurve(p0, p1, p2)
