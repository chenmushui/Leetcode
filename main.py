#
#
# # qn = [1,2,3]
# # # print(ls1)
# # qs = ['a','b','c','d','e']
# # j = 0
# # i = 0
# # while i<len(qs):
# #     try:
# #         qs.insert(i + 1, qn[j])
# #     except:
# #         break
# #     j += 1
# #     i+=2
# # print(qs)
# # # ls = [ls1]
# # print(abs(len(qn) - len(qs)))
#
# # ls = [1]
# # print(max(ls))
# #
# # ls = ['' for i in range(4)]
# # ls[0] = 1
# # print(ls)
# # def b():
# #     s = []
# #     def a():
# #         s.append()
# #         print(s)
# #     a()
# # # b()
# # for i   in  range(5):
# #     j =1
# #     pass
# # print(i,j)
# startTime = [1,2,5,7]
# print(max(startTime))
# endTime = [3,4]
# queryTime = 2
# # print(list(zip(ls, ls2)))
# # l = list(zip(ls, ls2))
# # for i,j in l:
# #     print(i,j)
# # print([s <= queryTime <= e for s, e in zip(startTime, endTime)])
# import bisect
#
# print(bisect.bisect_left(startTime, 1))
#
# # a = []
# # print(a[-1])
#
#
# a = [0]*5
# a[2] =1
# print(a)
#
# h = 4
# res = [['']*(2**h - 1) for i in range(h)]
# print(res)
#

# a = [1,2,3]
# for i in a:
#     a.append(i)
# print(a)
#
# a = [1,2,3]
# x,y,z = a
# print(x,y,z)
# a= 0b1000
# print(bin(0b1000^0))

# # print(a.bit_count())
# from collections import Counter
# a = [1,3,2,3]
# b = [2,1,3,3]
#
# c = Counter(a)
# d = Counter(b)
# # a.sort()
# print(c==d)
#
# import bisect
# l = [1,3,5,7]
# a= bisect.bisect_right(l,8)
# print(a)
#
# import heapq
# arr = [3,1,5,7,2,6,9,3,5]
# print("原数组：{0}".format(arr))
# # 将给定的列表转化为最小堆，线性时间
# heapq.heapify(arr)
# heapq.nlargest()
# print("最小堆数组：{0}".format(arr))

# for i in range(5):
#     j = i
# print(j)

from collections import deque
q = deque([('a',1)])
q.append(('b',2))
print(q[0][0])
#
# l = [1,2]
# a,b=l
# print(a,b)