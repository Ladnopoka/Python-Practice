"""
NeetCode 150 - Sliding Window Practice Problems
===============================================

This file contains practice problems for Sliding Window topic.
Each problem includes the problem description, constraints, and a solution template.

Topics covered:
- Fixed size sliding window
- Variable size sliding window
- Two pointer techniques
- String problems
- Array problems
- Subarray problems
"""

# Problem 1: Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve 
any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

def max_profit(prices):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Best Time to Buy and Sell Stock
def test_max_profit():
    print("Testing Best Time to Buy and Sell Stock:")
    print(max_profit([7,1,5,3,6,4]))  # Expected: 5
    print(max_profit([7,6,4,3,1]))    # Expected: 0
    print(max_profit([1,2,3,4,5]))    # Expected: 4
    print()

# Problem 2: Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

def length_of_longest_substring(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is the size of the charset
    """
    # Your solution here
    pass

# Test cases for Longest Substring Without Repeating Characters
def test_length_of_longest_substring():
    print("Testing Longest Substring Without Repeating Characters:")
    print(length_of_longest_substring("abcabcbb"))  # Expected: 3
    print(length_of_longest_substring("bbbbb"))     # Expected: 1
    print(length_of_longest_substring("pwwkew"))    # Expected: 3
    print(length_of_longest_substring(""))          # Expected: 0
    print()

# Problem 3: Longest Repeating Character Replacement
"""
You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation 
at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Example 1:
Input: s = "ABAB", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABB" or "ABBB".
The substring "BBBB" has the longest repeating letters, which is 4.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""

def character_replacement(s, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Longest Repeating Character Replacement
def test_character_replacement():
    print("Testing Longest Repeating Character Replacement:")
    print(character_replacement("ABAB", 1))      # Expected: 4
    print(character_replacement("AABABBA", 1))   # Expected: 4
    print(character_replacement("AAAA", 2))      # Expected: 4
    print()

# Problem 4: Permutation in String
"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""

def check_inclusion(s1, s2):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Permutation in String
def test_check_inclusion():
    print("Testing Permutation in String:")
    print(check_inclusion("ab", "eidbaooo"))   # Expected: True
    print(check_inclusion("ab", "eidboaoo"))   # Expected: False
    print(check_inclusion("hello", "ooolleoooleh"))  # Expected: False
    print()

# Problem 5: Minimum Window Substring
"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""

def min_window(s, t):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Minimum Window Substring
def test_min_window():
    print("Testing Minimum Window Substring:")
    print(min_window("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    print(min_window("a", "a"))                # Expected: "a"
    print(min_window("a", "aa"))               # Expected: ""
    print()

# Problem 6: Sliding Window Maximum
"""
You are given an array of integers nums, there is a sliding window of size k which is 
moving from the very left of the array to the very right. You can only see the k numbers 
in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

def max_sliding_window(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    # Your solution here
    pass

# Test cases for Sliding Window Maximum
def test_max_sliding_window():
    print("Testing Sliding Window Maximum:")
    print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                  # Expected: [1]
    print(max_sliding_window([1,-1], 1))               # Expected: [1,-1]
    print()

# Problem 7: Longest Substring with At Most Two Distinct Characters
"""
Given a string s, return the length of the longest substring that contains at most two 
distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:
- 1 <= s.length <= 5 * 10^4
- s consists of English letters.
"""

def length_of_longest_substring_two_distinct(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Longest Substring with At Most Two Distinct Characters
def test_length_of_longest_substring_two_distinct():
    print("Testing Longest Substring with At Most Two Distinct Characters:")
    print(length_of_longest_substring_two_distinct("eceba"))    # Expected: 3
    print(length_of_longest_substring_two_distinct("ccaabbb"))  # Expected: 5
    print(length_of_longest_substring_two_distinct("a"))        # Expected: 1
    print()

# Problem 8: Subarray Product Less Than K
"""
Given an array of integers nums and an integer k, return the number of contiguous 
subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6
"""

def num_subarray_product_less_than_k(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Subarray Product Less Than K
def test_num_subarray_product_less_than_k():
    print("Testing Subarray Product Less Than K:")
    print(num_subarray_product_less_than_k([10,5,2,6], 100))  # Expected: 8
    print(num_subarray_product_less_than_k([1,2,3], 0))       # Expected: 0
    print(num_subarray_product_less_than_k([1,1,1], 2))       # Expected: 6
    print()

# Problem 9: Maximum Sum Subarray of Size K
"""
Given an array of integers nums and an integer k, find the maximum sum of any contiguous 
subarray of size k.

Example 1:
Input: nums = [1, 4, 2, 10, 2, 3, 1, 0, 20], k = 4
Output: 24
Explanation: Subarray [4, 2, 10, 2] has the maximum sum of 24.

Example 2:
Input: nums = [100, 200, 300, 400], k = 2
Output: 700
Explanation: Subarray [300, 400] has the maximum sum of 700.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
- -10^4 <= nums[i] <= 10^4
"""

def max_sum_subarray_of_size_k(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Maximum Sum Subarray of Size K
def test_max_sum_subarray_of_size_k():
    print("Testing Maximum Sum Subarray of Size K:")
    print(max_sum_subarray_of_size_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))  # Expected: 24
    print(max_sum_subarray_of_size_k([100, 200, 300, 400], 2))           # Expected: 700
    print(max_sum_subarray_of_size_k([1, 2, 3, 4, 5], 3))                # Expected: 12
    print()

# Problem 10: Find All Anagrams in a String
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.
"""

def find_anagrams(s, p):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Your solution here
    pass

# Test cases for Find All Anagrams in a String
def test_find_anagrams():
    print("Testing Find All Anagrams in a String:")
    print(find_anagrams("cbaebabacd", "abc"))  # Expected: [0,6]
    print(find_anagrams("abab", "ab"))         # Expected: [0,1,2]
    print(find_anagrams("aaaa", "a"))          # Expected: [0,1,2,3]
    print()

# Run all tests
if __name__ == "__main__":
    print("=== NeetCode 150 - Sliding Window Practice ===\n")
    
    test_max_profit()
    test_length_of_longest_substring()
    test_character_replacement()
    test_check_inclusion()
    test_min_window()
    test_max_sliding_window()
    test_length_of_longest_substring_two_distinct()
    test_num_subarray_product_less_than_k()
    test_max_sum_subarray_of_size_k()
    test_find_anagrams()
    
    print("=== Practice Complete! ===")
    print("\nRemember to implement each function before running the tests!")
    print("Each problem includes the description, constraints, and expected time/space complexity.") 