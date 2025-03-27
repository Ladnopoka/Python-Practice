from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]):

        my_tree = TreeNode()

        for i in range(len(nums)):
            if nums[i] < my_tree.val:
                my_tree.left = TreeNode(nums[i])
            else:
                my_tree.right = TreeNode(nums[i])

        return my_tree
        
# Main function
def main():
    tree = [-10,-3,0,5,9]
    sol = Solution()

    binary_tree = sol.sortedArrayToBST(tree)

    inorder_traversal(binary_tree)
    
    def inorder_traversal(root):
        if root is None:
            return
        
        inorder_traversal(binary_tree.left)
        print(binary_tree.val)
        inorder_traversal(binary_tree.right)


# Run the script
if __name__ == "__main__":
    main()