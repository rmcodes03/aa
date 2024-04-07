import math

def pollards_p_minus_1(n, max_iter=1000):
    """Pollard's p-1 factorization algorithm."""
    a = 2

    for j in range(2, max_iter + 1):
        a = pow(a, j, n)
        d = math.gcd(a - 1, n)

        if 1 < d < n:
            return d  # Found a non-trivial factor

    return None  # Failed to find a factor within the given iterations

def factorize(n):
    """Factorize a number using Pollard's p-1 algorithm."""
    factors = []

    while n > 1:
        factor = pollards_p_minus_1(n)
        if factor:
            factors.append(factor)
            n //= factor
        else:
            factors.append(n)
            break

    return factors

if __name__ == "__main__":
    # Example usage
    number_to_factorize = 4712

    factors = factorize(number_to_factorize)

    if len(factors) == 1:
        print(f"{number_to_factorize} is prime.")
    else:
        print(f"Factors of {number_to_factorize}: {factors}")
