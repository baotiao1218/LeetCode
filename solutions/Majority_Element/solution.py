class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)

        for num in nums:
            hashtable[num] += 1
        
        # 題目定義的Majority Element = 該數字出現次數大於數列長的一半以上
        for key in hashtable:
            if hashtable[key] > (len(nums)/2):
                return key
        
        return 0

## Time Complexity:O(n)
## Space complexity:O(n)


#Optimized Answer 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = sys.maxsize
        count = 0
        # 只需遍歷一次: Boyer-Moore Majority Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            elif num != candidate:
                count -= 1

        return candidate
    
## Time Complexity:O(n)
## Space Complexity:O(1)