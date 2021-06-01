import pytest
from strings import stringupper

def test_stringupper():
    assert stringupper('tree') =='TREE'
    assert stringupper('flower') =='FLOWER'
    assert stringupper(False) =='Input must be a string'