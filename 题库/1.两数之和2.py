# -*- coding: utf-8 -*-
# @Time : 2022/7/30 16:55
# @Author : mushui
# @Site : 
# @File : 1.两数之和2.py
# @Software: PyCharm
#暴力
from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i  in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15],9))