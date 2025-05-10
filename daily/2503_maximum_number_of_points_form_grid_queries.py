from typing import List
from collections import deque
import heapq

def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    m, n = len(grid), len(grid[0])
    
    # Create sorted queries with original indices
    indexed_queries = sorted((q, i) for i, q in enumerate(queries))
    answer = [0] * len(queries)
    
    # BFS data structures
    visited = set([(0, 0)])
    heap = [(grid[0][0], 0, 0)]  # (value, row, col)
    count = 0
    
    # Directions for adjacent cells
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Process each cell in ascending order
    for query_val, query_idx in indexed_queries:
        # Process all cells with values less than query_val
        while heap and heap[0][0] < query_val:
            _, row, col = heapq.heappop(heap)
            count += 1
            
            # Check neighbors
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if (0 <= new_row < m and 
                    0 <= new_col < n and 
                    (new_row, new_col) not in visited):
                    
                    visited.add((new_row, new_col))
                    heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
        
        # Store result for this query
        answer[query_idx] = count if grid[0][0] < query_val else 0
    
    return answer

# def quicksort(array):
#     if not array:
#         return array
#     if not isinstance(array[0], tuple):
#         array = list(enumerate(array))


#     if len(array) <= 1:
#         return array
    
#     pivot = array[-1][0]
#     left = []
#     right = []
#     middle = []

#     for i in array:
#         value = i[0]
#         if pivot == value:
#             middle.append(i)
#         elif pivot > value:
#             left.append(i)
#         else:
#             right.append(i)

#     return quicksort(left) + middle + quicksort(right)
    
# def bfs(limit, grid, m, n):
#     #data structures
#     visited = set() #keep track of visited cells
#     queue = deque([(0,0)])  #start from top left cell
#     count = 0 #count cells we can visit

#     #add starting point to visited set
#     visited.add((0,0))

#     #process queue while it is not empty
#     while queue:
#         current_row, current_col = queue.popleft()   #get current cell coordinates

#         if grid[current_row][current_col] < limit:  #process current cell
#             count += 1

#             for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:  #check all 4 directions
#                 new_row = current_row + dx
#                 new_col = current_col + dy

#                 if (0 <= new_row < m and    #validate new coordinates
#                     0 <= new_col < n and
#                     (new_row, new_col) not in visited and
#                     grid[new_row][new_col] < limit):

#                     queue.append((new_row, new_col))    #add valid neighbors to queue and visited
#                     visited.add((new_row, new_col))

#     return count

def main():
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    grid2 = [[5,2,1],[1,1,2]]
    queries2 = [3]
    queries = [5,6,2]
    grid3 = [[100, 1000, 10000], [500, 400, 1]]
    queries3 = [1000000, 3, 5000, 2]
    grid4 = [[1, 3], [2, 4]]
    queries4 = [1000000]

    result = maxPoints(grid3, queries3)
    print(f"Max points: {result}")

if __name__ == "__main__":
    main()
