from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high + low)//2 

            # if exactly in the middle of the list
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1

        return -1
                





s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0


print(s.search(nums, target))