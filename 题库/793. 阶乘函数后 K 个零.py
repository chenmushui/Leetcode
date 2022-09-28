# -*- coding: utf-8 -*-
# @Time : 2022/8/28 15:38
# @Author : mushui
# @Site : https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/solution/by-insist-just-do-it-m75v/
# @File : 793. 阶乘函数后 K 个零.py
# @Software: PyCharm
# 没做出， 二分

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        if k == 0: return 5
        L, R = 4 * k, 5 * k
        while L <= R:
            M = L + (R - L) // 2
            s = 0
            tmp = M
            while tmp:
                tmp //= 5
                s += tmp
            if s == k:
                return 5
            if s < k:
                L = M + 1
            else:
                R = M - 1
        return 0

if __name__ == '__main__':
    print(Solution().preimageSizeFZF(5))

# 作者：insist-just-do-it
# 链接：https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/solution/by-insist-just-do-it-m75v/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。