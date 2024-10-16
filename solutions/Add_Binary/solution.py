#My Original Answer
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            ans += str(carry%2)
            carry = carry // 2
        
        return ''.join(reversed(ans))
    
## Time Complexity:O(m*n)
## Space Complexity:O(m*n)

