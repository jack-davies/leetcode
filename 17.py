class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        prev = [""]
        current = []
        
        for digit in digits:
            current = []
            for element in prev:
                key = int(digit) - 2
                for i in range(len(keys[key])):
                    current.append(element + keys[key][i])
                prev = current
        
        return current
            
a = Solution()
print(a.letterCombinations("23"))