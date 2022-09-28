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
if __name__ == '__main__':
    t = Tree()  # 实例化二叉树类，调用add方法，向二叉树中添加元素

    t.add(0)

    t.add(1)

    t.add(2)

    t.add(3)

    t.add(4)

    t.add(5)

    t.add(6)

    t.add(7)

    t.add(8)

    t.breadth()  # 调用breadth方法，打印二叉树
    print('\n')

    t.preorderTraversal(t.root)