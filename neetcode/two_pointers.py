"""
NeetCode 150 - Two Pointers Practice Problems
============================================

This file contains practice problems for Two Pointers topic.
Each problem includes the problem description, constraints, and a solution template.

Topics covered:
- Two pointer techniques
- Array manipulation with pointers
- String manipulation
- Linked list problems
- Container with most water
- Three sum variations
"""

# Problem 1: Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

def is_palindrome(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Valid Palindrome
def test_is_palindrome():
    print("Testing Valid Palindrome:")
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(is_palindrome("race a car"))                      # Expected: False
    print(is_palindrome(" "))                               # Expected: True
    print(is_palindrome("0P"))                              # Expected: False
    print()

# Problem 2: Two Sum II - Input Array Is Sorted
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""

def two_sum_sorted(numbers, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Two Sum II
def test_two_sum_sorted():
    print("Testing Two Sum II - Input Array Is Sorted:")
    print(two_sum_sorted([2,7,11,15], 9))  # Expected: [1,2]
    print(two_sum_sorted([2,3,4], 6))      # Expected: [1,3]
    print(two_sum_sorted([-1,0], -1))      # Expected: [1,2]
    print()

# Problem 3: 3Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

def three_sum(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1) - output space not counted
    """
    # Your solution here
    pass

# Test cases for 3Sum
def test_three_sum():
    print("Testing 3Sum:")
    print(three_sum([-1,0,1,2,-1,-4]))  # Expected: [[-1,-1,2],[-1,0,1]]
    print(three_sum([]))                # Expected: []
    print(three_sum([0]))               # Expected: []
    print()

# Problem 4: Container With Most Water
"""
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines, which, together with the x-axis forms a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

def max_area(height):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Container With Most Water
def test_max_area():
    print("Testing Container With Most Water:")
    print(max_area([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(max_area([1,1]))                 # Expected: 1
    print(max_area([4,3,2,1,4]))           # Expected: 16
    print()

# Problem 5: Trapping Rain Water
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

def trap(height):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Trapping Rain Water
def test_trap():
    print("Testing Trapping Rain Water:")
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected: 6
    print(trap([4,2,0,3,2,5]))               # Expected: 9
    print(trap([2,0,2]))                     # Expected: 2
    print()

# Problem 6: Remove Duplicates from Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should 
be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do 
the following things:

1. Change the array nums such that the first k elements of nums contain the unique elements 
   in the order they were present in nums initially. The remaining elements of nums are not 
   important as well as the size of nums.
2. Return k.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

def remove_duplicates(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Remove Duplicates from Sorted Array
def test_remove_duplicates():
    print("Testing Remove Duplicates from Sorted Array:")
    nums1 = [1,1,2]
    k1 = remove_duplicates(nums1)
    print(f"k={k1}, nums={nums1[:k1]}")  # Expected: k=2, nums=[1,2]
    
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = remove_duplicates(nums2)
    print(f"k={k2}, nums={nums2[:k2]}")  # Expected: k=5, nums=[0,1,2,3,4]
    print()

# Problem 7: Move Zeroes
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""

def move_zeroes(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Move Zeroes
def test_move_zeroes():
    print("Testing Move Zeroes:")
    nums1 = [0,1,0,3,12]
    move_zeroes(nums1)
    print(nums1)  # Expected: [1,3,12,0,0]
    
    nums2 = [0]
    move_zeroes(nums2)
    print(nums2)  # Expected: [0]
    
    nums3 = [1,2,3,4,5]
    move_zeroes(nums3)
    print(nums3)  # Expected: [1,2,3,4,5]
    print()

# Problem 8: Is Subsequence
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
"""

def is_subsequence(s, t):
    """
    Time Complexity: O(n) where n is length of t
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Is Subsequence
def test_is_subsequence():
    print("Testing Is Subsequence:")
    print(is_subsequence("abc", "ahbgdc"))  # Expected: True
    print(is_subsequence("axc", "ahbgdc"))  # Expected: False
    print(is_subsequence("", "ahbgdc"))     # Expected: True
    print(is_subsequence("abc", ""))        # Expected: False
    print()

# Run all tests
if __name__ == "__main__":
    print("=== NeetCode 150 - Two Pointers Practice ===\n")
    
    test_is_palindrome()
    test_two_sum_sorted()
    test_three_sum()
    test_max_area()
    test_trap()
    test_remove_duplicates()
    test_move_zeroes()
    test_is_subsequence()
    
    print("=== Practice Complete! ===")
    print("\nRemember to implement each function before running the tests!")
    print("Each problem includes the description, constraints, and expected time/space complexity.") 