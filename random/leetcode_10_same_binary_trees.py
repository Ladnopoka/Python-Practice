from typing import Optional

# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class with isSameTree method
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case: Both trees are empty → They are the same
        if not p and not q:
            return True
        
        # Base Case: One tree is empty but the other is not → Not the same
        if not p or not q:
            return False
        
        # Compare root values and recursively compare left and right subtrees
        return (p.val == q.val) and \
                self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

# Main function
def main():
    # Creating trees p = [1,2,3] and q = [1,2,3]
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    # Calling isSameTree
    sol = Solution()
    output = sol.isSameTree(p, q)
    print("Output of isSameTree:", output)

# Run the script
if __name__ == "__main__":
    main()
