import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def fermat_little_theorem_test(n, k=5):
    if n <= 1 or n == 4:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1:
            return False
        if mod_pow(a, n - 1, n) != 1:
            return False

    return True

number_to_test = 63999999
result_flt = fermat_little_theorem_test(number_to_test)
print(f"{number_to_test} is {'probably prime' if result_flt else 'composite'}")
