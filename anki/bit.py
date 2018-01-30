""" Questions about bit manipulation.
"""


def hamming_distance(x, y):
    """ Standard Hamming distance of two sequence of same length.

    :param x: First sequence such as a string.
    :param y: Second sequence
    :return:
    """
    if len(x) != len(y):
        raise ValueError("Two sequences must have same length")
    else:
        dist = sum([ex != ey for ex, ey in zip(x, y)])
        return dist


def hamming_distance_int(x: int, y: int) -> int:
    """ Find Hamming distance of two integers.

    :param x:
    :param y:
    :return:
    """
    diff = x ^ y
    count = 0

    while diff != 0:
        # increment the cound
        count += 1
        # clear the least significant bit
        diff &= diff - 1

    return count


def hamming_weight(x: int) -> int:
    """ Hamming weight is effectively Hamming distance between x and 0.
    """
    count = 0

    while x != 0:
        # increment the cound
        count += 1
        # clear the least significant bit
        x &= x - 1

    return count


def add(a, b):
    """ Add two integers using bit manipulation.
    x + y = x^y + (x&y) << 1
    """
    while a != 0:
        a, b = (a & b) << 1, a ^ b
        # print("{} {}".format(x, y))
    return b


def subtract(a, b):
    """ Sutract two integers using bit manipulation
    x - y = x^y - (~x & y)<<1
    """
    # This does NOT work for negative result in Python
    # Due to a number in Python is an unbounded bit sequence
    assert a >= b
    while b != 0:
        a, b = a ^ b, (~a & b) << 1
    return a


def abs(a):
    """ Get absolute value of 32-bit integer without branching.
    For two's complement form:
    absolute value of a negative number = toggle bits of the number and add 1 to the result.
    """
    # Mask will be all 1s (value=-1) for negative integers,
    # all 0s (value=0) for positive integer.
    mask = a >> 31
    return a ^ mask - mask
