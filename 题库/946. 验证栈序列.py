# -*- coding: utf-8 -*-
# @Time : 2022/8/31 21:26
# @Author : mushui
# @Site : 
# @File : 946. 验证栈序列.py
# @Software: PyCharm 

from typing import *
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st,j = [],0
        for x in pushed:
            st.append(x)
            while st and st[-1]==popped[j]:
                st.pop()
                j +=1
        return len(st)==0