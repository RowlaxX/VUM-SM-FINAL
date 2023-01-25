import unittest

from unittest import TestCase
from Space import Point3D


class Point3DTest(TestCase):
    def testAdd(self):
        p1 = Point3D(4, 3, 0)
        p2 = Point3D(1, 3, -3)
        p3 = Point3D(5, 6, -3)
        self.assertEqual(p1 + p2, p3)

    def testSub(self):
        p1 = Point3D(6, 2, 1)
        p2 = Point3D(9, 0, -2)
        p3 = Point3D(-3, 2, 3)
        self.assertEqual(p1 - p2, p3)

    def testAbs(self):
        p1 = Point3D(6, 3, 2)
        self.assertEqual(abs(p1), 7)

    def testDist(self):
        p1 = Point3D(10, 10, 0)
        p2 = Point3D(-10, 10, 0)
        self.assertEqual(p1.distance(p2), 20)

    def testRepr(self):
        p1 = Point3D(1, 2, 3)
        print(p1)
        self.assertEqual(str(p1), "Point3D (x=1 y=2 z=3)")


unittest.main()
