from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        flagCounter = 0
        maxConsecutiveMap = {}
        maxConsecutiveMap[flagCounter] = 1

        if not nums:
            return 0

        for index in range(len(nums)-1):
            if nums[index+1] - nums[index] == 1:
                maxConsecutiveMap[flagCounter] += 1
            else:
                # If previous and next number difference is 0 then skip
                if nums[index+1] - nums[index] == 0:
                    continue
                flagCounter += 1
                maxConsecutiveMap[flagCounter] = 1
        return max(maxConsecutiveMap.values())



# s = Solution()
# nums = [0,1,1,2]
# print(s.longestConsecutive(nums))