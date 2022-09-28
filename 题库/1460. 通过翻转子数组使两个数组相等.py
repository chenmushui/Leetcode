# -*- coding: utf-8 -*-
# @Time : 2022/8/24 13:11
# @Author : mushui
# @Site : 
# @File : 1460. 通过翻转子数组使两个数组相等.py
# @Software: PyCharm 

from typing import *
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return True
        return False