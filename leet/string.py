
class Box():

    @staticmethod
    def simple_string(mystring):
        """Evaluate simple expression string such as "5+6-11". Expected 11."""
        import re
        sum = 0

        if mystring and mystring[0] not in "+-":
            mystring = "+" + mystring

        operands = re.split("[+-]", mystring)
        # print(operands)
        operators = re.findall("[+-]", mystring)
        # print(operators)

        for o, num in zip(operators, operands[1:]):
            # There is always an empty string in operands
            print("%s %s" %(o, num))
            if o == "+":
                sum += int(num)
            elif o == "-":
                sum -= int(num)
            else:
                raise ValueError("Unexpected operator")

        return sum

    @staticmethod
    def simple_string_serious(mystring):
        """Evaluate simple expression string such as "5+6-11". Expected 11."""
        def op(a, b, plus:bool)->int:
            if plus:
                return a + b
            else:
                return a - b

        start = 0
        end = -1
        plus = True
        sum = 0

        for idx, char in enumerate(mystring):
            if char == "+":
                end = idx
                if start < end:
                    sum = op(sum, int(mystring[start:end]), plus)
                start = idx + 1
                plus = True
            elif char == "-":
                end = idx
                if start < end:
                    sum = op(sum, int(mystring[start:end]), plus)
                start = idx+1
                plus = False
            else:
                pass

        # Handle the rest
        if start < len(mystring):
            sum = op(sum, int(mystring[start:]), plus)

        return sum

    @staticmethod
    def complex_string(mstr):
        """Evaluate complex expression. Example: "5+16-((9-6)-(4-2))"""
        stack = []
        try:
            start = mstr.index("(")
        except ValueError:
            return Box.simple_string_serious(mstr)

        for char in mstr[start:]:
            # print(stack)
            if char == ")":
                exp = []
                a = stack.pop()
                while a != "(":
                    exp.append(a)
                    a = stack.pop()

                # evaluate exp and push back
                exp_str = ''.join(reversed(exp))
                # print(exp_str)
                stack.append(str(Box.simple_string_serious(exp_str)))
            else:
                stack.append(char)

        return Box.simple_string_serious(mstr[0:start] + ''.join(stack))


class GoogleWordPuzzle():

    RESOURCE_FOLDER = "leet/resources"

    @staticmethod
    def is_adjacent(word1, word2):
        count = 0
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
            if count > 1:
                return False

        if count == 1:
            return True

    @staticmethod
    def adjacent_words(dict, word):
        adj = []

        for w in dict:
            if GoogleWordPuzzle.is_adjacent(w, word):
                adj.append(w)

        return adj

    @staticmethod
    def word_puzzle(start: str, end: str):
        """Solve puzzle: from a source word, modify one character in each step such that
        the new word is valid in order to get to destination word.
        """

        from collections import deque

        if len(start) != len(end):
            return None

        # Dictionary of same length words
        mydict = GoogleWordPuzzle.filter_dict(len(start))

        # This is basically a BFS traversal
        to_visit = deque([start])
        discovered = {start: None}

        while to_visit:
            v = to_visit.popleft()
            breakFlag = False

            for w in GoogleWordPuzzle.adjacent_words(mydict, v):
                if w not in discovered:
                    discovered[w] = (v, w)
                    to_visit.append(w)

                if w == end:
                    breakFlag = True
                    break

            if breakFlag:
                break

        if end not in discovered:
            return None
        else:
            path = [end]
            walk = end
            while walk != start:
                parent = discovered[walk][0]
                path.append(parent)
                walk = parent

            path.reverse()
            return path

    @staticmethod
    def filter_dict(length):
        mydict = []
        try:
            with open(GoogleWordPuzzle.RESOURCE_FOLDER + "/words.txt") as words:
                count = 0
                for word in words:
                    if len(word.strip()) == length:
                        mydict.append(word.strip())
        except IOError:
            print("Error opening dictionary")

        return mydict


class FacebookPerms():

    @staticmethod
    def generate_perms(mlist):
        """Generate permutations of a list"""
        if not mlist or len(mlist) == 1:
            yield mlist
        else:
            for perm in FacebookPerms.generate_perms(mlist[1:]):
                # NOTE: len(mlist) NOT len(perm)
                for i in range(len(mlist)):
                    yield perm[:i] + mlist[0:1] + perm[i:]

    @staticmethod
    def merge_intervals(mlol):
        """ Given a collection of intervals, merge all overlapping intervals.

        :param mlol: List of lists
        :return: overlapping intervals.
        """
        return None


class LinkedIn():

    @staticmethod
    def min_word_dist(words, word1, word2):
        """Calculate the shortest distance between 2 words in a word list.
        The word list is given to the constructor, and may contain more than 1 instance of each word.
        Example: "the quick brown fox quick jumps", distance(fox, quick) should return 1
        (indices for fox = (3), quick = (1, 4), smallest distance is between 3 & 4).
        """

        occ_1 = [idx for idx, word in enumerate(words) if word == word1]
        occ_2 = [idx for idx, word in enumerate(words) if word == word2]

        min_dist = len(words)
        for num1 in occ_1:
            for num2 in occ_2:
                if abs(num1-num2) < min_dist:
                    min_dist = abs(num1-num2)

        return min_dist

    @staticmethod
    def union(a: list, b: list):

        if a is None and b is None:
            return None
        elif a is None:
            return set(b)
        elif b is None:
            return set(a)

        idx1, idx2 = 0, 0
        m, n = len(a), len(b)
        output = []

        while idx1 < m and idx2 < n:
            if a[idx1] < b[idx2]:
                output.append(a[idx1])
                idx1 += 1
            else:
                output.append(b[idx2])
                idx2 += 1

        # Either idx1 == len(a) or idx2 == len(b)
        output.extend(a[idx1:])
        output.extend(b[idx2:])

        return set(output)

    @staticmethod
    def intersect(a: list, b: list):

        idx1, idx2 = 0, 0
        m, n = len(a), len(b)
        output = []

        while idx1 < m and idx2 < n:
            if a[idx1] == b[idx2]:
                if not output or (output and output[-1] != a[idx1]):
                    output.append(a[idx1])
                idx1 += 1
                idx2 += 1
            elif a[idx1] < b[idx2]:
                idx1 += 1
            else:  # a[idx1] > b[idx2]
                idx2 += 1

        return output


def triangleOrNot(a, b, c):

    def _triangle_check(x, y, z):
        check = abs(y-z) < x < y + z
        return "Yes" if check else "No"

    res = []
    for e in zip(a, b, c):
        res.append(_triangle_check(*e))

    return res


def consecutive(num):
    """Idea: a + (a+1) + ... + (a+L) == a*(L+1) + L*(L+1)/2 = num
    The requirement translates to a >= 1 and L >= 1.
    """
    def _cum_sum(n):
        """Cumulative sum 1 + ... + n"""
        return n*(n+1) // 2

    count = 0
    L = 1
    while _cum_sum(L) < num:
        a, r = divmod(num - _cum_sum(L), (L+1))
        if r == 0 and a >= 1:
            count += 1

        L += 1

    return count


def create_text_from_magazine(text, magazine):
    """
    You are given a search string and a magazine.
    You seek to generate all the characters in search string by cutting them out from the magazine.
    Give an algorithm to efficiently determine whether the magazine contains all the letters in the search string.

    :param text: Text you want to generate.
    :param magazine: Where you get characters from.
    :return: True or False
    """
    from collections import Counter

    text_count = Counter(text.strip().lower())
    del text_count[' ']

    lines = magazine.split("\n")
    for line in lines:
        mag_count = Counter(line.strip().lower())
        text_count -= mag_count
        # print(text_count)
        if not text_count:
            return True

    return False
