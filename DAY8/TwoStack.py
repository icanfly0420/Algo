#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian

from typing import Optional


class LStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []

    def __iter__(self):
        for item in self.data:
            yield item

    def __len__(self):
        return len(self.data)

    def push(self, val: object) -> object:
        if len(self) >= self.capacity:
            return False
        else:
            return self.data.append(val)

    def pop(self) -> bool:
        try:
            return self.data.pop(-1)
        except IndexError:
            return False

    def print_all(self):
        for i in self:
            print(i)
            print('->')


class DLNode:
    def __init__(self,elem: object):
        self.elem = elem
        self.next = None
        self.prev = None


class LLStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = DLNode(-1)
        self.tail = DLNode(-1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def __iter__(self):
        head = self.top.next
        while head.next:
            yield head
            head = head.next

    def __len__(self):
        head = self.top.next
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def push(self,elem: object) -> bool:
        if len(self) >= self.capacity:
            return False
        else:
            new_node = DLNode(elem)
            current = self.tail.prev
            current.next = new_node
            new_node.prev = current
            new_node.next = self.tail
            return True

    def pop(self) -> Optional[DLNode]:
        current = self.tail.prev
        if current.prev:
            current.prev.next = current.next
            current.next.prev = current.prev
            return current
        else:
            return None

    def print_all(self):
        for i in self:
            print(i)
            print("->")