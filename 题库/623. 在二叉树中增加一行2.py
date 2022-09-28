# -*- coding: utf-8 -*-
# @Time : 2022/8/5 23:27
# @Author : mushui
# @Site : https://leetcode.cn/problems/add-one-row-to-tree/solution/zai-er-cha-shu-zhong-zeng-jia-yi-xing-by-xcaf/
# @File : 623. 在二叉树中增加一行2.py.py
# @Software: PyCharm
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if root == None:
            return
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/add-one-row-to-tree/solution/zai-er-cha-shu-zhong-zeng-jia-yi-xing-by-xcaf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。