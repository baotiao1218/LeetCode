class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 可直接用len(nums)//2
        mid = int(len(nums)/2)
        l = 0
        h = len(nums) - 1
        
        while(l <= h):
            if(nums[mid] == target):
                return mid
            
            if(target > nums[mid]):
                l = mid + 1
            else:
                h = mid - 1
            # 可直接用//2
            mid = int((l+h)/2)
        
        if(l == h and nums[l] == target):
            return mid

        return -1 
             

## Time Complexity:O(log n)
## Space complexity:O(1) 


#Optimized Answer 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        
        while(l <= h):
            mid = (l+h)//2
            if(nums[mid] == target):
                return mid
            
            if(target > nums[mid]):
                l = mid + 1
            else:
                h = mid - 1

        return -1 