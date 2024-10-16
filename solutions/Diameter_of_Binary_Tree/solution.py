class Solution:
    def __init__(self):
        self.maxlength = 0
    def height(self, root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            
            left = self.height(root.left)
            right = self.height(root.right)

            if (left + right) > self.maxlength:
                self.maxlength = left+right

            return left + 1 if left > right else right + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        
        return self.maxlength

"""
Note:
原本把max跟length的比較，擺在left/right + 1之後，當時思慮不周，沒考慮到+1的值是回傳給上面，
而非本次執行的值。

後來將max的比較放在+1前，就正常了。
"""
## Time Complexity: O(n) (全部都走一次)
## Space complexity:O(n) (全部都走一次)