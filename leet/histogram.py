"""
A group of problems related to histogram

* Largest Rectangle in Histogram
    * Largest Rectangle in Matrix
        * Largest Square in Matrix
"""

def largest_rect_histogram(mlist: list) -> int:
    """ Find the largest rectangular area possible in a given histogram
    where the largest rectangle can be made of a number of contiguous bars.
    https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

    :param mlist: list of bar heights, each bar width = 1.
    :return: area of the largest rectangle.
    """
    return 0