
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


class Google():

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
            if Google.is_adjacent(w, word):
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
        mydict = Google.filter_dict(len(start))

        # This is basically a BFS traversal
        to_visit = deque([start])
        discovered = {start: None}

        while to_visit:
            v = to_visit.popleft()
            breakFlag = False

            for w in Google.adjacent_words(mydict, v):
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
            with open(Google.RESOURCE_FOLDER + "/words.txt") as words:
                count = 0
                for word in words:
                    if len(word.strip()) == length:
                        mydict.append(word.strip())
        except IOError:
            print("Error opening dictionary")

        return mydict