
import random

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

    if not mlist or len(mlist) <= 1:
        return mlist
    else:
        med = len(mlist)//2
        left = merge_sort(mlist[:med])
        right = merge_sort(mlist[med:])
        return _merge(left, right)


def quick_sort(mlist, lo=0, hi=None):

    def partition(alist, lo, hi):
        pidx = random.randint(lo, hi-1)
        mlist[pidx], mlist[hi - 1] = mlist[hi - 1], mlist[pidx]
        pivot = alist[hi - 1]
        idx = lo

        for i in range(lo, hi-1):
            if alist[i] < pivot:
                alist[i], alist[idx] = alist[idx], alist[i]
                idx += 1
        # move the pivot
        alist[idx], alist[hi - 1] = alist[hi - 1], alist[idx]
        return idx

    if not mlist:
        return mlist

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
        quick_sort(mlist, lo, p)
        quick_sort(mlist, p + 1, hi)
        return mlist


def heap_sort(mlist):
    if mlist is None:
        return None

    import heapq
    heapq.heapify(mlist)
    return [heapq.heappop(mlist) for i in range(len(mlist))]


def counting_sort(mlist, k=None, key=None):
    """Counting sort

    :param mlist: List of items.
    :param k: Maximum range of key [0,k)
    :param key: function to get key of item. (for radix sort)
    :return:
    """
    if not mlist:
        return mlist

    if k is None:
        k = max(mlist) + 1

    if key is None:
        key = lambda x: x

    counter = [[] for i in range(k)]
    for e in mlist:
        counter[key(e)].append(e)

    output = []
    for section in counter:
        output.extend(section)
    return output


def radix_sort(mlist, w=None):
    RADIX = 10

    if not mlist:
        return mlist

    if w is None:
        temp = max(mlist)
        w = 0
        while temp > 0:
            w += 1
            temp //= RADIX

    output = mlist
    for digit in range(w):
        def my_key(num):
            for _ in range(digit):
                num //= RADIX
            return num % RADIX

        output = counting_sort(output, RADIX, my_key)
        # print(output)

    return output


def selection_sort(mlist):

    if not mlist:
        return mlist

    for i in range(0, len(mlist)-1):
        iMin = i
        for j in range(i+1, len(mlist)):
            if mlist[j] < mlist[iMin]:
                iMin = j

        if iMin != i:
            mlist[iMin], mlist[i] = mlist[i], mlist[iMin]

    return mlist


def binary_search(mlist, target):
    def _bs(lo, hi):
        if lo == hi:
            return -1
        if lo == hi-1:
            if mlist[lo] == target:
                return lo
            else:
                return -1

        mid = (lo+hi)//2
        if mlist[mid] == target:
            return mid
        elif mlist[mid] < target:
            return _bs(mid+1, hi)
        else:
            return _bs(lo, mid)

    if mlist:
        return _bs(0, len(mlist))
    else:
        return -1


def binary_search_iterative(mlist, target):
    if mlist is None:
        return -1
    else:
        lo = 0
        hi = len(mlist)
        while lo < hi:
            mid = (lo+hi) // 2
            if mlist[mid] == target:
                return mid
            elif mlist[mid] < target:
                lo = mid+1
            else:
                hi = mid

        return -1


def search_end(mlist, target):
    if mlist is None:
        return -1
    else:
        lo = 0
        hi = len(mlist)

        while lo < hi:
            mid = (lo + hi) // 2
            if mlist[mid] == target:
                if mid+1 < len(mlist) and mlist[mid+1] == target:
                    lo = mid+1
                else:
                    return mid
            elif mlist[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return -1


def search_start(mlist, target):
    if mlist is None:
        return -1
    else:
        lo = 0
        hi = len(mlist)

        while lo < hi:
            mid = (lo + hi) // 2
            if mlist[mid] == target:
                if mid >= 1 and mlist[mid-1] == target:
                    hi = mid
                else:
                    return mid
            elif mlist[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return -1


def quicksort3(mlist, lo=0, hi=None):
    """ Quick-sort using three-way partition strategy.
    """

    def partition3(mlist, lo, hi):
        """ In-place three-way partition of the list will return [< pivot] [== pivot] [> pivot]

        The two-way partition ([< pivot] [>= pivot]) seen in previous quicksort has the following degenerate cases:
         1. Almost sorted lists. -> Defense: Use random swaps to scramble the lists before sorting.
         2. Almost equal items. -> Defense: Use this three-way partition strategy.
        """
        pidx = random.randint(lo, hi-1)
        mlist[pidx], mlist[hi-1] = mlist[hi-1], mlist[pidx]
        pivot = mlist[hi-1]

        idx1 = lo
        for i in range(lo, hi-1):
            if mlist[i] < pivot:
                mlist[i], mlist[idx1] = mlist[idx1], mlist[i]
                idx1 += 1

        idx2 = idx1
        for i in range(idx1, hi-1):
            if mlist[i] == pivot:
                mlist[i], mlist[idx2] = mlist[idx2], mlist[i]
                idx2 += 1

        # move the pivot to the right partition
        mlist[idx2], mlist[hi - 1] = mlist[hi - 1], mlist[idx2]

        return idx1, idx2

    if not mlist:
        return mlist

    if hi is None:
        hi = len(mlist)

    if lo == hi:
        # empty list
        return mlist
    elif lo == hi - 1:
        # singleton list
        return mlist
    else:
        p, q = partition3(mlist, lo, hi)
        quicksort3(mlist, lo, p)
        quicksort3(mlist, q + 1, hi)
        return mlist
