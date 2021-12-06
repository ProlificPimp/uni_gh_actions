from functools import reduce
from random import randint, seed, uniform
from funcs import find_min, find_max, find_sum, find_prod, read_file
import operator
from decimal import Decimal



def test_find_min():
    assert find_min([Decimal('1'), Decimal('10'), Decimal('20')]) == Decimal('1')
    assert find_min([Decimal('0'), Decimal('10'), Decimal('40'), Decimal('30')]) == Decimal('0')
    assert find_min([Decimal('-5'), Decimal('-10'), Decimal('-99')]) == Decimal('-99')
    assert find_min([Decimal('-8'), Decimal('-10'), Decimal('-86'), Decimal('0')]) == Decimal('-86')
    assert find_min([Decimal('0'), Decimal('5.4'), Decimal('1'), Decimal('6')]) == Decimal('0')

def test_find_max():
    assert find_max([Decimal('1'), Decimal('10'), Decimal('2.10')]) == Decimal('10')
    assert find_max([Decimal('0'), Decimal('10'), Decimal('40.2'), Decimal('30')]) == Decimal('40.2')
    assert find_max([Decimal('-5'), Decimal('-10'), Decimal('-99')]) == Decimal('-5')
    assert find_max([Decimal('-8'), Decimal('-10'), Decimal('-86'), Decimal('0')]) == Decimal('0')
    assert find_max([Decimal('0'), Decimal('5'), Decimal('1'), Decimal('-16')]) == Decimal('5')

def test_find_sum():
    assert find_sum([Decimal('0'), Decimal('10'), Decimal('20')]) == Decimal('31')
    assert find_sum([Decimal('0'), Decimal('10'), Decimal('40'), Decimal('30')]) == Decimal('80')
    assert find_sum([Decimal('-5'), Decimal('-10'), Decimal('-99')]) == Decimal('-114')
    assert find_sum([Decimal('-8'), Decimal('-10'), Decimal('-86'), Decimal('0')]) == Decimal('-104')
    assert find_sum([Decimal('0'),Decimal('5'), Decimal('3.2'), Decimal('-6')]) == Decimal('2.2')

def test_find_prod():
    assert find_prod([Decimal('0'), Decimal('-10'), Decimal('2.0')]) == Decimal('0')
    assert find_prod([Decimal('1'), Decimal('10'), Decimal('2'), Decimal(2)]) == Decimal('40')
    assert find_prod([Decimal('-1'), Decimal('-10'), Decimal('-99')]) == Decimal('-990')
    assert find_prod([Decimal('5'), Decimal('2')]) == Decimal('10')
    assert find_prod([Decimal('33'), Decimal('-5')]) == Decimal('-165')
    assert find_prod([Decimal('3.3'), Decimal('-5')]) == Decimal('-16.5')
    assert find_prod([Decimal('1'), Decimal('5')]) == Decimal('5')

def test_stress():
    seed(44)

    for i in range(100):
        res = []
        for i in range(500):
            res.append(Decimal(str(randint(9, 9999999999999))))
        assert find_min(res) == min(res)
        assert find_max(res) == max(res)
        assert find_sum(res) == sum(res)
        assert find_prod(res) == reduce(operator.mul, res, 1)

    for i in range(100):
        res = []
        for i in range(500):
            res.append(Decimal(str(uniform(1, 99999))))
        assert find_min(res) == min(res)
        assert find_max(res) == max(res)
        assert find_sum(res) == sum(res)
        assert find_prod(res) == reduce(operator.mul, res, 1)

def test_read_file():
    f = open('nums.txt', 'w')
    f.write('1 4 5 1 3 4 3')
    f.close()
    assert read_file('nums.txt') == [Decimal('1'), Decimal('4'), Decimal('5'), Decimal('1'), Decimal('3'), Decimal('4'), Decimal('3')]

    f = open('nums.txt', 'w')
    f.write(' 1 3 -3 2')
    f.close()
    assert read_file('nums.txt') == [Decimal('1'), Decimal('3'), Decimal('-3'), Decimal('2')]

    f = open('nums.txt', 'w')
    f.write('234 0.4 13 33')
    f.close()
    assert read_file('nums.txt') == [Decimal('234'), Decimal('0.4'), Decimal('13'), Decimal('33')]

    f = open('nums.txt', 'w')
    f.write('1 a 45 234 2342')
    f.close()
    assert read_file('nums.txt') == 'Error'

    assert read_file('nums2.txt') == 'Error'

