#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


class LNode:
    def __init__(self, value: int):
        self.val = value
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.top = LNode(-1)
        self.tail = LNode(-1)
        self.value = []
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, val: int) -> int:
        node = LNode(val)
        if node in self.value:
            node.next.prev = node.prev
            node.prev.next = node.next
            top_node = self.top.next
            self.top.next = node
            node.prev = self.top
            node.next = top_node
            top_node.prev = node
            return val
        return -1

    def put(self, val: int) -> None:
        node = LNode(val)
        if node in self.value:
            node.next.prev = node.prev
            node.prev.next = node.next
            top_node = self.top.next
            self.top.next = node
            node.prev = self.top
            node.next = top_node
            top_node.prev = node
        else:
            top_node = self.top.next
            self.top.next = node
            node.prev = self.top
            node.next = top_node
            top_node.prev = node
            if len(self.value) > self.capacity:
                self.value.pop(-1)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.top.prev.prev



