from datetime import date
import logging
from trivial_functions import mod_ten_of_double

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def mod_two_of_mod_ten_of_double(some_number):
    return mod_ten_of_double(some_number) % 2


def mod_ten_of_double_is_even(some_number):
    return mod_two_of_mod_ten_of_double(some_number) == 0


def prepend_date_to_log_msg(msg):
    timestamp = date.strftime(date.today(), "%m-%d-%Y")
    logger.info(f'{timestamp}: {msg}')


def log_msg_if_string_otherwise_noop(msg):
    if isinstance(msg, str):
        prepend_date_to_log_msg(msg)


def log_date_before_msg(msg):
    timestamp = date.strftime(date.today(), "%m-%d-%Y")
    logger.info(f'{timestamp}:')
    logger.info(msg)


def unpack_kwargs_values(**kwargs):
    return list(kwargs.values())


def redundant_proxy_function(a, b, c, d):
    first = unpack_kwargs_values(a=a, b=b)
    second = unpack_kwargs_values(c=c, d=d)
    return first, second
