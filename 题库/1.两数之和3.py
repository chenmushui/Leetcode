# -*- coding: utf-8 -*-
# @Time : 2022/7/30 17:07
# @Author : mushui
# @Site : 
# @File : 1.两数之和3.py
# @Software: PyCharm
# 哈希表 参考力扣官方
from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        n = len(nums)
        for i,num in enumerate(nums):
            if target-num in hashtable:  #判断哈希表的键key是否已经存在
                return [hashtable[target-num],i]
            hashtable[num] = i
        return []

if __name__ == '__main__':
    print(Solution().twoSum([3,3,3,1],4))