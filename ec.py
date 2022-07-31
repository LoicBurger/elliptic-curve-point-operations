from typing import List
from euclidian_algorithm import *
from ec_point import ECPoint


class EC:
    def __init__(self, field: int, generator: ECPoint):
        self.field = field
        self.generator = generator

    # Addition of two elliptic curve points A and B, knowing the field of the
    # ellpitic curve, p
    def addition(self, A: ECPoint, B: ECPoint) -> ECPoint:
        S = ECPoint(0, 0)
        p = self.field

        if A == B:
            L = (3*A.x*A.x) * find_inverse_mod_prime(2*A.y, p) % p
        else:
            L = (B.y-A.y) * find_inverse_mod_prime(B.x-A.x, p) % p

        S.x = (L*L - A.x - B.x) % p
        S.y = (L*(A.x - S.x) - A.y) % p
        return S

    # Multiplication of elliptic curve point A, k times, where k is a scalar

    def multiplication(self, A: ECPoint, k: int) -> ECPoint:
        B = ECPoint(0, 0)
        flag_lowest_non_zero_bit = 1

        for i in range(len(bin(k))-2):
            if bin(k)[len(bin(k))-1-i] == '1':
                if flag_lowest_non_zero_bit == 1:
                    B = A
                    flag_lowest_non_zero_bit = 0
                else:
                    B = self.addition(A, B)
            A = self.addition(A, A)
        return B
