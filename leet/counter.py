
def find_uniques(mlist: list):
    from collections import Counter
    counter = Counter(mlist)
    return [k for k, v in counter.items() if v == 1]


def intersection(nums1, nums2):
    from collections import Counter
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    counter12 = counter1 & counter2
    return list(counter12.keys())

