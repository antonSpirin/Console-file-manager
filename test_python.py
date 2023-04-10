import math
from library import names_friends, numbers_list, pow_list, dict_for_sorted


def test_filter():
    assert list(filter(lambda x: x[0].lower() in 'aeouiy', names_friends)) == ['Ilya', 'Andry', 'Oleg']
    assert list(filter(lambda x: x[0].lower() in 'qwrtpsdfghjklzxcvbnm', names_friends)) == ['Roman', 'Petr', 'Maks']


def test_map():
    assert list(map(pow, numbers_list, pow_list)) == [2, 9, 64]
    assert len(list(map(pow, numbers_list, pow_list))) == len(pow_list)


def test_sorted():
    assert sorted(dict_for_sorted) == ['A: 1', 'C: 8', 'F: 6', 'G: 9']


def test_pi():
    r = 3
    P = 2 * 3.141592653589793 * r
    assert math.pi == P / (2 * r)


def test_sqrt():
    num = 16
    sqrt = num ** (0.5)
    assert math.sqrt(num) == sqrt


def test_pow():
    num = 4
    degree = 2
    assert pow(num, degree) == num ** (degree)
    assert math.sqrt(pow(num, degree)) == num


def test_hypot():
    x = 5
    y = 7
    assert math.hypot(x, y) == (x * x + y * y) ** (0.5)
    
