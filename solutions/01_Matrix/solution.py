class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        m,n = len(mat), len(mat[0])
        direction = [0,1,0,-1,0]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append([r,c])
                else:
                    mat[r][c] = -1
        
        while queue:
            r,c = queue.pop(0)
            for i in range(4):
                nr, nc = r + direction[i], c + direction[i+1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] != -1:
                    continue
                    
                mat[nr][nc] = mat[r][c] + 1
                queue.append([nr,nc])
        
        return mat
    
## Time Complexity: O(m*n)
## Space Complexity: O(m*n) (如果每個元素都不等於0, 就都要存入)


#Optimized Answer 1
class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat
    
## Time Complexity: O(m*n)
## Space Complexity: O(1) (就地改數字)