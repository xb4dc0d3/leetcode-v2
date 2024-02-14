class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEnding = 0
        maxSoFar = -99999999

        for idx in range(len(nums)):
            maxEnding = maxEnding + nums[idx]
            if (maxSoFar < maxEnding):
                maxSoFar = maxEnding
            if (maxEnding < 0):
                maxEnding = 0
        return maxSoFar
