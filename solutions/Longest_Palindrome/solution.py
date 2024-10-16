class Solution:
    def longestPalindrome(self, s: str) -> int:
        numset = set()
        longest = 0
        for c in s:
            if c in numset:
                numset.remove(c)
                longest += 2
            else:
                numset.add(c)
        # +1是因為中間會有一個字當"軸心" , eg: dccaccd
        return longest + 1 if numset else longest
        
## Time Complexity: O(n)
## Space complexity: O(1) (因為Max為O(52))