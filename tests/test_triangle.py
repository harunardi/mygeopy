import numpy as np
import numbers
import doctest

def test_hypot():
    from mygeopy.triangle import hypot

    assert hypot(3, 4) == 5
    assert hypot(5, 12) == 13
    assert hypot(-8, 15) == 17

# run pytest -> `pytest` in command line
# run doctest -> `pytest --doctest-modules` in command line