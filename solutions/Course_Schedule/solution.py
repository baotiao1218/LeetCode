#(Recursive)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numCourses
        queue = deque([])

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indeg[pre[0]] += 1

        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)
        
        visited = 0
        
        while queue:
            deg = queue.popleft()
            visited += 1
            for neighbor in adj[deg]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == visited
    
## Time Complexity:O(V+E) V=節點數 E="邊"
## Space Complexity:O(V+E)
