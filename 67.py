class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = False
        for i in range(max(len(a), len(b))):
            a_digit = 0 if len(a)-i-1 < 0 else int(a[len(a)-i-1])
            b_digit = 0 if len(b)-i-1 < 0 else int(b[len(b)-i-1])

            sum_digit = int(a_digit) + int(b_digit) + (1 if carry else 0)
            carry = False
            if sum_digit > 1:
                carry = True
                sum_digit -= 2

            result += [str(sum_digit)]

        if carry:
            result += ["1"]

        return "".join(reversed(result))
