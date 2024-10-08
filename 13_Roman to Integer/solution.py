class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        num = 0
    
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                num -= dic[s[i]]
            else:
                num += dic[s[i]]

        return num
    
## Time Complexity:O(n)
## Space Complexity:O(1) -> 變數('s' and 'num')及字典都是固定的