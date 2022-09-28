# -*- coding: utf-8 -*-
# @Time : 2022/8/30 19:53
# @Author : mushui
# @Site : 
# @File : 998. 最大二叉树 II.py
# @Software: PyCharm 


# Definition for a binary tree node.
from typing import *
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

    def preorderTraversal(self, root): #中序遍历
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        print(root.val,end=' ')
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        b = []
        def dfs(node:TreeNode) -> None:
            if node == None:
                return
            dfs(node.left)
            if node.val != None:
                b.append(node.val)
            dfs(node.right)
        dfs(root)
        b.append(val)

        def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
            if nums == []:
                return None
            ma = max(nums)
            ma_index = nums.index(ma)
            node = TreeNode(ma,
                            constructMaximumBinaryTree(nums[:ma_index]),
                            constructMaximumBinaryTree(nums[ma_index + 1:]))
            return node
        node = constructMaximumBinaryTree(b)
        return node

if __name__ == '__main__':
    t = Tree()
    for node in [4,1,3,None,None,2]:
        t.add(node)
    t.preorderTraversal(t.root)
    t2 = Solution().insertIntoMaxTree(t.root,5)
    def predfs(node:TreeNode):
        if node ==None:
            return
        predfs(node.left)
        print(node.val)
        predfs(node.right)
    print('\n')
    predfs(t2)