Numbers for Humans
==================

Because sometimes using builtins is hard.


Usage
-----

>>> import numbers
>>> number(1)
1

Simple comparisons:

>>> number(1) < number(2)
True

Complicated math:

>>> number(1) * number(50) / number(25)
2

Real results:

>>> number(sys.maxint)
"It's over 9000!"

Credits
-------

This project was inspired by `prices <https://github.com/mirumee/prices>`_, because sometimes programming should be as
easy as using MongoDB.