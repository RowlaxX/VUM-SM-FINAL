import math
import unittest

from math import degrees
from math import pi
from unittest import TestCase


class DegreeCoverage(TestCase):
    def test1(self):
        x = math.degrees(pi)
        self.assertEqual(x, 180)


unittest.main()
