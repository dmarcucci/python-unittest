from datetime import date
from more_trivial_functions import mod_two_of_mod_ten_of_double, mod_ten_of_double_is_even, prepend_date_to_log_msg, \
    log_msg_if_string_otherwise_noop, log_date_before_msg, unpack_kwargs_values, redundant_proxy_function
import more_trivial_functions
import unittest
from unittest.mock import Mock, patch

date_mock = Mock()
logger_mock = Mock()
mod_ten_of_double_mock = Mock()
mod_two_of_mod_ten_of_double_mock = Mock()
prepend_date_to_log_msg_mock = Mock()
unpack_kwargs_values_mock = Mock()


@patch('more_trivial_functions.mod_ten_of_double', mod_ten_of_double_mock)
class TestMoreTrivialFunctionsBasicVersion(unittest.TestCase):
    def setUp(self):
        self.mock_logger = patch.object(more_trivial_functions, 'logger', logger_mock)

    def tearDown(self):
        date_mock.reset_mock()
        logger_mock.reset_mock()

    def test_mod_two_of_mod_ten_of_double(self):
        # Given
        mod_ten_of_double_mock.return_value = 5
        # When
        result = mod_two_of_mod_ten_of_double(60)
        # Then
        mod_ten_of_double_mock.assert_called_once_with(60)
        self.assertEqual(result, 1)

    @patch('more_trivial_functions.mod_two_of_mod_ten_of_double', mod_two_of_mod_ten_of_double_mock)
    def test_mod_ten_of_double_is_even_true_case(self):
        # Given
        mod_two_of_mod_ten_of_double_mock.return_value = 0
        # When
        result = mod_ten_of_double_is_even(87)
        # Then
        mod_two_of_mod_ten_of_double_mock.assert_called_once_with(87)
        self.assertTrue(result)
        # Cleanup
        mod_two_of_mod_ten_of_double_mock.reset_mock()

    @patch('more_trivial_functions.mod_two_of_mod_ten_of_double', mod_two_of_mod_ten_of_double_mock)
    def test_mod_ten_of_double_is_even_false_case(self):
        # Given
        mod_two_of_mod_ten_of_double_mock.return_value = 1
        # When
        result = mod_ten_of_double_is_even(87)
        # Then
        mod_two_of_mod_ten_of_double_mock.assert_called_once_with(87)
        self.assertFalse(result)
        # Cleanup
        mod_two_of_mod_ten_of_double_mock.reset_mock()

    @patch('more_trivial_functions.date', date_mock)
    def test_prepend_date_to_log_msg(self):
        with self.mock_logger:
            # Given
            msg = "Message"
            # And
            today = date.fromisoformat('2023-01-01')
            date_mock.today.return_value = today
            date_mock.strftime.return_value = '01-01-2023'
            # When
            prepend_date_to_log_msg(msg)
            # Then
            date_mock.today.assert_called_once()
            date_mock.strftime.assert_called_once_with(today, "%m-%d-%Y")
            logger_mock.info.assert_called_once_with(f'01-01-2023: {msg}')

    @patch('more_trivial_functions.prepend_date_to_log_msg', prepend_date_to_log_msg_mock)
    def test_log_msg_if_string_otherwise_noop_noop_case(self):
        # Given
        msg = 1234
        # When
        log_msg_if_string_otherwise_noop(msg)
        # Then
        prepend_date_to_log_msg_mock.assert_not_called()
        # Cleanup
        prepend_date_to_log_msg_mock.reset_mock()

    @patch('more_trivial_functions.prepend_date_to_log_msg', prepend_date_to_log_msg_mock)
    def test_log_msg_if_string_otherwise_noop_string_case(self):
        # Given
        msg = 'msg'
        # When
        log_msg_if_string_otherwise_noop(msg)
        # Then
        prepend_date_to_log_msg_mock.assert_called_once_with(msg)
        # Cleanup
        prepend_date_to_log_msg_mock.reset_mock()

    @patch('more_trivial_functions.date', date_mock)
    def test_log_date_before_msg(self):
        with self.mock_logger:
            # Given
            msg = "Message"
            # And
            today = date.fromisoformat('2023-01-01')
            date_mock.today.return_value = today
            date_mock.strftime.return_value = '01-01-2023'
            # When
            log_date_before_msg(msg)
            # Then
            date_mock.today.assert_called_once()
            date_mock.strftime.assert_called_once_with(today, "%m-%d-%Y")
            self.assertTrue(len(logger_mock.info.mock_calls) == 2)
            self.assertTrue(logger_mock.info.mock_calls[0].args == ('01-01-2023:',))
            self.assertTrue(logger_mock.info.mock_calls[1].args == (msg,))

    def test_unpack_kwargs_values(self):
        self.assertEqual(["Alpha", "Beta", "Charlie"],
                         unpack_kwargs_values(a="Alpha", b="Beta", c="Charlie"))

    @patch('more_trivial_functions.unpack_kwargs_values', unpack_kwargs_values_mock)
    def test_redundant_proxy_function(self):
        # Given
        unpack_kwargs_values_mock.return_value = ["Mock", "list"]
        # When
        result = redundant_proxy_function("aVal", "bVal", "cVal", "dVal")
        # Then
        self.assertTrue(len(unpack_kwargs_values_mock.mock_calls) == 2)
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[0].args == ())
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[0].kwargs == {'a': "aVal", 'b': "bVal"})
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[1].args == ())
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[1].kwargs == {'c': "cVal", 'd': "dVal"})
        self.assertEqual((["Mock", "list"], ["Mock", "list"]), result)
        # Cleanup
        unpack_kwargs_values_mock.reset_mock()

    @patch('more_trivial_functions.unpack_kwargs_values', unpack_kwargs_values_mock)
    def test_redundant_proxy_function_using_side_effect(self):
        # Given
        unpack_kwargs_values_mock.side_effect = [["List", "1"], ["List", "2"]]
        # When
        result = redundant_proxy_function("aVal", "bVal", "cVal", "dVal")
        # Then
        self.assertTrue(len(unpack_kwargs_values_mock.mock_calls) == 2)
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[0].args == ())
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[0].kwargs == {'a': "aVal", 'b': "bVal"})
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[1].args == ())
        self.assertTrue(unpack_kwargs_values_mock.mock_calls[1].kwargs == {'c': "cVal", 'd': "dVal"})
        self.assertEqual((["List", "1"], ["List", "2"]), result)
        # Cleanup
        unpack_kwargs_values_mock.reset_mock(side_effect=True)
