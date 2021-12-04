from copy import copy
from unittest import TestCase

from __init__ import Point


class TestPoint(TestCase):
    def test__str__Doit_retourner_des_coordonnées(self):
        # given
        point = Point(1, 2)
        # when
        string = string(point)
        # then
        self.assertEqual('(1,2)', string)

    def test__eq__Doit_retourner_True_Lorsque_les_coordonnées_sont_identiques(self):
        # given
        a = Point(1, 2)
        b = Point(1, 2)
        # when
        equal = a == b
        # then
        self.assertTrue(equal)
    
    def test__add__Doit_additionner_les_coordonnées_termes_a_termes(self):
        # given
        a = Point(1, 1)
        b = Point(2, 3)
        # when
        c = a + b
        # then
        self.assertEqual('(3,4)', str(c))

    def test__copy__Doit_copier_les_coordonnées(self):
        # Given
        a = Point(1, 2)
        b = copy(a)
        # when
        a.x = 2
        b.y = 3
        # then
        self.assertEqual('(2,2)', str(a))
        self.assertEqual('(1,3)', str(b))
