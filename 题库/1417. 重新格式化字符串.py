# -*- coding: utf-8 -*-
# @Time : 2022/8/11 9:05
# @Author : mushui
# @Site : 
# @File : 1417. 重新格式化字符串.py
# @Software: PyCharm
class Solution:
    def reformat(self, s: str) -> str:
        ans = ''
        # n = len(s)
        qs = []  # 字符队列
        qn = []  # 数字队列
        for st in s:
            if str.isdigit(st):
                qn.append(st)
            if str.isalpha(st):
                qs.append(st)
        if abs(len(qs) - len(qn)) > 1:
            return ''
        elif len(qs) - len(qn) == 1:
            j = 0
            i = 0
            while i < len(qs):
                try:
                    qs.insert(i + 1, qn[j])
                except:
                    break
                j += 1
                i += 2
            return ''.join(qs)
        else:
            j = 0
            i = 0
            while i < len(qn):
                try:
                    qn.insert(i + 1, qs[j])
                except:
                    break
                j += 1
                i += 2
            return ''.join(qn)

if __name__ == '__main__':
    print(Solution().reformat("ab123"))
