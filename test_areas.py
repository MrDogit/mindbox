"""This module is unittest for areas module"""
import unittest
import areas

class TestAreas(unittest.TestCase):
    
    def test_circle(self):
        self.assertAlmostEqual(areas.circle(5.6418958354776), 100)
        self.assertAlmostEqual(areas.circle(10), 314.15926535897932384626433)
    
    def test_triangle(self):
        self.assertEqual(areas.triangle(3, 4, 5), 6)

if __name__ == '__main__':
    unittest.main()