# -*- coding: utf-8 -*-
# @Time : 2022/8/4 20:54
# @Author : mushui
# @Site : 
# @File : 1403. 非递增顺序的最小子序列.py
# @Software: PyCharm

from typing import *
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if sum(nums[n-i-1:n]) > sum(nums[0:n-i-1]):
                res.append(nums[n-i-1])
                return res
            res.append(nums[n - i - 1])

if __name__ == '__main__':
    print(Solution().minSubsequence( [6]))