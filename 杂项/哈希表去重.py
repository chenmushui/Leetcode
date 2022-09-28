# -*- coding: utf-8 -*-
# @Time : 2022/7/29 12:53
# @Author : mushui
# @Site : 
# @File : 哈希表去重.py
# @Software: PyCharm 


class Solution:
    def process(self):
        T = int(input())
        for c in range(T):
            n = int(input())
            a = list(map(int, input().split()))
            mp = dict()
            for i in range(n):
                mp[a[i]] = i
            print(len(mp))
            for i in range(n):
                if mp[a[i]] == i:
                    print(a[i], end=" ")
            print()


if __name__ == '__main__':
    Solution().process()