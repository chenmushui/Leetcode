# -*- coding: utf-8 -*-
# @Time : 2022/8/3 21:48
# @Author : mushui
# @Site : https://leetcode.cn/problems/orderly-queue/solution/you-xu-dui-lie-by-leetcode-solution-p6gv/
# @File : 899. 有序队列.py
# @Software: PyCharm 
# 第一次做没考虑可以取前k个值

from typing import *
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        res = s
        temp = s
        if k == 1:
            ls = list(temp)
            for i in range(n):
                a = ls[k-1]
                ls.pop(k-1)
                ls.append(a)
                temp = ''.join(ls)
                if temp<res:
                    res = temp
        else:
            res = ''.join(sorted(s))
        return res

if __name__ == '__main__':
    print(Solution().orderlyQueue('baaca',3))

'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/orderly-queue/solution/you-xu-dui-lie-by-leetcode-solution-p6gv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''