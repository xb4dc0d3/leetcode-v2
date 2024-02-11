from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lp = 0 # left pointer
        rp = 1 # right pointer
        sum_of_num = 0

        while rp < len(nums):
            sum_of_num = nums[lp] + nums[rp]
            if sum_of_num == target:
                return [lp, rp]

            else:
                rp += 1
                if rp > len(nums) - 1:
                    lp += 1
                    rp = lp + 1
              





s = Solution()
nums = [1,2,11,7,12]
target = 9

print(s.twoSum(nums, target))
        