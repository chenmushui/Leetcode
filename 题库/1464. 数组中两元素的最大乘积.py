# -*- coding: utf-8 -*-
# @Time : 2022/8/26 13:40
# @Author : mushui
# @Site : 
# @File : 1464. 数组中两元素的最大乘积.py
# @Software: PyCharm 

# from collections import
from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]-1)*(nums[1]-1)