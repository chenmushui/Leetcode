# -*- coding: utf-8 -*-
# @Time : 2022/8/6 19:43
# @Author : mushui
# @Site : 
# @File : 1408. 数组中的字符串匹配.py
# @Software: PyCharm 

from typing import *


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        # words.sort()
        n = len(words)
        for i in range(n):
            for word in words:
                if words[i] == word:
                    continue
                if words[i] in word:
                    res.append(words[i])
                    break
        return res
if __name__ == '__main__':
    print(Solution().stringMatching(["mass","as","hero","superhero"]))