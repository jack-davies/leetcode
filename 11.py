class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        best_area = (right - left) * min(height[left], height[right])
        
        for i in range(len(height) - 1):
            for j in range(len(height) - 1, i, -1):
                area = (j - i) * min(height[i], height[j])
                if area > best_area:
                    left = i
                    right = j
                    best_area = area
        return best_area
        

a = Solution()
print(a.maxArea([1,2,4,3]))