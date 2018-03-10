
def longest_common_subsequence_length(str1:str, str2:str) -> int:
    return 0


def longest_common_subsequence(str1:str, str2:str) -> str:
    return ""


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