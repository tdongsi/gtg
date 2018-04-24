
def find_brute(text:str, subs: str):
    """ Pattern matching with brute force.
    Return the lowest index of text T at which substring P begins (or else -1).

    :param text: text T
    :param subs: substring P
    :return: lowest index of T
    """
    if not text or not subs:
        return -1

    n, m = len(text), len(subs)

    for i in range(n - m + 1):
        k = 0
        while k < m and text[i+k] == subs[k]:
            k += 1
        if k == m:
            return i

    return -1


def find_boyer_moore(text:str, subs:str):
    """ Pattern matching with Boyer-Moore algorithm.
    Return the lowest index of text T at which substring P begins (or else -1).

    :param text: text T
    :param subs: substring P
    :return: lowest index of T
    """
    if not text or not subs:
        return -1

    n, m = len(text), len(subs)

    last = {}
    for k in range(m):
        last[subs[k]] = k

    # align end of pattern at index m-1 of text
    i = m-1  # index into 'text'
    k = m-1  # index into 'subs'
    while i < n:
        if text[i] == subs[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text
            else:
                i -= 1  # examine previous characters in both T & P
                k -= 1
        else:
            j = last.get(text[i], -1)
            # Sanity check:
            # 1) text[i] not in last -> i += m
            # 2) text[i] in last -> i += m - (j+1)
            i += m - min(k, j+1)
            k = m -1  # restart at end of pattern

    return -1


def compute_kmp_fail(pattern: str):
    """ Utility function that computes and returns KMP failure function.

    :param pattern: the pattern
    :return: list as lookup table
    """
    m = len(pattern)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if pattern[j] == pattern[k]:  # k+1 characters match thus far
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:  # no match found starting a j
            j += 1
    return fail


def find_kmp(text: str, subs: str):
    """ Pattern matching with Knuth-Morris-Pratt algorithm.
    Return the lowest index of text T at which substring P begins (or else -1).

    :param text: text T
    :param subs: substring P
    :return: lowest index of T
    """
    if not text or not subs:
        return -1

    n, m = len(text), len(subs)

    fail = compute_kmp_fail(subs)

    j = 0
    k = 0
    while j < n:
        if text[j] == subs[k]:
            if k == m-1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1

    return -1


def longest_common_subsequence(str1:str, str2:str) -> int:
    if not str1 or not str2:
        return 0

    m = len(str1)
    n = len(str2)
    mtable = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                mtable[i][j] = 1 + mtable[i-1][j-1]
            else:
                mtable[i][j] = max(mtable[i-1][j], mtable[i][j-1])

    return mtable


class TrieNode():
    __slots__ = 'children', 'word_end'

    def __init__(self):
        self.children = {}
        self.word_end = False


class Trie():

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        current = self._root

        for c in word:
            node = current.children.get(c)
            if node is None:
                node = TrieNode()
                current.children[c] = node

            current = node

        # Mark the last one as end of word
        current.word_end = True

    def search(self, word):
        current = self._root

        for c in word:
            node = current.children.get(c)
            if node is None:
                return False
            current = node

        return current.word_end

    def delete(self, word):
        self._delete(self._root, word, 0)

    def _delete(self, current: TrieNode, word: str, idx: int):
        """Return True if parent node should delete the mapping."""
        if idx == len(word):
            if not current.word_end:
                return False

            current.word_end = False
            return len(current.children) == 0

        c = word[idx]
        node = current.children.get(c)
        if node is None:
            return False

        shouldDelete = self._delete(node, word, idx+1)

        if shouldDelete:
            del current.children[c]
            return len(current.children) == 0

        return False

    def list(self):
        self._list(self._root, "")

    def _list(self, current: TrieNode, prefix: str):
        if current.word_end:
            print(prefix)
            # yield prefix
        else:
            for k in current.children:
                self._list(current.children[k], prefix + k)