from ec import *

# Bitcoin elliptic curve parameters
ec = EC(0x3fddbf07bb3bc551, ECPoint(
    0x69d463ce83b758e, 0x287a120903f7ef5c))

G = ec.generator


def test_addition_ec_point_with_itself():
    assert ec.addition(G, G) == ECPoint(
        0x2544b2250b8b1e1c, 0x10fa88c491b36c0b)


def test_addition_two_different_ec_points():
    assert ec.addition(G, ec.multiplication(
        G, 2)) == ECPoint(0x16cc969206bac6ef, 0x2fe18466e8ff225f)


def test_multiplication_by_2():
    assert ec.multiplication(G, 2) == ECPoint(
        0x2544b2250b8b1e1c, 0x10fa88c491b36c0b)


def test_multiplication_by_power_of_2():
    assert ec.multiplication(G, 16) == ECPoint(
        0x3b920b2af8274614, 0x30f51978ed5e3f6b)


def test_multiplication_by_not_power_of_2():
    assert ec.multiplication(G, 6) == ECPoint(
        0x1eb4c74b285a26a0, 0x288e45d8a479a37)
