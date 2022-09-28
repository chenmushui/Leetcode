# -*- coding: utf-8 -*-
# @Time : 2022/7/31 22:47
# @Author : mushui
# @Site : https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/solution/zui-da-ceng-nei-yuan-su-he-by-leetcode-s-2tm4/
# @File : 1161.最大层内元素和2.py
# @Software: PyCharm 
#dfs

from typing import *
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
        summ = []
        def dfs(node:TreeNode,level:int)->None: #先序遍历
            if node == None:
                return
            if level == len(summ): #判断是不是当前层第一个结点
                summ.append(node.val)
            else:
                summ[level] += node.val #如果不是就让加入到当前层
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return summ.index(max(summ))+1