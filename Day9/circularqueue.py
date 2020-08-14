#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
from typing import Optional

class LCQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.data = []
        self.head = 0
        self.tail = 0

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        if self.tail >= self.head:
            for item in self.data[self.head:self.tail]:
                yield item

    def __repr__(self):
        for i in self:
            print(i)

    def enqueue(self, val: int) -> bool:
        if (self.tail + 1) % self.capacity == self.head:
            return False

        self.data.append(val)
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self) -> Optional[str]:
        if self.head != self.tail:
            item = self.data[self.head]
            self.head = (self.head + 1) % self.capacity
            return item


