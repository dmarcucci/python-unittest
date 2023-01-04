import trivial_functions
import unittest
from unittest.mock import Mock, patch

multiply_by_two_mock = Mock()


class TestTrivialFunctionsBasicVersion(unittest.TestCase):
    def test_multiply_by_two(self):
        self.assertEqual(trivial_functions.multiply_by_two(10), 20)
        self.assertEqual(trivial_functions.multiply_by_two(5), 10)
        self.assertEqual(trivial_functions.multiply_by_two(1), 2)

    def test_mod_ten_of_double_without_mock(self):
        self.assertEqual(trivial_functions.mod_ten_of_double(10), 0)
        self.assertEqual(trivial_functions.mod_ten_of_double(14), 8)
        self.assertEqual(trivial_functions.mod_ten_of_double(1), 2)

    @patch('trivial_functions.multiply_by_two', multiply_by_two_mock)
    def test_mod_ten_of_double_with_mock(self):
        # Given
        multiply_by_two_mock.return_value = 20
        # When
        result = trivial_functions.mod_ten_of_double(10)
        # Then
        multiply_by_two_mock.assert_called_once_with(10)
        self.assertEqual(result, 0)
