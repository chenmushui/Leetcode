# -*- coding: utf-8 -*-
# @Time : 2022/8/13 17:06
# @Author : mushui
# @Site : https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/
# @File : 768. 最多能完成排序的块 II.py
# @Software: PyCharm
# 速度慢
from math import inf
from typing import *


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        j = 0  # 双指针
        head = arr[0]  # 记录最大值
        n = len(arr)
        ans = []
        # chunk = [arr[0]]
        for i, num in enumerate(arr):
            if head < num:
                head = num
            if i != n - 1:
                m = min(arr[i + 1:])
                if head <= m:
                    ans.append(arr[j:i + 1])
                    # head = num
                    j = i + 1
                else:
                    continue
            else:
                if num == max(arr):
                    # ans.append(arr[j:i])
                    ans.append(num)
                else:
                    ans.append(arr[j:])

                # ans = []
                # chunk = arr[:i + 1]

                # ans.append(chunk)
                # j = i+1
        # ans.append(arr[j:])
        return len(ans)


if __name__ == '__main__':
    print(Solution().maxChunksToSorted([2, 1, 5, 4, 5]))
