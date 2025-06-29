"""
NeetCode 150 - Binary Search Practice Problems
==============================================

This file contains practice problems for Binary Search topic.
Each problem includes the problem description, constraints, and a solution template.

Topics covered:
- Basic binary search
- Search in rotated sorted array
- Find peak element
- Search in 2D matrix
- Median of two sorted arrays
- Time-based problems
- Range-based problems
"""

# Problem 1: Binary Search
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""

def binary_search(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Binary Search
def test_binary_search():
    print("Testing Binary Search:")
    print(binary_search([-1,0,3,5,9,12], 9))   # Expected: 4
    print(binary_search([-1,0,3,5,9,12], 2))   # Expected: -1
    print(binary_search([5], 5))                # Expected: 0
    print(binary_search([5], -5))               # Expected: -1
    print()

# Problem 2: Search in Rotated Sorted Array
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the 
index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4
"""

def search_rotated_sorted_array(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Search in Rotated Sorted Array
def test_search_rotated_sorted_array():
    print("Testing Search in Rotated Sorted Array:")
    print(search_rotated_sorted_array([4,5,6,7,0,1,2], 0))  # Expected: 4
    print(search_rotated_sorted_array([4,5,6,7,0,1,2], 3))  # Expected: -1
    print(search_rotated_sorted_array([1], 0))              # Expected: -1
    print(search_rotated_sorted_array([1,3], 3))            # Expected: 1
    print()

# Problem 3: Find Minimum in Rotated Sorted Array
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the 
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

def find_min_rotated_sorted_array(nums):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Find Minimum in Rotated Sorted Array
def test_find_min_rotated_sorted_array():
    print("Testing Find Minimum in Rotated Sorted Array:")
    print(find_min_rotated_sorted_array([3,4,5,1,2]))       # Expected: 1
    print(find_min_rotated_sorted_array([4,5,6,7,0,1,2]))   # Expected: 0
    print(find_min_rotated_sorted_array([11,13,15,17]))     # Expected: 11
    print(find_min_rotated_sorted_array([2,1]))             # Expected: 1
    print()

# Problem 4: Search a 2D Matrix
"""
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
"""

def search_2d_matrix(matrix, target):
    """
    Time Complexity: O(log(m * n))
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Search a 2D Matrix
def test_search_2d_matrix():
    print("Testing Search a 2D Matrix:")
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search_2d_matrix(matrix1, 3))   # Expected: True
    print(search_2d_matrix(matrix1, 13))  # Expected: False
    print(search_2d_matrix(matrix1, 60))  # Expected: True
    print()

# Problem 5: Koko Eating Bananas
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile 
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she 
eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the 
guards come back.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

def min_eating_speed(piles, h):
    """
    Time Complexity: O(n * log(max(piles)))
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Koko Eating Bananas
def test_min_eating_speed():
    print("Testing Koko Eating Bananas:")
    print(min_eating_speed([3,6,7,11], 8))           # Expected: 4
    print(min_eating_speed([30,11,23,4,20], 5))      # Expected: 30
    print(min_eating_speed([30,11,23,4,20], 6))      # Expected: 23
    print()

# Problem 6: Find Peak Element
"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always 
considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.
"""

def find_peak_element(nums):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Find Peak Element
def test_find_peak_element():
    print("Testing Find Peak Element:")
    print(find_peak_element([1,2,3,1]))           # Expected: 2
    print(find_peak_element([1,2,1,3,5,6,4]))     # Expected: 1 or 5
    print(find_peak_element([1]))                 # Expected: 0
    print()

# Problem 7: Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the 
target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""

def search_insert(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Search Insert Position
def test_search_insert():
    print("Testing Search Insert Position:")
    print(search_insert([1,3,5,6], 5))  # Expected: 2
    print(search_insert([1,3,5,6], 2))  # Expected: 1
    print(search_insert([1,3,5,6], 7))  # Expected: 4
    print(search_insert([1,3,5,6], 0))  # Expected: 0
    print()

# Problem 8: Capacity To Ship Packages Within D Days
"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the 
ship with packages on the conveyor belt (in the order given by weights). We may not load 
more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on 
the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
- 1 <= days <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500
"""

def ship_within_days(weights, days):
    """
    Time Complexity: O(n * log(sum(weights)))
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Capacity To Ship Packages Within D Days
def test_ship_within_days():
    print("Testing Capacity To Ship Packages Within D Days:")
    print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5))  # Expected: 15
    print(ship_within_days([3,2,2,4,1,4], 3))           # Expected: 6
    print(ship_within_days([1,2,3,1,1], 4))             # Expected: 3
    print()

# Run all tests
if __name__ == "__main__":
    print("=== NeetCode 150 - Binary Search Practice ===\n")
    
    test_binary_search()
    test_search_rotated_sorted_array()
    test_find_min_rotated_sorted_array()
    test_search_2d_matrix()
    test_min_eating_speed()
    test_find_peak_element()
    test_search_insert()
    test_ship_within_days()
    
    print("=== Practice Complete! ===")
    print("\nRemember to implement each function before running the tests!")
    print("Each problem includes the description, constraints, and expected time/space complexity.") 