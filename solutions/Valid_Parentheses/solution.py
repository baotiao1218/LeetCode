class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ('(','[','{'):
                stack.append(s[i])
            else:
                try:
                    popdata = stack.pop()
                    if(ord(s[i]) - ord(popdata) == 1 or ord(s[i]) - ord(popdata) == 2):
                        continue
                    else:
                        return False
                except IndexError:
                    return False
    
        if not stack:
            return True

        return False
    
## Time Complexity:O(n)
## Space complexity:O(n)

#Optimized Answer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if not stack:
                    return False

                popdata = stack.pop()

                if(ord(c) - ord(popdata) == 1 or ord(c) - ord(popdata) == 2):
                    continue
                else:
                    return False

        return not stack
    
## Time Complexity:O(n)
## Space complexity:O(n)
