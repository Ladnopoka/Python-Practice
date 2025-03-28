from typing import List
from collections import deque

def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    answer = []
    k = len(queries)-1
    score = 0

    m = len(grid)
    n = len(grid[0])

    def bfs(limit):
        visited = set()
        queue = deque([(0,0)])
        count = 0

        #right down left up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        return count

    queries = sorted(queries)

    for i in range(len(queries)):
        if queries[i] > grid[i][0]:
            print("cell")
            score += 1
        else: 
            return -1


    return -1
    

def main():
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]

    result = maxPoints(grid, queries)
    print(f"Max points: {result}")

if __name__ == "__main__":
    main()
