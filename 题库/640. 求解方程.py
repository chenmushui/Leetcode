# -*- coding: utf-8 -*-
# @Time : 2022/8/10 20:13
# @Author : mushui
# @Site : 
# @File : 640. 求解方程.py
# @Software: PyCharm 


class Solution:
    def solveEquation(self, equation: str) -> str:
        left = equation.split('=')[0]
        right = equation.split('=')[1]
        xl, xr = 0, 0
        nl = nr = 0
        # xs = [] #x的栈
        # ns = [] #常数栈
        # ind = 1  # 数字系数
        pre_num = ''  # 数字和
        fuhao = '+'
        for i, s in enumerate(left):  # 求等式左边x系数和and常数和
            if s == '+' or s == '-':
                if str.isdigit(left[i - 1])and i != 0:  # 符号前是数字
                    nl += int(fuhao + pre_num)
                    pre_num = ''
                fuhao = s
                continue
            if str.isdigit(s):
                pre_num += s
                # ind *=10
                if i == len(left) - 1:  # 数字是最后一位
                    nl += int(fuhao + pre_num)
                    pre_num = ''
                continue
            if s == 'x':
                if str.isdigit(left[i - 1]) and i != 0:  # x 前有数字且x不是第一项
                    xl += int(fuhao + pre_num)
                    pre_num = ''
                # if not str.isalnum(): #x前没数字
                else:
                    xl += int(fuhao+'1')
        fuhao = '+'
        pre_num = ''  # 数字和
        for i, s in enumerate(right):  # 求等式右边x系数和and常数和
            if s == '+' or s == '-':
                if str.isdigit(right[i - 1]) and i != 0:  # 符号前是数字且符号不是第一位
                    nr += int(fuhao + pre_num)
                    pre_num = ''
                fuhao = s
                continue
            if str.isdigit(s):
                pre_num += s
                if i == len(right) - 1:  # 数字是最后一位
                    nr += int(fuhao + pre_num)
                    pre_num = ''
                # ind *=10
                continue
            if s == 'x':
                if str.isdigit(right[i - 1]) and i != 0:  # x 前有数字且x不是第一项
                    xr += int(fuhao + pre_num)
                    pre_num = ''
                # if not str.isalnum(): #x前没数字
                else:
                    xr += int(fuhao+'1')
        if xl - xr == 0 and nr - nl != 0:
            return "No solution"

        if xl - xr == 0 and nr - nl == 0:
            return "Infinite solutions"

        else:
            ans = (nr - nl) // (xl - xr)

        return f'x={ans}'
        # return [xl, nl,xr,nr]


if __name__ == '__main__':
    print(Solution().solveEquation("-1=-x"))
