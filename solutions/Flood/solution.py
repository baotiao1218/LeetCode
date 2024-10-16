class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        def fill(r:int, c:int):
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return
            if image[r][c] != target:
                return
            if image[r][c] == color:
                return
            
            image[r][c] = color

            fill(r+1,c)
            fill(r-1,c)
            fill(r,c+1)
            fill(r,c-1)

        fill(sr,sc)
        
        return image

## Time Complexity: O(m*n)
## Space complexity: O(m*n) (遞迴深度 depth of recursion)