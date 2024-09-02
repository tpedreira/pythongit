def is_prime(num):
    """Checks if a given number is prime.

    Args:
        num: The positive integer to check.

    Returns:
        True if num is prime, False otherwise.
    """

    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True
is_prime(11)