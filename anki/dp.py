
def longest_common_subsequence_length(str1:str, str2:str) -> int:
    return 0


def longest_common_subsequence(str1:str, str2:str) -> str:
    return ""


def subset_sum(values:list, total:int) -> bool:
    """ Given an array of non-negative numbers and a total, is there a way to add up those numbers to the total.

    :param values: array of non-negative numbers
    :param total: target total
    :return: True if possible
    """

    check = [False] * (total+1)
    check[0] = True

    for i in range(1, total+1):
        for val in values:
            if i - val >= 0 and check[i-val]:
                check[i] = True
                break

    return check[total]