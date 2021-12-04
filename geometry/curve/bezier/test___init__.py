from unittest import TestCase

from . import BezierCurve
from ...point import Point


class TestBezierCurve(TestCase):
    def setUp(self):
        self.start = Point(1, 1)
        self.control = Point(2, 2)
        self.end = Point(3, 3)


    def test__str__Doit_afficher_les_trois_points_de_controles(self):
        # given a curve
        curve = BezierCurve(self.start,self.control, self.end)
        # when the curve is printed
        data = str(curve)
        # then it displays all the 3 points
        self.assertEqual('((1,1),(2,2),(3,3))', data)

    def test__eq__Doit_retourner_True_Lorsque_les_coordonnées_sont_identiques(self):
        # given twos curves with same points
        a = BezierCurve(self.start,self.control,self.end)
        b = BezierCurve(self.start,self.control,self.end)
        # when we try a comparison
        res = a == b
        # then the curves have to be equals
        self.assertTrue(res)

    def test_get_points_Doit_retourner_un_tableau_de_points(self):
        # given a curve
        curve = BezierCurve(self.start, self.control, self.end)
        # when we get points
        points = curve.get_points()
        # then the points keep the same order
        self.assertEqual([self.start, self.control, self.end], points)

    def test_plot_Doit_retourner_un_nombre_de_points_identiques_a_la_quantité_fournie(self):
        # given a curve
        curve = BezierCurve(self.start, self.control, self.end)
        # when we plot points
        points = curve.plot(3)
        # then we keep 3 points
        self.assertEqual(points[0].x, self.start.x)
        self.assertEqual(points[0].y, self.start.y)
        self.assertNotEqual(points[1].x, self.control.x)
        self.assertNotEqual(points[1].y, self.control.y)
        self.assertNotEqual(points[2].x, self.end.x)
        self.assertNotEqual(points[2].y, self.end.y)