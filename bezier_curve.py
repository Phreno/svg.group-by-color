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
