"""
NeetCode 150 - Arrays & Hashing Practice Problems
================================================

This file contains practice problems for Arrays & Hashing topic.
Each problem includes the problem description, constraints, and a solution template.

Topics covered:
- Hash maps/sets
- Array manipulation
- Two sum variations
- Frequency counting
- Anagram problems
"""

# Problem 1: Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

def two_sum(nums, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Two Sum
def test_two_sum():
    print("Testing Two Sum:")
    print(two_sum([2,7,11,15], 9))  # Expected: [0,1]
    print(two_sum([3,2,4], 6))      # Expected: [1,2]
    print(two_sum([3,3], 6))        # Expected: [0,1]
    print()

# Problem 2: Contains Duplicate
"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def contains_duplicate(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Contains Duplicate
def test_contains_duplicate():
    print("Testing Contains Duplicate:")
    print(contains_duplicate([1,2,3,1]))           # Expected: True
    print(contains_duplicate([1,2,3,4]))           # Expected: False
    print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # Expected: True
    print()

# Problem 3: Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

def is_anagram(s, t):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size alphabet
    """
    # Your solution here
    pass

# Test cases for Valid Anagram
def test_is_anagram():
    print("Testing Valid Anagram:")
    print(is_anagram("anagram", "nagaram"))  # Expected: True
    print(is_anagram("rat", "car"))          # Expected: False
    print(is_anagram("", ""))                # Expected: True
    print()

# Problem 4: Group Anagrams
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

def group_anagrams(strs):
    """
    Time Complexity: O(n * k * log k) where n is number of strings, k is max string length
    Space Complexity: O(n * k)
    """
    # Your solution here
    pass

# Test cases for Group Anagrams
def test_group_anagrams():
    print("Testing Group Anagrams:")
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["a"]))
    print()

# Problem 5: Top K Frequent Elements
"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.
"""

def top_k_frequent(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Top K Frequent Elements
def test_top_k_frequent():
    print("Testing Top K Frequent Elements:")
    print(top_k_frequent([1,1,1,2,2,3], 2))  # Expected: [1,2]
    print(top_k_frequent([1], 1))             # Expected: [1]
    print(top_k_frequent([1,1,1,2,2,3,3,3], 2))  # Expected: [1,3]
    print()

# Problem 6: Product of Array Except Self
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, answer[2] = 1*2*4 = 8, answer[3] = 1*2*3 = 6

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

def product_except_self(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) - output array doesn't count
    """
    # Your solution here
    pass

# Test cases for Product of Array Except Self
def test_product_except_self():
    print("Testing Product of Array Except Self:")
    print(product_except_self([1,2,3,4]))        # Expected: [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3]))    # Expected: [0,0,9,0,0]
    print()

# Problem 7: Valid Sudoku
"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
"""

def is_valid_sudoku(board):
    """
    Time Complexity: O(n^2) where n = 9
    Space Complexity: O(n^2)
    """
    # Your solution here
    pass

# Test cases for Valid Sudoku
def test_is_valid_sudoku():
    print("Testing Valid Sudoku:")
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(is_valid_sudoku(board1))  # Expected: True
    print()

# Problem 8: Longest Consecutive Sequence
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def longest_consecutive(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Longest Consecutive Sequence
def test_longest_consecutive():
    print("Testing Longest Consecutive Sequence:")
    print(longest_consecutive([100,4,200,1,3,2]))      # Expected: 4
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))  # Expected: 9
    print(longest_consecutive([]))                     # Expected: 0
    print()

# Run all tests
if __name__ == "__main__":
    print("=== NeetCode 150 - Arrays & Hashing Practice ===\n")
    
    test_two_sum()
    test_contains_duplicate()
    test_is_anagram()
    test_group_anagrams()
    test_top_k_frequent()
    test_product_except_self()
    test_is_valid_sudoku()
    test_longest_consecutive()
    
    print("=== Practice Complete! ===")
    print("\nRemember to implement each function before running the tests!")
    print("Each problem includes the description, constraints, and expected time/space complexity.") 