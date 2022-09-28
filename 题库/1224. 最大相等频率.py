# -*- coding: utf-8 -*-
# @Time : 2022/8/18 12:32
# @Author : mushui
# @Site : https://leetcode.cn/problems/maximum-equal-frequency/solution/zui-da-xiang-deng-pin-lu-by-leetcode-sol-5y2m/
# @File : 1224. 最大相等频率.py
# @Software: PyCharm
# 参考答案的两个哈希表

from collections import Counter #Counter 类 可以当字典使用
from typing import *


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        ans = 0
        fre_max = 0  # 记录出现频率最大
        count = Counter()  # 记录出现次数
        freq = Counter()  # key出现频率，value该频率所对应数字数目
        for i, num in enumerate(nums):
            if num in count:
                freq[count[num]] -= 1
            count[num] += 1
            freq[count[num]] += 1
            fre_max = max(fre_max,count[num])
            if fre_max == 1 or \
                freq[fre_max] * fre_max + freq[fre_max-1] * (fre_max -1) == i+1 and freq[fre_max] ==1 or \
                freq[fre_max] * fre_max == i and freq[1] ==1:
                ans = i+1
        return ans
