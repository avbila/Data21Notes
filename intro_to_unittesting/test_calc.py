from simple_calc import SimpleCalc

calc = SimpleCalc()


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(4, 1) == 3
