class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    """
    Finds the lowest common ancestor (LCA) node of two given nodes in a binary search tree (BST).

    Args:
    - root: The root of the BST.
    - p, q: The nodes for which to find the LCA.

    Returns:
    - TreeNode: The LCA node.
    """
    # Base case: if the root is None or one of the nodes is found, return the root
    if not root or root.val == p.val or root.val == q.val:
        return root

    # Recursively search in the left and right subtrees
    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    # If both nodes are found in different subtrees, the current root is the LCA
    if left_lca and right_lca:
        return root

    # If one of the nodes is found, return that node
    return left_lca if left_lca else right_lca

# Example usage:
# Construct the BST from the given input
root = TreeNode(6)
root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
root.right = TreeNode(8, TreeNode(7), TreeNode(9))

# Example 1:
p1 = TreeNode(2)
q1 = TreeNode(8)
result1 = lowestCommonAncestor(root, p1, q1)
print(result1.val)  # Output: 6

# Example 2:
p2 = TreeNode(2)
q2 = TreeNode(4)
result2 = lowestCommonAncestor(root, p2, q2)
print(result2.val)  # Output: 2

# Example 3:
root2 = TreeNode(2, TreeNode(1))
p3 = TreeNode(2)
q3 = TreeNode(1)
result3 = lowestCommonAncestor(root2, p3, q3)
print(result3.val)  # Output: 2
