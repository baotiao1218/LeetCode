class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = defaultdict(int)

        for c in magazine:
            hashTable[c] += 1
        
        for c in ransomNote:
            if hashTable[c] == 0:
                return False
            else:
                hashTable[c] -= 1
        
        return True


## Time Complexity:O(n+m) (n = len(st1), m = len(st2)) 
## Space complexity:O(1) 字母只有26位


#Optimized Answer 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #
        st1,st2 = Counter(ransomNote), Counter(magazine)

        if st1 & st2 == st1:
            return True
        
        return False

## Time Complexity:O(n+m) (n = len(st1), m = len(st2)) 
## Space complexity:O(1) 字母只有26位