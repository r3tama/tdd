import unittest
import pytest
from function import mostRepetitiveInteger

EMPTY_TESTING_LIST = []
ONE_ELEMENT_LIST = [2]


@pytest.mark.parametrize("input,expected", [

([1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3],1),
([6,7,4,3,2,2,3,4,2,5,6,8,2,2,2,6,2],2),
([1,1,1,1,2,2,2,2],1),

])
def test_given_correct_list(input,expected):
    assert mostRepetitiveInteger(input) == expected

def test_given_empty_list():
    with pytest.raises(ValueError):
        mostRepetitiveInteger(EMPTY_TESTING_LIST)

def test_given_one_item_list():
    assert mostRepetitiveInteger(ONE_ELEMENT_LIST) == 2
