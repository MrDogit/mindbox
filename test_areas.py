"""This module is unittest for areas module"""
import unittest
import areas

class TestAreas(unittest.TestCase):
    
    def test_circle(self):
        self.assertAlmostEqual(areas.Circle(5.6418958354776).area, 100)
        self.assertAlmostEqual(areas.Circle(10).area, 314.15926535897932384626433)
    
    def test_triangle(self):
        self.assertEqual(areas.Triangle(3, 4, 5).area, 6)
        self.assertEqual(areas.Triangle(3, 4, 5).is_right, True)
        self.assertEqual(areas.Triangle(3, 4, 6).is_right, False)


if __name__ == '__main__':
    unittest.main()