from collections import Counter

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        # Any more than 3 occurrences of an int do not affect the solution
        counts = Counter(nums)
        nums = []
        for element in counts:
            nums += [element] * min(3, counts[element])
            
        nums.sort()
        t_neg_c = [target-element for element in nums]
        
        # a + b + c = target
        # a + b = target - c
        dist = float('inf')
        best = None
        print(nums)
        print(t_neg_c)
        for i in range(len(t_neg_c)):
            tc = t_neg_c[i]
            search = nums[:i] + nums[i+1:]
            left = 0
            right = len(search) - 1
            while left < right:
                ab = search[left] + search[right]
                current_dist = ab - tc
                if abs(current_dist) < dist:
                    dist = abs(current_dist)
                    best = ab + nums[i]
                if current_dist > 0:
                    right -= 1
                elif current_dist < 0:
                    left += 1
                else:
                    break
        return best
                    
a = Solution()
print(a.threeSumClosest([-1, 2, 1, -4], 1))