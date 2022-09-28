# -*- coding: utf-8 -*-
# @Time : 2022/8/29 15:22
# @Author : mushui
# @Site : 
# @File : 1470. 重新排列数组.py
# @Software: PyCharm 


from typing import *
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res