class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = defaultdict(int)
        for num in nums:
            ht[num] += 1
            if ht[num] > 1:
                return True
        
        return False

## Time Complexity:O(n)
## Space Complexity:O(1) (英文字母最多26字) 


#Optimized Answer
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 直接先排序好
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
    
"""
注意:
range()不需要-1! (len(nums)-1)

range會自動幫你-1, 所以直接range(len(nums))就好
"""
## Time Complexity:O(n)
## Space Complexity:O(1)