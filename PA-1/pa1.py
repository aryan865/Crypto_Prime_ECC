import math
from functools import lru_cache
import sys

sys.setrecursionlimit(10**7)


def factorial(n, p):
    """return factorial of n mod p"""
    return (n * factorial(n - 1, p)) % p if n > 1 else 1

# FASTEST WAY TO CHECK PRIME
# def is_prime(x: int) -> int:
#     if x < 2:
#         return 0
#     if x in (2, 3):
#         return 1
#     if x % 2 == 0 or x % 3 == 0:
#         return 0
#     i = 5
#     while i * i <= x:
#         if x % i == 0 or x % (i + 2) == 0:
#             return 0
#         i += 6
#     return 1


def is_prime(x):
    """check if x is prime using wilson's theorem"""
    if x < 2:
        return 0
    # wilson's theorem
    val = (factorial(x-1, x) + 1)
    if val == x:
        return 1
    return 0


@lru_cache(maxsize=None)
def num_primes_less_than(i):
    """return number of primes less than or equal to i"""
    if i < 2:
        return 0

    return num_primes_less_than(i - 1) + is_prime(i)


def nth_prime(n):
    """return the nth prime number"""
    # the new upper bound does not work for n < 6, so hard code
    if n < 6:
        return [2, 3, 5, 7, 11][n-1]

    # Rosser–Schoenfeld bound
    upper_bound = math.ceil(n * (math.log(n) + math.log(math.log(n))))

    value = 2  # 1 included
    for i in range(2, upper_bound+1):
        value += math.floor((n/(num_primes_less_than(i) + 1)) ** (1/n))

    return value


if __name__ == "__main__":
    # for k in range(2, 1001):
    k = int(input("Enter n to find nth prime: "))
    print(f"{k}th prime = {nth_prime(k)}")