# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return left + 1 if left > right else right + 1

## Time Complexity:O(n)
## Space complexity:O(n) / O(log n)


#Optimized Answer
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 直接用max函數取大值並+1即可
        return max(left,right) + 1
    
## Time Complexity: O(n)
## Space complexity: O(n) / O(log n)