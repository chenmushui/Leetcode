# -*- coding: utf-8 -*-
# @Time : 2022/8/13 20:36
# @Author : mushui
# @Site : https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-deng-jie-/
# @File : 768. 最多能完成排序的块 II2.py
# @Software: PyCharm
# 单调栈

from typing import *
class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]: stack.pop()
                stack.append(head)
            else: stack.append(num)
        return len(stack)

# 作者：jyd
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-deng-jie-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。