# -*- coding: utf-8 -*-
# @Time : 2022/8/22 10:25
# @Author : mushui
# @Site : 
# @File : 655. 输出二叉树.py
# @Software: PyCharm 

#bfs
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import *
import math
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calDepth(root: Optional[TreeNode]) -> int:
            h = -1
            q = [root]
            while q:
                h += 1
                tmp = q
                q = []
                for node in tmp:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return h
        height = calDepth(root)

        m = height + 1
        n = 2 ** m - 1
        ans = [[''] * n for _ in range(m)]
        q = deque([(root, 0, (n - 1) // 2)])
        while q:
            node, r, c = q.popleft()
            ans[r][c] = str(node.val)
            if node.left:
                q.append((node.left, r + 1, c - 2 ** (height - r - 1)))
            if node.right:
                q.append((node.right, r + 1, c + 2 ** (height - r - 1)))
        return ans
