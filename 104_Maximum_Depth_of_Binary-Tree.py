from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class with findAllRecipes method
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        max_depth = max(left_depth, right_depth)

        return max_depth + 1
        

# Main function
def main():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()

    print(sol.maxDepth(tree))

# Run the script
if __name__ == "__main__":
    main()