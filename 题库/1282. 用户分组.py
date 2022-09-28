# -*- coding: utf-8 -*-
# @Time : 2022/8/12 9:31
# @Author : mushui
# @Site : 
# @File : 1282. 用户分组.py
# @Software: PyCharm

from typing import *
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []

        dic = {}
        for i,member in enumerate(groupSizes):
            if member not in dic:
                dic[member] = [i]
            else:
                if (len(dic[member]) == member):
                    ans.append(dic[member])
                    dic[member] = [i]
                else:
                    dic[member].append(i)
        for key,value in dict.items(dic):
            ans.append(value)
        return ans

if __name__ == '__main__':
    print(Solution().groupThePeople([2,1,3,3,3,2]))