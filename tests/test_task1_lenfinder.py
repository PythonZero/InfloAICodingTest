import pytest
from tasks.task1_len_finder import LenFinder


@pytest.mark.parametrize(
    "number,expected", [  # (0, (0, 1)),  # empty list
        (99, (10, 100)),
        (100, (10, 100)),
        (10 ** 6 - 1, (10 ** 5, 10 ** 6)),
        (10 ** 6, (10 ** 5, 10 ** 6)),
        (654325, (100000, 1000000))
    ]
)
def test_find_max_size_factor_10(number, expected):
    container = [i for i in range(1, number + 1)]
    assert expected == LenFinder._find_max_size_factor_10(container)


@pytest.mark.parametrize(
    "expected,min,max", [
        # (0, 0, 1),  # empty list
        (99, 10, 100),
        (100, 100, 1000),
        (10 ** 6 - 1, 10 ** 5, 10 ** 6),
        (10 ** 6, 10 ** 6, 10 ** 7),
        (654325, 100000, 1000000),
    ])
def test_binary_search_len(expected, min, max):
    container = [i for i in range(1, expected + 1)]
    assert expected == LenFinder._binary_search_len(container, min, max)


@pytest.mark.parametrize(
    "number", [99, 100, (10 ** 6 - 1), (10 ** 6), 654325, 74,
               63, 321, 76584, 89457]
)
def test_lenfinder(number):
    container = [i for i in range(1, number + 1)]
    assert number == LenFinder(container)


def test_lenfinder_mixed_obj_types():
    assert 5 == LenFinder(['bob', 'mike', 'jack', 31, 18])


@pytest.mark.parametrize(
    "number", [31, 84, 856, 8346, 5863, 100]
)
def test_lenfinder_different_containers(number):
    containers = [
        tuple(i for i in range(1, number + 1)),
        list(i for i in range(1, number + 1))
    ]
    for container in containers:
        assert number == LenFinder(container)
