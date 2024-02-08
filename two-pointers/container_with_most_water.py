from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0 # left pointer
        rp = len(height) - 1 # right pointer
        max_area = -9999999
        max_x_axis = 0
        max_y_axis = 0
        while lp < rp:
            x_axis =  (rp-lp)
            y_axis =  min(height[lp], height[rp])
            area = x_axis * y_axis
            if area > max_area:
                max_area = area
                max_x_axis = x_axis
                max_y_axis = y_axis
            else:
                # if the height is more taller then shift to the right, else shift left
                if height[lp] < height[rp]:
                    lp += 1
                else:
                    rp -= 1
        return max_x_axis * max_y_axis
    

# s = Solution()
# inputs = [1,8,100,2,100,4,8,3,7]
# print(s.maxArea(inputs))

