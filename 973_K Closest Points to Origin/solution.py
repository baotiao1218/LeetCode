##這題要用heap sort, 但我直接sort掉了. heap sort解法詳見optimized 1

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            point.append((point[0]**2) + (point[1]**2))

        points.sort(key = lambda x:x[-1])

        for i in range(k):
            closest.append([points[i][0],points[i][1]])

        return closest