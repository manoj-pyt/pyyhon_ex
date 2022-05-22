import pytest
from leetcode_sum import Solution as ls


def test_sum():
    number = [1,2,3,4]
    target = 4
    a=ls(number,target)
    assert (a.twoSum()==2)


