from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist")
    else:
        return x % m

def chinese_remainder_theorem(n, a):
    # n: list of pairwise coprime numbers
    # a: remainders
    prod = 1
    for ni in n:
        prod *= ni

    result = 0
    for ni, ai in zip(n, a):
        pi = prod // ni
        result += ai * mod_inverse(pi, ni) * pi

    return result % prod

# Example usage:
n_values = [3, 5, 7]
a_values = [2, 3, 2]

result_crt = chinese_remainder_theorem(n_values, a_values)
print("Chinese Remainder Theorem Result:", result_crt)
