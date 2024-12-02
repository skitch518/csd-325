import unittest
from city_function import format_location

class TestCityFunction(unittest.TestCase):
    # Tests for city_function.py

    def test_format_location(self):
        # Test 1
        formatted_location = format_location('tokyo', 'japan')
        self.assertEqual(formatted_location, 'Tokyo, Japan')

        # Test 2
        formatted_location = format_location('london', 'england')
        self.assertEqual(formatted_location, 'London, England')

        # Test 3
        formatted_location = format_location('paris', 'france')
        self.assertEqual(formatted_location, 'Paris, France')

if __name__ == '__main__':
    unittest.main()

