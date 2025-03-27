from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    # Construct tree from list
    values = [5, 4, 9, 1, 10, None, 7]
    root = build_tree_from_list(values)

    # Call the function to replace values in the tree (or whatever processing you need)
    replaceValueInTree(root)


def replaceValueInTree(root):
    if root is None:
        return

    queue = deque([(root, None)])  # Store (node, parent) pairs
    level = 0
    result = []  # To store sibling groups by level

    while queue:
        current_level_values = []
        current_level_nodes = []
        current_level_parents = []

        # Process all nodes at the current level
        for i in range(len(queue)):
            current_node, parent = queue.popleft()  # Unpack the node and its parent
            current_level_values.append(current_node.val)  # Store the value
            current_level_nodes.append(current_node)  # Store the node itself
            current_level_parents.append(parent)  # Track the parent

            # Enqueue left and right children with their parent
            if current_node.left:
                queue.append((current_node.left, current_node))  # Append (left child, parent)
            if current_node.right:
                queue.append((current_node.right, current_node))  # Append (right child, parent)

        # Group nodes by their parent (siblings)
        siblings = group_siblings_by_parent(current_level_nodes, current_level_parents)

        # Update the values of nodes based on the sibling group
        level_sum = sum(current_level_values)
        for sibling_group in siblings:
            sibling_sum = sum(node.val for node in sibling_group)
            for node in sibling_group:
                node.val = level_sum - sibling_sum  # Update each node's value

        # Save the sibling groups for debug purposes (optional)
        result.append([node.val for node in current_level_nodes])

        print(f"Level {level} values after replacement: {[node.val for node in current_level_nodes]}")

        level += 1

    print("Final result:", result)
    return root


def bfs_traversal(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current_level_values = []

        for i in range(len(queue)):
            current_node = queue.popleft()
            current_level_values.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        
        print(f"Level {i+1}: {current_level_values}")

def build_tree_from_list(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current_node = queue.popleft()

        # Add left child
        if index < len(values) and values[index] is not None:
            current_node.left = TreeNode(values[index])
            queue.append(current_node.left)
        index += 1

        # Add right child
        if index < len(values) and values[index] is not None:
            current_node.right = TreeNode(values[index])
            queue.append(current_node.right)
        index += 1

    return root

def group_siblings_by_parent(values, parents):
    """
    Helper function to group sibling nodes that have the same parent.
    :param values: List of node values at the current level.
    :param parents: List of parent nodes corresponding to the node values.
    :return: List of sibling groups.
    """
    siblings_dict = {}
    for i in range(len(values)):
        parent = parents[i]
        if parent not in siblings_dict:
            siblings_dict[parent] = []
        siblings_dict[parent].append(values[i])
    
    # Return a list of sibling groups
    return [sibling_group for sibling_group in siblings_dict.values()]

if __name__ == "__main__":
    main() 