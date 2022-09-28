# -*- coding: utf-8 -*-
# @Time : 2022/8/8 21:55
# @Author : mushui
# @Site : 
# @File : 761. 特殊的二进制序列.py
# @Software: PyCharm
# 看答案做出来了，题目一开始没读懂，通过题目英文提示“山”知道大概意思，是一道递归、字符串的题


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        cnt = left = 0
        subs = []
        for i, ch in enumerate(s):
            if ch == '1':
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:  # 说明得到一个特殊序列，递归看里面还有没有特殊序列，进行排序
                    subs.append('1'+self.makeLargestSpecial(s[left+1:i])+'0') #最重要，将1和0去掉
                    left = i+1 #left为下一个特殊序列的开始坐标
        subs.sort(reverse=True) #从大到小排序
        return ''.join(subs)

