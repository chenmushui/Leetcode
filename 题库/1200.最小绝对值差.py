# -*- coding: utf-8 -*-
# @Time : 2022/7/31 0:48
# @Author : mushui
# @Site : 
# @File : 1200.最小绝对值差.py
# @Software: PyCharm 

from typing import *
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        res = []
        if n<1:
            return res
        minL = 0
        minR = 1
        j = 1
        for i in range(n-1):
            if arr[j]-arr[i]==arr[minR]-arr[minL]:
                res.append([arr[i],arr[j]])
            elif arr[j]-arr[i]<arr[minR]-arr[minL]:
                res = []
                minR,minL = j,i
                res.append([arr[i],arr[j]])
            else:
                j = j+1
                continue
            j = j+1
        return res

if __name__ == '__main__':
    print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))