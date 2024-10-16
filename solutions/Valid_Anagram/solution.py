class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = []
        arr2 = []

        for c in s:
            arr1.append(c)
        for c in t:
            arr2.append(c)

        arr1.sort()
        arr2.sort()

        if(len(arr1) != len(arr2)):
            return False
            
        for i in range(len(s)):
            if(arr1[i] != arr2[i]):
                return False
        
        return True

## Time Complexity:O(n)
## Space complexity:O(n)


#Optimized Answer 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        return sorted_s == sorted_t

## Time Complexity:O(n log n) (跑兩次sort)
## Space complexity:O(n) (用另外兩個新的list存sorted的值)


#Optimized Answer 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = defaultdict(int)

        for x in s:
            count[x] += 1

        for x in t:
            count[x] -= 1

        for val in count.values():
            if val != 0:
                return False
        
        return True

## Time Complexity:O(n)
## Space complexity:O(1) (dict最大26個值而已)