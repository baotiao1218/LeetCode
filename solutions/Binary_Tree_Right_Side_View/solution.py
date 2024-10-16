# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, depth):
            if not root:
                return
            if len(ans) == depth :
                ans.append(root.val)
            if root.right:
                helper(root.right, depth + 1)
            if root.left:
                helper(root.left, depth + 1)

        helper(root, 0)

        return ans

## Time Complexity: O(n) (最壞) / O(log n)(complete binary tree) 
## Space Complexity: O(n) (最壞)