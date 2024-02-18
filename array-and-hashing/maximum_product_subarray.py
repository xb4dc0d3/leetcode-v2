from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxLocalProduct = nums[0]
        minLocalProduct = nums[0]
        maxGlobalProduct = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], max(maxLocalProduct * nums[i], minLocalProduct * nums[i]))
            minLocalProduct = min(nums[i], min(minLocalProduct * nums[i], maxLocalProduct * nums[i]))
            maxLocalProduct = temp
            maxGlobalProduct = max(maxGlobalProduct, maxLocalProduct)
        return maxGlobalProduct
    

s = Solution()
print(s.maxProduct([-4,-3]))