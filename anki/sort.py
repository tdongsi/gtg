

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
        med = len(mlist) // 2
        left = merge_sort(mlist[:med])
        right = merge_sort(mlist[med:])
        return _merge(left, right)