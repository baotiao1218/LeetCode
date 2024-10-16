#My Original Answer (Recursive)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def landFinder(nc:int, nr:int) -> bool:
            if nc < 0 or nr < 0 or nc >= len(grid) or nr >= len(grid[0]) or grid[nc][nr] == "0" or grid[nc][nr] == "-1":
                return False
            
            found = False
            if grid[nc][nr] == "1":
                grid[nc][nr] = "-1"
                found = True

            a = landFinder(nc+1, nr)
            b = landFinder(nc-1, nr)
            c = landFinder(nc, nr+1)
            d = landFinder(nc, nr-1)

            return found or a or b or c or d

        numOfIsland = 0
        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if landFinder(c,r):
                    numOfIsland += 1

        return numOfIsland
    
## Time Complexity:O(m*n)
## Space Complexity:O(m*n)


#Optimized 1:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def landFinder(nc:int, nr:int):
            if nc < 0 or nr < 0 or nc >= len(grid) or nr >= len(grid[0]) or grid[nc][nr] == "0" or grid[nc][nr] == "0":
                return False
            # 直接把計算過的土地變成0
            grid[nc][nr] = "0"

            landFinder(nc+1, nr)
            landFinder(nc-1, nr)
            landFinder(nc, nr+1)
            landFinder(nc, nr-1)

        numOfIsland = 0
        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[c][r] == '1':
                    numOfIsland += 1
                    landFinder(c,r)

        return numOfIsland
    
## Time Complexity:O(m*n)
## Space Complexity:O(m*n)