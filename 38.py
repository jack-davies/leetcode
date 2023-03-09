class Solution:
    def countAndSay(self, n: int) -> str:
        """
        1 -> 1
        2 -> 11
        3 -> 21
        4 -> 1211
        5 -> 111221
        6 -> 312211
        ...
        """
        def render(value: str):
            output = []
            previous = None
            for digit in value:
                if digit == previous:
                    output[-1][-1] += 1
                else:
                    previous = digit
                    output += [[digit, 1]]
            return "".join([(str(d[1]) + d[0]) for d in output])

        output = "1"
        for i in range(2, n+1):
            output = render(output)

        return output
