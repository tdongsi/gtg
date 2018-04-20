
def find_brute(text:str, subs: str):
    """ Pattern matching with brute force.
    Return the lowest index of text T at which substring P begins (or else -1).

    :param text: text T
    :param subs: substring P
    :return: lowest index of T
    """
    if not text or not subs:
        return -1

    n, m = len(text), len(subs)

    for i in range(n - m + 1):
        k = 0
        while k < m and text[i+k] == subs[k]:
            k += 1
        if k == m:
            return i

    return -1

