from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        three_sum = 0
        lp = 0 # left pointer
        rp = 0 # right pointer
        nums.sort()

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                # Check if the a from (a + b + c) is already in the previous pointer then proceed to next index to
                # to prevent duplicate
                # Example:
                # [-1a, -1b, -2, 2]
                # [-1a, -2, 2]
                # [-1b] <-- skipped
                continue
            
            lp = index + 1
            rp = len(nums) - 1
            while lp < rp:
                three_sum = nums[index] + nums[lp] + nums[rp]
                if  three_sum < 0:
                    lp += 1
                elif three_sum > 0:
                    rp -= 1
                else:
                    result.append([nums[index], nums[lp], nums[rp]])
                    lp += 1
                    # if the previous number is same then proceed to the next number
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1

        return result
        



# [-4, -1, -1, 0, 1, 2]
inputs = [-4, -1, -1, 0, 1, 2]
s = Solution()
print(s.threeSum(inputs))