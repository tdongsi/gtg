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
    Divide and Conquer solution. O(n logn)
    https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

    :param mlist: list of bar heights, each bar width = 1.
    :return: area of the largest rectangle.
    """
    if len(heights) == 1:
        return heights[0]
    elif len(heights) == 0:
        return 0



    return 0