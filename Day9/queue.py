#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


class LQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []
        self.head = 0
        self.tail = 0

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item

    def __repr__(self):
        for item in self:
            print(item)

    def enqueue(self, val: int) -> bool:
        if len(self) == self.capacity:
            return False
        else:
            self.data.append(val)
            return True

    def dequeue(self) -> object:
        try:
            return self.data.pop(0)
        except IndexError:
            return False


class Node:
    def __init__(self, elem: object, _next=None):
        self.val = elem
        self._next = _next


class LLQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.tail = None

    def __len__(self):
        count = 0
        top = self.head
        while top:
            count += 1
            top = top._next
        return count

    def __iter__(self):
        top = self.head
        while top:
            yield top
            top = top._next

    def __repr__(self):
        for item in self:
            print(item)

    def enqueue(self, val: object) -> bool:
        if len(self) == self.capacity:
            return False
        else:
            new = Node(val)
            self.tail.next = new
            self.tail = new

    def dequeue(self) -> object:
        if len(self) == 0:
            return False
        else:
            elem = self.head
            self.head = self.head._next
            return elem