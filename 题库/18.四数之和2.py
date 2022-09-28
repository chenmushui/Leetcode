# -*- coding: utf-8 -*-
# @Time : 2022/7/30 19:29
# @Author : mushui
# @Site : https://leetcode.cn/problems/4sum/solution/dai-ma-sui-xiang-lu-by-carlsun-2-bf7k/
# @File : 18.四数之和2.py
# @Software: PyCharm 
# 剪枝 去重 双指针 相当于15三数之和拓展

from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for k in range(n):
            if nums[k]>target and nums[k]>=0: #剪枝
                break
            #去重
            if k>0 and nums[k]==nums[k-1]:
                continue
            for i in range(k+1,n):
                if nums[k]+nums[i] > target and nums[k]+nums[i] >= 0:
                    # 二次剪枝
                    break
                # 二次去重
                if i > k+1 and nums[i] == nums[i - 1]:
                    continue
                L = i+1
                R = n-1

                while L<R :
                    if nums[L]+nums[R]+nums[k]+nums[i] == target:
                        res.append([nums[k],nums[i],nums[L],nums[R]])
                        while L<R and nums[L]==nums[L+1]:
                            L +=1
                        while L<R and nums[R]==nums[R-1]:
                            R -=1
                        L +=1
                        R -=1
                    elif nums[L]+nums[R]+nums[k]+nums[i] > target:
                        R -=1
                    else:
                        L +=1
        return res


if __name__ == '__main__':
    print(Solution().fourSum([1,0,-1,0,-2,2],0))