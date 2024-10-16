# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def helper(node, height):
            if node == None:
                return None
            if len(ans) == height:
                ans.append([])
            ans[height].append(node.val)
            if node.left:
                helper(node.left, height + 1)
            if node.right:
                helper(node.right, height + 1) 

        helper(root, 0)             

        return ans

## Time Complexity:O(n)
## Space complexity:O(n)


#Optimized Answer (Iteration)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = [root]
        ans = []

        while Q:
            level_length = len(Q)
            level_list = []

            for i in range(level_length):
                node = Q.pop(0)
                level_list.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            ans.append(level_list)

        return ans
    
# Queue剩下的剛好都在同一層

## Time Complexity:O(n)
## Space complexity:O(n)