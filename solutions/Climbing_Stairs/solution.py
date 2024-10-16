class Solution:
    def climbStairs(self, n: int) -> int:
        d = defaultdict(int)
        d[0] = d[1] = 1
        
        def helper(n):
            if d[n]:
                return d[n]
            d[n] = helper(n-1) + helper(n-2)
            return d[n]
        return helper(n)
    
## Time Complexity:O(n)
## Space complexity:O(n)


#Optimized Answer 1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev = cur = temp = 1
        
        for i in range(2,n+1):
            temp = cur
            cur += prev
            prev = temp
        
        return cur

## Time Complexity:O(n)
## Space complexity:O(1)