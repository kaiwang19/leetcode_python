# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.result