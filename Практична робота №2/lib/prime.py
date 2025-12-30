from math import isqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True
