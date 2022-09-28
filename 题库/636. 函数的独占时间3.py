# -*- coding: utf-8 -*-
# @Time : 2022/8/7 17:00
# @Author : mushui
# @Site : https://leetcode.cn/problems/exclusive-time-of-functions/solution/han-shu-de-du-zhan-shi-jian-by-leetcode-d54e2/
# @File : 636. 函数的独占时间3.py
# @Software: PyCharm
# 官方做法 采用栈 入栈两个元素，一个是id 一个是 时间戳
from typing import *


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk = []
        last = 0
        for log in logs:
            id, tp, t = log.split(':')
            id, t = int(id), int(t)
            if tp[0] == 's':
                if stk:
                    ans[stk[-1]] += t - last
                    last = t
                stk.append(id)
            else:
                i = stk.pop()
                ans[i] += t - last + 1
                last = t + 1
        return ans