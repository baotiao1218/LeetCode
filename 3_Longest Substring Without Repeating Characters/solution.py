class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlist = []
        maxlength = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in strlist:
                strlist.append(s[right])   
            else:
                while s[right] in strlist:
                    strlist.pop(0)
                    left += 1
                strlist.append(s[right])

            maxlength = max(maxlength, right - left + 1)

        return maxlength

## Time Complexity:O(n^2) (list要遍歷)
## Space complexity:O(n)

# Optimized solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strset = set()
        maxlength = 0
        left = 0

        for right in range(len(s)):
            while s[right] in strset:
                strset.remove(s[left])
                left += 1
            strset.add(s[right])
            
            maxlength = max(maxlength, right - left + 1)

        return maxlength
## Time Complexity:O(n) (set用hashtable,所以其add,del,find...皆為O(1), 效率較佳)
## Space complexity:O(n)
