class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:  
        if amount == 0:
            return 0
        
        am_arr = [amount + 1] * (amount + 1)
        am_arr[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if i-c >= 0:
                    am_arr[i] = min(am_arr[i], am_arr[i-c] + 1)

        return am_arr[-1] if am_arr[-1] != amount + 1 else -1
    
## Time Complexity: O(amount * m) (amount: 目標金額, m = 硬幣數)
## Space complexity: O(amount) (因用amount + 1存各金額的硬幣數)