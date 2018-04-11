"""
A group of problems related to histogram

* Largest Rectangle in Histogram
    * Largest Rectangle in Matrix
        * Largest Square in Matrix
"""

def largest_rect_histogram_DnC(heights: list) -> int:
    """ Find the largest rectangular area possible in a given histogram
    where the largest rectangle can be made of a number of contiguous bars.
    Divide and Conquer solution. O(n logn)
    https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

    :param mlist: list of bar heights, each bar width = 1.
    :return: area of the largest rectangle.
    """
    if len(heights) == 1:
        return heights[0]
    elif len(heights) == 0:
        return 0

    # This step takes O(N)
    minVal = min(heights)
    minIdx = heights.index(minVal)

    # Solve the smaller problem for sublist before smallest number
    # E.g. solve [4,6,5]
    front = largest_rect_histogram_DnC(heights[0:minIdx])
    # Solve the smaller problem for sublist after smallest number
    # E.g.: solve [3,2]
    back = largest_rect_histogram_DnC(heights[minIdx + 1:])
    # The area associated with minimum column is trivial to compute
    current = minVal * len(heights)

    # Find max of 3
    return max(front, current, back)


def largest_rect_histogram_stack(heights: list) -> int:
    """ Find the largest rectangular area possible in a given histogram
    where the largest rectangle can be made of a number of contiguous bars.

    O(n) solution with a stack. Intuition explained in https://www.youtube.com/watch?v=VNbkzsnllsU.

    Using a stack to store (left_idx, height).

    Going from left to right, if current height (2) is smaller than top of the stack (6).
    1) Pop stack: left_idx, height = s.pop()
    2) Calculate best rectangle: area = height * (cur_idx - left_idx). Update max.
    3) Prepare new item: (left_idx, cur_height). NOTE: left_idx, not cur_idx.
    4) If top of the stack > cur_height, continue.

    :param mlist: list of bar heights, each bar width = 1.
    :return: area of the largest rectangle.
    """

    stack = []
    max_area = 0
    peek_idx = -1  # idx of stack peek

    for idx, e in enumerate(heights):
        if not stack:
            stack.append((idx, e))
        else:
            save_idx = idx
            while stack:
                # peek top of the stack
                peek_idx, peek_height = stack[-1]
                if e < peek_height:
                    stack.pop()
                    save_idx = peek_idx

                    temp = peek_height * (idx - peek_idx)
                    if max_area < temp:
                        max_area = temp
                else:
                    break

            # push back the current bar
            stack.append((save_idx, e))

    # Handle the bars still in the stack
    idx = len(heights)
    while stack:
        peek_idx, peek_height = stack.pop()
        temp = peek_height * (idx - peek_idx)
        if max_area < temp:
            max_area = temp

    return max_area