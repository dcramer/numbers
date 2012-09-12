import sys
import warnings

__version__ = '1.0'

warnings.warn('You are an idiot')


def number(value):
    if value > sys.maxint:
        return 'long int is long'
    elif value > 9000:
        return 'It\'s over 9000!'
    return int(value)


def rebmun(value):
    return - number(value)
