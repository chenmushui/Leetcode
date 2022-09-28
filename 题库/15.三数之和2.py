# -*- coding: utf-8 -*-
# @Time : 2022/7/29 13:44
# @Author : mushui
# @Site : 参考https://leetcode.cn/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
# @File : 15.三数之和2.py
# @Software: PyCharm 

from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''''''
        #特殊情况 n<3
        n = len(nums)
        if n<3 :
            return []
        res = []
        nums.sort()
        if nums[0]>0:
            return []

        #遍历排序后数组
        for i in range(n):
            if nums[i]>0: #说明后面都是大于0 不用考虑
                return res
            #重复元素处理
            if i>0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R = n-1
            target = -nums[i]
            while L<R :
                if nums[L]+nums[R] == target:
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L]==nums[L+1]:
                        L +=1
                    while L<R and nums[R]==nums[R-1]:
                        R -=1
                    L +=1
                    R -=1
                elif nums[L]+nums[R] > target:
                    R -=1
                else:
                    L +=1
        return res



if __name__ == '__main__':
    ''''''
    print(Solution().threeSum([0,0]))