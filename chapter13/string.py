
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


def find_boyer_moore(text:str, subs:str):
    """ Pattern matching with Boyer-Moore algorithm.
    Return the lowest index of text T at which substring P begins (or else -1).

    :param text: text T
    :param subs: substring P
    :return: lowest index of T

    """
    if not text or not subs:
        return -1

    n, m = len(text), len(subs)

    last = {}
    for k in range(m):
        last[subs[k]] = k

    # align end of pattern at index m-1 of text
    i = m-1  # index into 'text'
    k = m-1  # index into 'subs'
    while i < n:
        if text[i] == subs[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text
            else:
                i -= 1  # examine previous characters in both T & P
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j+1)
            k = m -1  # restart at end of pattern

    return -1