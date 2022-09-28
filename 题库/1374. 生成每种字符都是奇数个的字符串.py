# -*- coding: utf-8 -*-
# @Time : 2022/8/1 10:34
# @Author : mushui
# @Site : 
# @File : 1374. 生成每种字符都是奇数个的字符串.py
# @Software: PyCharm 


from typing import *
class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2 == 1:
            return 'a'*n
        else:
            return 'a'*(n-1)+'b'

if __name__ == '__main__':
    print(Solution().generateTheString(4))