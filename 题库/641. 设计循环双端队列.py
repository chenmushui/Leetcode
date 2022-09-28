# -*- coding: utf-8 -*-
# @Time : 2022/8/15 11:39
# @Author : mushui
# @Site : 
# @File : 641. 设计循环双端队列.py
# @Software: PyCharm
class MyCircularDeque:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)
        self.l = len(self.elements)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % (self.l)
        self.elements[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % (self.l)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.l
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.l
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % self.l]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % self.l == self.front

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
