# -*- coding: utf-8 -*-
# @Time : 2022/7/28 17:43
# @Author : mushui
# @Site : 
# @File : 15.三数之和.py
# @Software: PyCharm 
#超时

from typing import *
from itertools import *
class Solution:

    # @staticmethod
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.ls = nums
        self.ls = list(permutations(self.ls,3))
        # self.ls.sort()
        # print(self.ls)
        self.ls = list(set(self.ls)) #去重

        # print(self.ls)
        self.ls2 = []
        for items in self.ls:
            '''
            这是注释
            '''
            sum  = 0
            for item in items:
                sum += item
            if sum == 0:
                self.ls2.append(list(items))

        # print(self.ls2)
        for i in self.ls2:
            # print(sorted(i))
            self.ans.append(sorted(i))

        # print(self.ans)

        self.ans = list(set([tuple(t) for t in self.ans]))
        self.ans = [list(s) for s in self.ans]  # 去重


        # it = iter(self.ans)
        # print(it)


        # print(self.ans)
        # index = 0
        # for an in self.ans:
        #     print(an)
        #     print(self.ans[index+1])
        #     # print(self.ans[])
        #     boool = True
        #     for i in an:
        #         if i in self.ans[index+1]:
        #             # print(i)
        #             continue
        #         else:
        #             boool = False
        #             break
        #     if boool:
        #         self.ans.remove(self.ans[index+1])
        #         print("shanchu")
        #     else:
        #         index = index+1
        #     print("dangqian",self.ans[index+1])

        return self.ans

if __name__ == '__main__':
    s =  [12,-14,-5,12,-2,9,0,9,-3,-3,-14,-6,-4,13,-11,-8,0,5,-7,-6,-10,-13,-7,-14,-3,0,12,5,-8,7,3,-11,0,6,9,13,-8,-6,7,4,6,0,13,-13,-1,9,-13,6,-1,-13,-15,-4,-11,-15,-11,-7,1,-14,13,8,0,2,4,-15,-15,-2,5,-8,7,-11,11,-10,4,1,-15,10,-5,-13,2,1,11,-6,4,-15,-5,8,-7,3,1,-9,-4,-14,0,-15,8,0,-1,-2,7,13,2,-5,11,13,11,11]
    s2 = [0,1,1]

    solution = Solution()
    ans = solution.threeSum(s)
    ans2 = solution.threeSum(s2)
    print(ans)
    print(ans2)
    print(Solution().threeSum(s)) #不实例化 调用类中函数