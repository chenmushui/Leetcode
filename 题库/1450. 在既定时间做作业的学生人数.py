# -*- coding: utf-8 -*-
# @Time : 2022/8/19 12:49
# @Author : mushui
# @Site : 
# @File : 1450. 在既定时间做作业的学生人数.py
# @Software: PyCharm 

from typing import *


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        l = list(zip(startTime, endTime))
        for st, ed in l:
            if queryTime >= st and queryTime <= ed:
                ans += 1
        return ans
