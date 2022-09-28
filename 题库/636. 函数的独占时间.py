# -*- coding: utf-8 -*-
# @Time : 2022/8/7 13:57
# @Author : mushui
# @Site : 
# @File : 636. 函数的独占时间.py
# @Software: PyCharm
# 用栈来做 WA
from typing import *


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        last = [0 for i in range(n)]
        res = [0 for i in range(n)]
        stack.append(logs[0])
        i = 1
        # last = 0
        while stack:
            if logs[i].split(':')[0] == stack[-1].split(':')[0] and \
                    logs[i].split(':')[1] != stack[-1].split(':')[1]:
                a = stack.pop()
                res[int(logs[i].split(':')[0])] += int(logs[i].split(':')[-1]) - int(a.split(':')[-1]) + 1 - last[int(logs[i].split(':')[0])]
                last[int(logs[i].split(':')[0])] = int(logs[i].split(':')[-1]) - int(a.split(':')[-1])
            else:
                stack.append(logs[i])
            i = i+1
        return res

if __name__ == '__main__':
    print(Solution().exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))