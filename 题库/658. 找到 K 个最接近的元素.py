# -*- coding: utf-8 -*-
# @Time : 2022/8/25 14:21
# @Author : mushui
# @Site : 
# @File : 658. 找到 K 个最接近的元素.py
# @Software: PyCharm


from typing import *
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()
        n = len(arr)
        pos = bisect.bisect_left(arr, x)
        i = pos
        j = pos - 1
        ans = []
        while k != 0 and i != n and j != -1:
            if abs(arr[i] - x) > abs(arr[j] - x) or (abs(arr[i] - x) == abs(arr[j] - x)):
                ans.append(arr[j])
                j -= 1
                k -= 1
            else:
                ans.append(arr[i])
                i += 1
                k -= 1
        if k == 0:
            ans.sort()
            return ans
        elif i == n:
            while k:
                ans.append(arr[j])
                j -= 1
                k -= 1
            ans.sort()
            return ans
        else:
            while k:
                ans.append(arr[i])
                i += 1
                k -= 1
            ans.sort()
            return ans

if __name__ == '__main__':
    print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 18))