class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
            
        left = self.height(root.left)
        right = self.height(root.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return left + 1 if left > right else right + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1       

## Time Complexity:O(n)
## Space complexity:O(n) (最壞) / O(log n) (complete binary tree) 