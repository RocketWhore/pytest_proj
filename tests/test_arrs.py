from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

    assert arrs.my_slice([5,6,7,8], -2) == [7, 8]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([5,6,7,8], -15) == [5,6,7,8]