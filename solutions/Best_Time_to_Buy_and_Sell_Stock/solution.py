class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = sys.maxsize

        for i in prices:
            if(i < minPrice):
                minPrice = i
            if(i - minPrice > maxProfit):
                maxProfit = i - minPrice

        return maxProfit
    
## Time Complexity:O(n)
## Space complexity:O(1)


#Optimized Answer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        #minPrice第一個設為prices[0],然後迴圈再從[1]開始跑,可省一圈迴圈.
        for i in prices[1:]:
            if(i < minPrice):
                minPrice = i
            if(i - minPrice > maxProfit):
                maxProfit = i - minPrice

        return maxProfit
    
## Time Complexity:O(n)
## Space complexity:O(1)