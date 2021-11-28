#!/usr/bin/python3
from bezier_curve import BezierCurve
from point import Point


def split_curve_with_points(curve: BezierCurve, segments=10) -> [BezierCurve]:
    points = curve.get_points()
    curves = []
    start = points[0]
    top = points[1]
    end = points[2]
    offset_1 = Point((top.x - start.x), (top.y - start.y))
    offset_2 = Point((end.x - top.x), (end.y - top.y))
    increment_1 = Point(offset_1.x / segments, offset_1.y / segments)
    increment_2 = Point(offset_2.x / segments, offset_2.y / segments)
    current = Point(start.x, start.y)
    for i in range(segments - 1):
        curves.append(current)
        current = current.__copy__() + increment_1

    for i in range(segments - 1):
        curves.append(current)
        current = current.__copy__() + increment_2
    return curves


def get_points_from_curves(curves):
    points = []
    for curve in curves:
        points += curve.get_points()
    return points


def get_points_as_tuples(curves):
    points = []
    for curve in curves:
        points += curve.get_points_as_tuples()
    return points


def plot_bezier_curve_equation(curve: BezierCurve, amount: int):
    """
    Given Quadratic Bezier controls points
    Returns a list
    """

    points = []

    for i in range(amount):
        t = i / amount
        x = (1 - t) ** 2 * curve.start.x + 2 * (1 - t) * t * curve.control.x + t ** 2 * curve.end.x
        y = (1 - t) ** 2 * curve.start.y + 2 * (1 - t) * t * curve.control.y + t ** 2 * curve.end.y
        points.append(Point(x, y))
    return points
