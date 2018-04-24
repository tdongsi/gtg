
def find_uniques(mlist: list):
    from collections import Counter
    counter = Counter(mlist)
    out = []
    for k, v in counter.items():
        if v == 1:
            out.append(k)
    return out


def permutations(mlist: list):
    if not mlist:
        return

    if len(mlist) == 1:
        yield mlist
    else:
        for perm in permutations(mlist[1:]):
            for i in range(len(mlist)):
                yield perm[:i] + mlist[0:1] + perm[i:]
