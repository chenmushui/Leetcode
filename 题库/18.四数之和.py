# -*- coding: utf-8 -*-
# @Time : 2022/7/30 17:30
# @Author : mushui
# @Site : 
# @File : 18.四数之和.py
# @Software: PyCharm 

from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            part = [nums[i],nums[j],nums[k],nums[l]]
                            part.sort()
                            # if part not in res:
                            res.append(part)


        return res

if __name__ == '__main__':
    print(Solution().fourSum([2,2,2,2,2],8))