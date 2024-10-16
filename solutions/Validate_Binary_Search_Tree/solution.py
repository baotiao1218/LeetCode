# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(rt,min,max):
            if rt == None:
                return True

            if not(max > rt.val and min < rt.val):
                return False

            return check(rt.left, min, rt.val) and check(rt.right, rt.val, max)

        return check(root, -sys.maxsize, sys.maxsize)
    
## Time Complexity:O(n) -> 用遞歸遍歷每個Node
## Space Complexity: worse: O(n), best: O(log n)  -> 最差是節點都在同一邊， 最佳則視樹的高度。