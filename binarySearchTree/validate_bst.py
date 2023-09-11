"""A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this is recursive
        # right child of 1st left child is limited by parent
        # left child of 1st right child is limited by parent

        if not root:
            return True
        left = root.left
        while left:
            if left.val >= root.val:
                return False
            left = left.right
        
        right = root.right
        while right:
            if right.val <= root.val:
                return False
            right = right.left

        if not self.isValidBST(root.right) or not self.isValidBST(root.left):
            return False
        return True