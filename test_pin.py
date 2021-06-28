import pytest
from pin import validpin

def test_validpin():
    assert validpin("1234") == True
    assert validpin("45135") == False
    assert validpin("89abc1") == False
    assert validpin("900876") == True
    assert validpin(" 4983") == False
    assert validpin(" ") == False