# -*- coding: utf-8 -*-
# @Time : 2022/8/7 15:47
# @Author : mushui
# @Site : 
# @File : 636. 函数的独占时间2.py
# @Software: PyCharm 


# 分情况讨论 WA
from typing import *


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for i in range(n)]
        l = len(logs)
        # last = logs[0]
        for i in range(1, l):
            # if logs[i].split(':')[0] == logs[i - 1].split(':')[0]:
                if logs[i].split(':')[1] == logs[i - 1].split(':')[1] == 'start':
                    res[int(logs[i-1].split(':')[0])] += int(logs[i].split(':')[-1]) - int(logs[i - 1].split(':')[-1])
                elif logs[i].split(':')[1] == logs[i - 1].split(':')[1] == 'end':
                    res[int(logs[i].split(':')[0])] += int(logs[i].split(':')[-1]) - int(logs[i - 1].split(':')[-1])
                elif logs[i].split(':')[1] == 'end' and logs[i - 1].split(':')[1] == 'start':
                    res[int(logs[i].split(':')[0])] += int(logs[i].split(':')[-1]) - int(logs[i - 1].split(':')[-1]) + 1
                elif logs[i].split(':')[1] == 'start' and logs[i - 1].split(':')[1] == 'end':
                    res[int(logs[i-1].split(':')[0])] += int(logs[i].split(':')[-1]) - int(logs[i - 1].split(':')[-1]) -1
                else:
                    continue

        return res

if __name__ == '__main__':
    print(Solution().exclusiveTime(8,["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]))