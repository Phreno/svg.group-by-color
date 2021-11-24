class BezierCurve:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "(" + str(self.p0) + "," + str(self.p1) + "," + str(self.p2) + ")"

    def __eq__(self, other):
        return self.p0 == other.p0 and self.p1 == other.p1 and self.p2 == other.p2

    def get_points(self):
        return [self.p0, self.p1, self.p2]

    def get_points_as_tuples(self):
        return [(self.p0.x, self.p0.y), (self.p1.x, self.p1.y), (self.p2.x, self.p2.y)]
