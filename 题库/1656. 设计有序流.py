# -*- coding: utf-8 -*-
# @Time : 2022/8/16 13:24
# @Author : mushui
# @Site : 
# @File : 1656. 设计有序流.py
# @Software: PyCharm 

from typing import *


class OrderedStream:

    def __init__(self, n: int):
        self.ls = ['' for i in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        if self.ls[self.ptr] == '' and self.ptr != idKey -1:
            self.ls[idKey - 1] = value
            # self.ptr += 1
            return []
        else:
            self.ls[idKey - 1] = value
            ans = []
            while self.ptr < len(self.ls) and self.ls[self.ptr] != '':
                ans.append(self.ls[self.ptr])
                self.ptr += 1
            return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
