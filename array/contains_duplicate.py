from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                return True
        return False
    


# s = Solution()
# print(s.containsDuplicate([1,2,3,1]))