# -*- coding: utf-8 -*-
# @Time : 2022/8/20 12:34
# @Author : mushui
# @Site : 
# @File : 654. 最大二叉树.py
# @Software: PyCharm 


# Definition for a binary tree node.
from typing import *
from collections import deque
# -*- coding: utf-8 -*-
# @Time : 2022/8/1 16:22
# @Author : mushui
# @Site :
# @File : 二叉树.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):#root定义的根节点

        self.root=None

    def add(self,item):
        node = TreeNode(item)  # 将Node类实例化参数node

        if self.root is None:
            self.root = node

            return

        queue = [self.root]  # 创建一个队列，将根节点放入队列中

        while queue:

            cur_node = queue.pop(0)  # 向队列queue中取出第一个节点进行判断

            if cur_node.left is None:

                cur_node.left = node

                return

            else:

                queue.append(cur_node.left)

            if cur_node.right is None:

                cur_node.right = node

                return

            else:

                queue.append(cur_node.right)

    def  breadth(self):
        if self.root is None:  # 首先判断根节点是否为空，为空则返回

            return

        queue = [self.root]  # 将根节点放入队列中

        while queue:

            cur_node = queue.pop(0)  # 取出节点

            print(cur_node.val, end=' ')  # 打印节点值，也是广度遍历的值

            if cur_node.left is not None:  # 判断左子树

                queue.append(cur_node.left)

            if cur_node.right is not None:  # 判断右子树

                queue.append(cur_node.right)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        ma = max(nums)
        ma_index = nums.index(ma)
        node = TreeNode(ma,
                        self.constructMaximumBinaryTree(nums[:ma_index]),
                        self.constructMaximumBinaryTree(nums[ma_index+1:]))
        return node

