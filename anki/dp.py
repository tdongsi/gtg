"""Dynamic Programming."""

import chapter13.string


def longest_common_subsequence_length(str1:str, str2:str) -> int:
    if not str1 or not str2:
        return 0

    L = chapter13.string.longest_common_subsequence(str1, str2)

    return L[len(str1)][len(str2)]


def longest_common_subsequence_solution(str1:str, str2:str) -> str:
    if not str1 or not str2:
        return ""

    m = len(str1)
    n = len(str2)
    mtable = chapter13.string.longest_common_subsequence(str1, str2)

    subsequence = [""] * mtable[m][n]
    idx = mtable[m][n] - 1

    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            # if character matches, add to the array
            subsequence[idx] = str2[j - 1]
            i -= 1
            j -= 1
            idx -= 1
        else:
            # else, follow the larger number
            if mtable[i-1][j] > mtable[i][j-1]:
                i -= 1
            else:
                j -= 1

    return "".join(subsequence)


def subset_sum(values: list, total: int) -> bool:
    """ Given an array of non-negative numbers and a total, is there a way to add up those numbers to the total.

    :param values: array of non-negative numbers
    :param total: target total
    :return: True if possible
    """

    if not values:
        return False

    n = len(values)
    check = [[False] * (total+1) for _ in range(n+1)]

    # if sum == 0, it is True no matter how many in the set
    for i in range(n+1):
        check[i][0] = True

    for i in range(1, n+1):
        for j in range(1, total+1):
            if j < values[i-1]:
                check[i][j] = check[i-1][j]
            else:
                check[i][j] = check[i-1][j] or check[i-1][j - values[i-1]]

    return check[n][total]