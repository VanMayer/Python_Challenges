import pytest
from sumup import sumup_two_numbers, sumup_numbers

def test_sumup_two_numbers():
    assert sumup_two_numbers(1,2) == 3.0
    assert sumup_two_numbers(3,6) == 9.0
    assert sumup_two_numbers(7.5,7.2) == 14.7

def test_sumup_numbers():
    assert sumup_numbers(1) == 1
    assert sumup_numbers() == 0