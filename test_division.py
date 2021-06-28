import pytest
from division import division

def test_division():
    assert division(4,2) == 2
    assert division(6,3) == 2
    assert division(7.5,0) == 'This is not possible'