#(Recursive)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        t = root.left
        root.left = root.right
        root.right = t
        
        return root

## Time Complexity:O(n)
## Space complexity:O(n) (最差) / O(h) (樹高)


#Optimized Answer

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        
        return root

## Time Complexity:O(n)
## Space complexity:O(n) (最差) / O(h) (樹高)