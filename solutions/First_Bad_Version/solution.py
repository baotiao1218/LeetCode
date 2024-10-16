# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        
        while(low < high):
            mid = int((low+high)//2)
            if(isBadVersion(mid)):
                high = mid
            else:
                low = mid + 1
        
        # 沒必要再比對low == high了
        if(low == high):
            return low

## Time Complexity:O(log n)
## Space complexity:O(1)

#Optimized Answer 1
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        
        while(low < high):
            mid = int((low+high)//2)
            if(isBadVersion(mid)):
                high = mid
            else:
                low = mid + 1

        return low
             
## Time Complexity:O(log n)
## Space complexity:O(1)