from geometry.point import Point


class BezierCurve:
    def __init__(self, p0, p1, p2):
        self.start = p0
        self.control = p1
        self.end = p2

    def __str__(self):
        return "(" + str(self.start) + "," + str(self.control) + "," + str(self.end) + ")"

    def __eq__(self, other):
        return self.start == other.start and self.control == other.control and self.end == other.end

    def get_points(self):
        return [self.start, self.control, self.end]

    def get_points_as_tuples(self):
        return [(self.start.x, self.start.y), (self.control.x, self.control.y), (self.end.x, self.end.y)]

    def plot(self, amount: int):
        """
        Given Quadratic Bezier controls points
        Returns a list
        """
        points = []
        for i in range(amount):
            t = i / amount
            x = (1 - t) ** 2 * self.start.x + 2 * (1 - t) * t * self.control.x + t ** 2 * self.end.x
            y = (1 - t) ** 2 * self.start.y + 2 * (1 - t) * t * self.control.y + t ** 2 * self.end.y
            points.append(Point(x, y))
        return points
