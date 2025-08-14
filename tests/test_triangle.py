import numpy as np
import numbers

def test_hypot():
    from mygeopy.triangle import hypot

    assert hypot(3, 4) == 5
    assert hypot(5, 12) == 13
    assert hypot(-8, 15) == 17