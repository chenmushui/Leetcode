# -*- coding: utf-8 -*-
# @Time : 2022/7/30 16:07
# @Author : mushui
# @Site : 
# @File : 1.两数之和.py
# @Software: PyCharm
#wa 3 3，6不通过   算法来自三数之和
from  typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = dict() #哈希表存坐标 但是存在哈希碰撞
        n = len(nums)
        for i in range(n):
            hashh[nums[i]] = i
        nums.sort()
        res = []
        for i in range(n):
            if nums[i]>target:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            #右指针
            r = n-1
            while i<r:
                if nums[i]+nums[r] == target:
                    res.append(hashh[nums[i]])
                    res.append(hashh[nums[r]])
                    r = r-1
                elif nums[i]+nums[r] > target:
                    r = r-1
                else:
                    break
        return res

if __name__ == '__main__':

    ls = Solution().twoSum([2,7,11,15],9)
    print(ls)
