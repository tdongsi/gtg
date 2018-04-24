
def find_uniques(mlist: list):
    from collections import Counter
    counter = Counter(mlist)
    out = []
    for k, v in counter.items():
        if v == 1:
            out.append(k)
    return out


