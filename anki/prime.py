
import random


def decompose(num):
    """ Decompose num = 2**exp * d where d is odd.

    :param num: the input number.
    :return: (exp, d) where num = 2**exp * d
    """
    exp = 0
    while num & 1 == 0:  # check num % 2 == 0 but probably faster
        num >>= 1
        exp += 1
    return exp, num


def is_prime(number, trial=10):
    """ Rabin Miller test of primality.

    :param number: the input number.
    :param trial: Number of Rabin-Miller trial.
    :return: True if all trials passed, False if not.
    """

    # small primes < 100
    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def rabin_miller_trial(n):
        """ Check if prime pass the Rabin-Miller trial.

        :param n: a random "witness" of primality.

        :return: True if composite, False if probably prime.
        """
        n = pow(n, d, number)

        # For first iteration, 1 or -1 remainder implies prime
        if n == 1 or n == number - 1:
            return False

        # For next iterations, -1 implies prime, others imply composite
        for _ in range(s):
            n = pow(n, 2, number)
            if n == number - 1:
                return False

        return True

    # Labor saving steps
    if number < 2:
        return False
    for p in SMALL_PRIMES:
        if p * p > number:
            # if input is small enough for small primes
            return True
        if number % p == 0:
            return False

    # Starting Rabin-Miller algorithm
    s, d = decompose(number - 1)

    for _ in range(trial):
        num = random.randint(2, number - 2)
        if rabin_miller_trial(num):
            return False

    return True
