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