
class MedianSortedArrays:
    """https://leetcode.com/problems/median-of-two-sorted-arrays/description/"""

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        if (m + n) % 2 != 0:
            return self._find_k(nums1, nums2, mid)
        else:
            first = self._find_k(nums1, nums2, mid)
            second = self._find_k(nums1, nums2, mid - 1)
            # print("%f %f" % (first, second))
            return (first + second) / 2

    def _find_k(self, nums1, nums2, k):
        if k < 0 or (not nums1 and not nums2):
            raise ValueError()

        if len(nums1) == 0:
            return nums2[k]
        elif len(nums2) == 0:
            return nums1[k]
        elif k == 0:
            if nums1[0] < nums2[0]:
                return nums1[0]
            else:
                return nums2[0]
        else:
            mid = k // 2
            idx1 = min(mid, len(nums1) - 1)
            idx2 = min(mid, len(nums2) - 1)
            if nums1[idx1] < nums2[idx2]:
                return self._find_k(nums1[idx1 + 1:], nums2, k - idx1 - 1)
            elif nums1[idx2] > nums2[idx1]:
                return self._find_k(nums1, nums2[idx2 + 1:], k - idx2 - 1)
            else:  # nums1[idx2] == nums2[idx1]
                if idx1 == 0 and idx2 == 0:
                    return nums1[idx1]
                return self._find_k(nums1[idx1:], nums2[idx2:], k - idx1 - idx2)


class LongestConsecutive:
    """https://leetcode.com/problems/longest-consecutive-sequence/description/"""

    def longest_consecutive(self, nums):
        if not nums:
            return 0

        nums_set = set(nums)
        max_streak = 0

        for num in nums_set:

            if num-1 not in nums_set:
                cur = num
                cur_streak = 1

                while num+1 in nums_set:
                    cur += 1
                    cur_streak += 1

                max_streak = max(max_streak, cur_streak)

        return max_streak


    def longest_consecutive_old(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # NOTE: radix sort can be used instead.
        nums.sort()
        current_streak = 1
        last_e = nums[0]
        max_streak = 1

        for e in nums[1:]:
            if e == last_e + 1:
                last_e = e
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak

        return max_streak