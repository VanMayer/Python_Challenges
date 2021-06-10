import pytest
from wash import wash_hands

def test_wash_hands():
    assert wash_hands(8,7) == '588 minutes and 0 seconds'
    assert wash_hands(6,3) == '661 minutes and 30 seconds'