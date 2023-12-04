class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    # Base case: if the array is empty, return None
    """
    Converts a sorted integer array into a height-balanced binary search tree.

    Args:
    - nums: A sorted list of integers.

    Returns:
    - TreeNode: The root of the resulting binary search tree.
    """
    if not nums:
        return None

    # Find the middle index of the array
    mid = len(nums) // 2

    # Create a new TreeNode with the value at the middle index
    root = TreeNode(nums[mid])

    # Recursively build the left subtree with the elements to the left of the middle index
    root.left = sorted_array_to_bst(nums[:mid])

    # Recursively build the right subtree with the elements to the right of the middle index
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

def inorder_traversal(root):
    """
    Performs an inorder traversal of the binary search tree and prints the values.

    Args:
    - root: The root of the binary search tree.
    """
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage:1
nums1 = [-10, -3, 0, 5, 9]
root1 = sorted_array_to_bst(nums1)
inorder_traversal(root1)
# Output: -10 0 -3 5 9

# Example usage:2
nums2 = [1, 3]
root2 = sorted_array_to_bst(nums2)
inorder_traversal(root2)
# Output: 1 3
