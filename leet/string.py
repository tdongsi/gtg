
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
        return 0