#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


class LCQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.head = 0
        self.tail = 0

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item

    def __repr__(self):
        for i in self:
            print(i)

    def enqueue(self, val: int) -> bool:
        pass
    