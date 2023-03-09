class Solution:
    def isValid(self, s: str) -> bool:
        expected = ""
        for char in s:
            if char in set(["(", "[", "{"]):
                expected += {"(": ")", "[": "]", "{": "}"}[char]
            elif len(expected) > 0 and char == expected[-1]:
                expected = expected[:-1]
            else:
                return False
        return expected == ""
