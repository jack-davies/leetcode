class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        best_area = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            best_area = max(best_area, (right - left) * min(height[left], height[right]))
        return best_area
