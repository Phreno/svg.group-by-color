#!/usr/bin/python3


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
