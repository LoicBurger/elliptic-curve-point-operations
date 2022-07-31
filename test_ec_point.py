from ec_point import *


def test_equality():
    assert ECPoint(0x1, 0x1) == ECPoint(0x1, 0x1)


def test_unequality():
    assert not (ECPoint(0x1, 0x2) == ECPoint(0x1, 0x1))


def test_different_object():
    assert not (ECPoint(0x1, 0x2) == "test")


def test_print():
    assert f"{ECPoint(0x1,0x2)}" == '(0x1,0x2)'
