# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *


class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        s = 0
        max_level = -1

        def dfs(node: TreeNode, level: int):
            nonlocal s  # nonlocal用于函数嵌套中变量
            nonlocal max_level
            if node == None:
                return
            if max_level < level:
                max_level = level
                s = 0
            if level == max_level and node.right == None and node.left == None:
                s += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return s
