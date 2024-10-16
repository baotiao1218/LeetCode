class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = nums[0]
        
        #Using Kadane's Algorithm
        for i in range(1,len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]

            if cursum > maxsum:
                maxsum = cursum
        
        return maxsum
    
## Time Complexity:O(n)
## Space Complexity:O(n)