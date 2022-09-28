# -*- coding: utf-8 -*-
# @Time : 2022/8/14 19:50
# @Author : mushui
# @Site : 
# @File : 1422. 分割字符串的最大得分.py
# @Software: PyCharm 


class Solution:
    def maxScore(self, s: str) -> int:
        max_points = 0
        count_1 = 0
        for i, num in enumerate(s):
            if num == '1':
                count_1 += 1
        cur_points = count_1
        for i in range(len(s)-1):
            if s[i] == '0':
                cur_points += 1
            else:
                cur_points -= 1
            if max_points < cur_points:
                max_points = cur_points
        return max_points
if __name__ == '__main__':
    print(Solution().maxScore("1111"))