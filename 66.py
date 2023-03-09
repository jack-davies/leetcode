class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        carry = True
        while carry and i >= 0:
            carry = digits[i] == 9
            digits[i] = 0 if carry else digits[i] + 1
            i -= 1

        if carry:
            return [1] + digits
        else:
            return digits
