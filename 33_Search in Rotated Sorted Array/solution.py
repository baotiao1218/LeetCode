class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        while left < right:
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
        return -1
    
## Time Complexity:O(log n)
## Space Complexity:O(1) -> 只有搜尋，沒存東西


#Optimized Answer
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
## Time Complexity:O(log n)
## Space Complexity:O(1) -> 只有搜尋，沒存東西