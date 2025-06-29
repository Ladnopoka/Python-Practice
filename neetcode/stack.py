"""
NeetCode 150 - Stack Practice Problems
=====================================

This file contains practice problems for Stack topic.
Each problem includes the problem description, constraints, and a solution template.

Topics covered:
- Stack operations (push, pop, peek)
- Parentheses matching
- Monotonic stack
- Expression evaluation
- Next greater element
- Valid parentheses variations
"""

# Problem 1: Valid Parentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

def is_valid_parentheses(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Valid Parentheses
def test_is_valid_parentheses():
    print("Testing Valid Parentheses:")
    print(is_valid_parentheses("()"))           # Expected: True
    print(is_valid_parentheses("()[]{}"))       # Expected: True
    print(is_valid_parentheses("(]"))           # Expected: False
    print(is_valid_parentheses("([)]"))         # Expected: False
    print(is_valid_parentheses("{[]}"))         # Expected: True
    print()

# Problem 2: Min Stack
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

class MinStack:
    """
    Time Complexity: O(1) for all operations
    Space Complexity: O(n)
    """
    def __init__(self):
        # Your implementation here
        pass
    
    def push(self, val):
        # Your implementation here
        pass
    
    def pop(self):
        # Your implementation here
        pass
    
    def top(self):
        # Your implementation here
        pass
    
    def getMin(self):
        # Your implementation here
        pass

# Test cases for Min Stack
def test_min_stack():
    print("Testing Min Stack:")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"getMin: {minStack.getMin()}")  # Expected: -3
    minStack.pop()
    print(f"top: {minStack.top()}")        # Expected: 0
    print(f"getMin: {minStack.getMin()}")  # Expected: -2
    print()

# Problem 3: Evaluate Reverse Polish Notation
"""
You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

def eval_rpn(tokens):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Evaluate Reverse Polish Notation
def test_eval_rpn():
    print("Testing Evaluate Reverse Polish Notation:")
    print(eval_rpn(["2","1","+","3","*"]))                    # Expected: 9
    print(eval_rpn(["4","13","5","/","+"]))                   # Expected: 6
    print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Expected: 22
    print()

# Problem 4: Generate Parentheses
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
"""

def generate_parentheses(n):
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(4^n / sqrt(n))
    """
    # Your solution here
    pass

# Test cases for Generate Parentheses
def test_generate_parentheses():
    print("Testing Generate Parentheses:")
    print(generate_parentheses(3))  # Expected: ["((()))","(()())","(())()","()(())","()()()"]
    print(generate_parentheses(1))  # Expected: ["()"]
    print()

# Problem 5: Daily Temperatures
"""
Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to 
get a warmer temperature. If there is no future day for which this is possible, keep 
answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

def daily_temperatures(temperatures):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Daily Temperatures
def test_daily_temperatures():
    print("Testing Daily Temperatures:")
    print(daily_temperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30,40,50,60]))              # Expected: [1,1,1,0]
    print(daily_temperatures([30,60,90]))                 # Expected: [1,1,0]
    print()

# Problem 6: Car Fleet
"""
There are n cars going to the same destination along a one-lane road. The destination is 
target miles away.

You are given two integer array position and speed, both of length n, where position[i] 
is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper 
to bumper at the same speed. The faster car will slow down to match the slower car's speed. 
The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. 
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be 
considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. 
The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 10^6
"""

def car_fleet(target, position, speed):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Car Fleet
def test_car_fleet():
    print("Testing Car Fleet:")
    print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # Expected: 3
    print(car_fleet(10, [3], [3]))                    # Expected: 1
    print(car_fleet(100, [0,2,4], [4,2,1]))           # Expected: 1
    print()

# Problem 7: Largest Rectangle in Histogram
"""
Given an array of integers heights representing the histogram's bar height where the 
width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

def largest_rectangle_area(heights):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Largest Rectangle in Histogram
def test_largest_rectangle_area():
    print("Testing Largest Rectangle in Histogram:")
    print(largest_rectangle_area([2,1,5,6,2,3]))  # Expected: 10
    print(largest_rectangle_area([2,4]))          # Expected: 4
    print(largest_rectangle_area([1]))            # Expected: 1
    print()

# Problem 8: Simplify Path
"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or 
directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period 
'..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') 
are treated as a single slash '/'. For this problem, any other format of periods such as 
'...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target 
  file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is 
the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or underscore '_'.
- path is a valid absolute Unix path.
"""

def simplify_path(path):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Your solution here
    pass

# Test cases for Simplify Path
def test_simplify_path():
    print("Testing Simplify Path:")
    print(simplify_path("/home/"))        # Expected: "/home"
    print(simplify_path("/../"))          # Expected: "/"
    print(simplify_path("/home//foo/"))   # Expected: "/home/foo"
    print(simplify_path("/a/./b/../../c/"))  # Expected: "/c"
    print()

# Run all tests
if __name__ == "__main__":
    print("=== NeetCode 150 - Stack Practice ===\n")
    
    test_is_valid_parentheses()
    test_min_stack()
    test_eval_rpn()
    test_generate_parentheses()
    test_daily_temperatures()
    test_car_fleet()
    test_largest_rectangle_area()
    test_simplify_path()
    
    print("=== Practice Complete! ===")
    print("\nRemember to implement each function before running the tests!")
    print("Each problem includes the description, constraints, and expected time/space complexity.") 