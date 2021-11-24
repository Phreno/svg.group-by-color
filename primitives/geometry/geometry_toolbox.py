#!/usr/bin/python3

from geometry.bezier_curve import BezierCurve
from geometry.point import Point


def split_curve(curve, segments=10) -> [BezierCurve]:
    points = curve.get_points_as_tuples()
    return [BezierCurve(Point(points[i][0], points[i][1]),
                        Point((points[i][0] + points[i + 1][0]) / 2, (points[i][1] + points[i + 1][1]) / 2),
                        Point(points[i + 1][0], points[i + 1][1]))
            for i in range(segments)]


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
