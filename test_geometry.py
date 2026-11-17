import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)

    def test_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_area_with_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_perimeter_with_equal_sides(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_area_with_zero_height(self):
        self.assertEqual(triangle.area(6, 0), 0)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_with_equal_sides(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)


if __name__ == "__main__":
    unittest.main()
