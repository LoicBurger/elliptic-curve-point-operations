# Elliptic curve point operations

The repository concerns the implementation of the addition of two points on the elliptic curve and the multiplication of a point on the elliptic curve by a scalar. 

# How to use

```python
from ec import *


# Declare the finite field and the generator of the elliptic curve.
field = 0x3fddbf07bb3bc551
G = ECPoint(0x69d463ce83b758e, 0x287a120903f7ef5c)
ec = EC(field, G))


# Compute A = G+G, where G is the generator
A = ec.addition(G, G)


# Compute B = 5*G, where G is the generator
k = 5
B = ec.multiplication(G, k)
```

Note: In cryptography, a key-pair is for instance (k, k * G), where k is the private key and k * G is the public key, knowing G. The knowledge of k * G does not allow for an easy retrival of k, if k is sufficiently large.   

# Context and objective

An elliptic curve on the real numbers is a curve of the form y<sup>2</sup> = x<sup>3</sup> + a*x + b. For instance, the bitcoin elliptic curve can be recovered by taking a=0 and b=7. 

Such a curve is obviously composed of infinitely many points. However, if the elliptic curve equation holds only for a limited number of points if it is taken modulo p, where p is a prime number that is called the field of the elliptic curve. Moreover, finding the points that verify the elliptic curve equation modulo p is much less straightforward than finding a point on the elliptic curve over the real numbers, especially if the field is large.

In elliptic curves are particularly useful in cryptography, since they contribute to speeding up the calculations. Moreover, while it is easy, knowing a point A and the value of k, to compute the elliptic-curve point k * A, it is computationally difficult to find k, knowing A and the point k * A. Such a property is paramount for cryptographic applications.

In what follows, an efficient algorithm to compute k * A, knowing A and k, is implemented.

# Algorithm
## Elliptic curve point addition

Multiplying a point of the elliptic curve A by an integer k is equivalent to computing the sum A+A+A+...+A, k times. The notion of addition of two points A and B on an elliptic curve is equivalent to finding the intersection point of the line AB with the elliptic curve, which exists and is unique and is denoted by S. Note that in the case where A and B are the same point, the line that enables the definition of S is the tangent to the elliptic curve at point A. 

In practice, this can be done using the coordinates of the two points, using the equations 
```
    S.x = (L*L - A.x - B.x) mod p
    S.y = (L*(A.x - S.x) - A.y) mod p,
```
where
```
    L = (3*A.x*A.x) / (2*A.y) mod p
```
if A = B, and 
```
    L = (B.y-A.y) / (B.x-A.x) mod p
```
if A and B are different. The inverses modulo p are efficiently computed by means of the Euclidian algorithm.

## Double-and-add

Instead of repeating k times an addition operation to obtain the result of k * A, one can speed the process by using the double-and-add algorithm. This approach consists in exploiting the fact that 
```
2^i*A + 2^i*A = 2^(i+1)*A.
````
 Then, one can simply use the decomposition of k in base 2, progressively computing 2<sup>i</sup> * A from a single addition of 2<sup>i-1</sup> * A with itself, and then updating the result by adding 2<sup>i</sup> * A to the current value of the answer if 2<sup>i</sup> appears in the base-2 decomposition of k. k * A is then computed in O(log<sub>2</sub>(n)) additions instead of O(n) additions.  

 For example, if k = 81, which is can be rewritten as 2<sup>6</sup>+2<sup>4</sup>+1, the result of k * A can be obtained using 8 elliptic curve additions (6 for computing the points 2<sup>i</sup> * A, and two to obtain k * A from the base-2 decomposition of 81), instead of 80 successive additions.


# Perspectives

The algorithm could directly compute the generator from the coefficient of the elliptic curve equation. 

# Developer
## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Launch tests

```bash
# Launch all the tests
pytest

# Run tests with coverage
pytest --cov --cov-report term-missing

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
ec.py                       27      0   100%
ec_point.py                 10      0   100%
euclidian_algorithm.py      19      0   100%
test_ec.py                  13      0   100%
test_ec_point.py             9      0   100%
------------------------------------------------------
TOTAL                       78      0   100%

```