class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        arr = []

        for c in s:
            if(c.isalnum()):
                arr.append(c.lower())

        i = 0
        j = len(arr) - 1
        
        while(i <= j):
            if(arr[i] != arr[j]):
                return False
            else:
                i += 1
                j -= 1

        return True
    
## Time Complexity:O(n)
## Space complexity:O(n) 因本題不分大小寫，先把所有字母都先小寫化一次


#Optimized Answer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        # 直接開始跑2 pointers,並在跑pointers同時"小寫化"
        while(i < j):
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
                
            elif(s[i].lower() == s[j].lower()):
                i += 1
                j -= 1
            else:
                return False

        return True
    
## Time Complexity:O(n)
## Space complexity:O(1)
