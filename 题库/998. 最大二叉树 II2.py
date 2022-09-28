# -*- coding: utf-8 -*-
# @Time : 2022/8/30 22:28
# @Author : mushui
# @Site : 
# @File : 998. 最大二叉树 II2.py
# @Software: PyCharm 


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent, cur = None, root
        while cur:
            if val > cur.val:
                if not parent:
                    return TreeNode(val, root, None)
                node = TreeNode(val, cur, None)
                parent.right = node
                return root
            else:
                parent = cur
                cur = cur.right

        parent.right = TreeNode(val)
        return root

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / maximum - binary - tree - ii / solution / zui - da - er - cha - shu - ii - by - leetcode - solutio - piv2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。