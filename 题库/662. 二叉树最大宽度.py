# -*- coding: utf-8 -*-
# @Time : 2022/8/27 16:57
# @Author : mushui
# @Site : 
# @File : 662. 二叉树最大宽度.py
# @Software: PyCharm 

#bfs
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        h = -1
        w_ls = []
        while q:
            h += 1
            n = len(q)
            lf = 0
            # w_ls.append(q. - q.index(0)+1)
            for _ in range(n):
                node,ind = q.popleft()
                if _ == 0:
                    lf = ind
                if _ == n-1:
                    w_ls.append(ind - lf+1)
                if node.left:
                    q.append((node.left,2*ind+1))
                if node.right:
                    q.append((node.right,2*ind+2))
        return max(w_ls)

#已经ac 答案bfs 用的next队列
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for node, index in arr:
                if node.left:
                    tmp.append([node.left, index * 2])
                if node.right:
                    tmp.append([node.right, index * 2 + 1])
            res = max(res, arr[-1][1] - arr[0][1] + 1)
            arr = tmp
        return res
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-width-of-binary-tree/solution/er-cha-shu-zui-da-kuan-du-by-leetcode-so-9zp3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#dfs
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelMin = {}
        def dfs(node: Optional[TreeNode], depth: int, index: int) -> int:
            if node is None:
                return 0
            if depth not in levelMin:
                levelMin[depth] = index  # 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return max(index - levelMin[depth] + 1,
                       dfs(node.left, depth + 1, index * 2),
                       dfs(node.right, depth + 1, index * 2 + 1))
        return dfs(root, 1, 1)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-width-of-binary-tree/solution/er-cha-shu-zui-da-kuan-du-by-leetcode-so-9zp3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#bfs
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(root, 1)])
        max_wide = 1
        while dq:
            max_wide = max(dq[-1][1] - dq[0][1] + 1, max_wide)
            for _ in range(len(dq)):
                node, index = dq.popleft()
                if node.left:
                    dq.append((node.left, index * 2))
                if node.right:
                    dq.append((node.right, index * 2 + 1))
        return max_wide