
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