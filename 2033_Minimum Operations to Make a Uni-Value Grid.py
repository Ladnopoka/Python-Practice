from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        my_arr = []

        # Flatten the grid into array
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                my_arr.append(grid[i][j])
        
        # Check if all numbers can be transformed into each other
        first_num = my_arr[0]
        for num in my_arr:
            if abs(num - first_num) % x != 0:
                return -1

        my_arr = sorted(my_arr)
        median_number = self.find_median(my_arr, x)

        minimum_changes = 0
        for i in range(len(my_arr)):
            if my_arr[i] != median_number:
                minimum_changes += abs(median_number - my_arr[i])
        
        return minimum_changes // x

    def find_median(self, array, val):
        n = len(array)

        if n % 2 == 1:
            return array[n//2]
        else:
            # For even length, return the left middle value
            return array[n//2 - 1]

def main():
    grid = [[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]]
    x = 84

    sol = Solution()
    result = sol.minOperations(grid, x)
    print(result)

if __name__ == "__main__":
    main()