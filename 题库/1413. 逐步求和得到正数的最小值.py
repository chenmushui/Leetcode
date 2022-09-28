# -*- coding: utf-8 -*-
# @Time : 2022/8/9 21:18
# @Author : mushui
# @Site : 
# @File : 1413. 逐步求和得到正数的最小值.py
# @Software: PyCharm 

from typing import *


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # n = len(nums)
        sums = []
        ans = 0
        # for i, num in enumerate(nums):
        for num in nums:
            ans = num+ans
            sums.append(ans)

        m = min(sums)
        if m <1:
            ans = 1-m
        else:
            ans = 1
        return ans

if __name__ == '__main__':
    print(Solution().minStartValue([-3,2,-3,4,2]))