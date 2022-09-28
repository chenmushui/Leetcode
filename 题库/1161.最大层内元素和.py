# -*- coding: utf-8 -*-
# @Time : 2022/7/31 17:49
# @Author : mushui
# @Site : 
# @File : 1161.最大层内元素和.py
# @Software: PyCharm
#bfs
from typing import *
from numpy import *
class TreeNode:
    def __init__(self, val = 0, left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class BinTree:
    def __init__(self):
        self.root = None
from collections import *
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, maxx = 1,-inf
        q, level = [root], 1
        while q:
            summ, nq = 0, [] #采用双队列，nq 是存下一层结点的队列
            for node in q:
                summ += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if summ>maxx:
                maxx = summ
                ans = level
            q = nq
            level +=1
        return ans