"""
A group of problems related to finding "buy low, sell high" from a list of numbers

* Find when to buy and sell to maximize profit from list of stock prices
    * Largest Sum Contiguous Subarray/ Maximal Subarray
"""

from typing import Tuple


def buy_stock(prices:list) -> Tuple[int, int, int]:
    """Find when to buy and sell to maximize profit from list of stock prices"""
    profit, buy, sell = 0, 0, 0
    min_price, min_idx = prices[0], 0

    for i in range(1, len(prices)):
        if prices[i] - min_price > profit:
            profit = prices[i] - min_price
            buy, sell = min_idx, i

        if prices[i] < min_price:
            min_price, min_idx = prices[i], i

    return profit, buy, sell


def maximum_subarray_alt(numbers:list) -> list:
    """ Largest Sum Contiguous Subarray.
    NOTE: This is a WRONG solution, based on the unit tests.
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    total = 0
    accu = []  # accumulated sum of "numbers"

    for num in numbers:
        total += num
        accu.append(total)

    max_val, start, end = buy_stock(accu)

    print(max_val)

    return numbers[(start+1):(end+1)]


def maximum_subarray(nums: list) -> list:
    """Maximum subarray without using helper function buy_stock."""
    best_sum = 0  # NOTE: not infinity since you have a choice of empty sub-array.
    best_start = best_end = 0
    cur_sum, cur_start = 0, 0

    for cur_end, e in enumerate(nums):
        if cur_sum <= 0:
            # Start a new sequence
            cur_start = cur_end
            cur_sum = e
        else:
            # Extend the current sequence
            cur_sum += e

        if cur_sum > best_sum:
            best_sum = cur_sum
            best_start = cur_start
            best_end = cur_end + 1

    return nums[best_start:best_end]
