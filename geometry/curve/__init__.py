def get_points_from_curves(curves):
    points = []
    for curve in curves:
        points += curve.get_points()
    return points
