import pytest
from numbers_station_coded_messages import solution
def test_case1():
    assert solution([4,5,10,2,8],12) == [2,3]

def test_case2():
    assert solution([1,2,3,4],15) == [-1, -1]

def test_case3():
    assert solution([1],1) == [0, 0]

