
def factors(n):
    """ Generator of factors for n
    """
    if n < 1:
        raise ValueError("n must be larger than 0")

    k = 1
    while k*k < n:
        a, b = divmod(n, k)

        if b == 0:
            yield k
            yield a

        k += 1

    if k*k == n:
        yield k

