from typing import List
import heapq

# # Solution class with findAllRecipes method
# class Solution:
#     def practice():
#         grid = [
#             [1, 3, 5],
#             [2, 4, 6],
#             [0, 7, 8]
#         ]

#         rows, cols = len(grid), len(grid[0])

#         visited = [[False] * cols for _ in range(rows)]
#         print(visited)

#         return visited















# Main function
def main():
    # grid = [
    #     [1, 3, 5],
    #     [2, 4, 6],
    #     [0, 7, 8]
    # ]

    grid = [
        [0, 4],
        [4, 4]
    ]

    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # Initialize starting cell
    dp[0][0] = grid[0][0]

    # Fill first row (can only come from left)
    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
        print(f"Visiting cell (0,{c}) with value {grid[0][c]}")

    # Fill first column (can only come from above)
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
        print(f"Visiting cell ({r},0) with value {grid[r][0]}")

    # Fill the rest of the table
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
            print(f"Visiting cell ({r},{c}) with value {grid[r][c]}")

    # Minimum cost to reach bottom-right
    print(f"Minimum cost to reach ({rows-1}, {cols-1}) is {dp[rows-1][cols-1]}")

    

# Run the script
if __name__ == "__main__":
    main()