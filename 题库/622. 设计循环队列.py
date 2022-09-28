# -*- coding: utf-8 -*-
# @Time : 2022/8/2 16:39
# @Author : mushui
# @Site : 
# @File : 622. 设计循环队列.py
# @Software: PyCharm 

from typing import *
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.queue = [0]*(k+1)
        self.mod = k+1


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear+1)%self.mod
            return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front+1)%self.mod
        return True


    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]


    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[(self.rear - 1)%self.mod]


    def isEmpty(self) -> bool:
        return self.front ==self.rear


    def isFull(self) -> bool:
        return self.front == (self.rear+1)%self.mod




# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
param_1 = obj.enQueue()
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()