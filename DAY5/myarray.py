#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


class Myarray:
    def __init__(self, capacity: int):
        self.data = []
        self.capacity = capacity

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, position: int) -> object:
        return self.data[position]

    def __setitem__(self, position: int, val: object) -> None:
        self.data[position] = val

    def __iter__(self):
        for i in self.data:
            yield i

    def find(self, index: int) -> object:
        try:
            return self.data[index]
        except IndexError:
            return None

    def insert(self, index: int, value: object) -> object:
        if len(self.data) >= self.capacity:
            return False
        else:
            return self.data.insert(index, value)

    def delete(self, index: int) -> bool:
        try:
            return self.data.pop(index)
        except IndexError:
            return False

    def print_all(self):
        for item in self:
            print(item)
