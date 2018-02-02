

def merge_sort(mlist):
    def _merge(left, right):
        alist = []
        l_idx = 0
        r_idx = 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                alist.append(left[l_idx])
                l_idx += 1
            else:
                alist.append(right[r_idx])
                r_idx += 1

        # append the rest
        alist.extend(left[l_idx:])
        alist.extend(right[r_idx:])

        return alist

    if len(mlist) <= 1:
        return mlist
    else:
        med = len(mlist)//2
        left = merge_sort(mlist[:med])
        right = merge_sort(mlist[med:])
        return _merge(left, right)


def quicksort(mlist, lo=0, hi=None):

    def partition(alist, lo, hi):
        pivot = alist[hi - 1]
        idx = lo

        for i in range(lo, hi-1):
            if alist[i] < pivot:
                alist[i], alist[idx] = alist[idx], alist[i]
                idx += 1
        # move the pivot
        alist[idx], alist[hi - 1] = alist[hi - 1], alist[idx]
        return idx

    if hi is None:
        hi = len(mlist)

    if lo == hi:
        # empty list
        return mlist
    elif lo == hi-1:
        # singleton list
        return mlist
    else:
        p = partition(mlist, lo, hi)
        quicksort(mlist, lo, p)
        quicksort(mlist, p+1, hi)
        return mlist


def heap_sort(mlist):
    import heapq
    heapq.heapify(mlist)
    return [heapq.heappop(mlist) for i in range(len(mlist))]


def binary_search(mlist, target):
    def _bs(lo, hi):
        if lo == hi:
            return -1
        if lo == hi-1:
            if mlist[lo] == target:
                return lo
            else:
                return -1

        med = (lo+hi)//2
        if mlist[med] == target:
            return med
        elif mlist[med] < target:
            return _bs(med+1, hi)
        else:
            return _bs(lo, med)

    if mlist is None:
        return -1
    else:
        return _bs(0, len(mlist))
