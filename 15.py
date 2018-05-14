from collections import Counter

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # no solution
        if len(nums) < 3:
            return []
        
        # Any more than 3 occurrences of an int do not affect the solution
        counts = Counter(nums)
        nums = []
        for element in counts:
            nums += [element] * min(3, counts[element])
        
        nums.sort()
        neg_c = [-element for element in nums]
        solutions = set()
        
        # a + b = -c
        for i in range(len(neg_c)):
            target = neg_c[i]
            search = nums[:i] + nums[i+1:]
            left = 0
            right = len(search) - 1
            while left < right:
                current = search[left] + search[right]
                if current > target:
                    right -= 1
                elif current < target:
                    left += 1
                else:
                    solutions.add(frozenset([-target, search[left], search[right]]))
                    right -= 1
        
        # we now have the answer, just need to format
        solutions = list(solutions)
        solutions = [list(solution) if len(solution) == 3 
                     else list(solution) + [-sum(solution)] if len(solution) == 2 
                     else [0,0,0] for solution in solutions]
        
        return solutions
        
        
        
a = Solution()
print(a.threeSum([0, 0, 0, 1, 2, -1, -1]))