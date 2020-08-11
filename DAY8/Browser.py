#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
import sys

sys.path.append("TwoStack")
from TwoStack import LLStack


class Browser:
    def __init__(self):
        self.up = LLStack(10)
        self.down = LLStack(10)

    def push_up(self, elem: str) -> bool:
        return self.up.push(elem)

    def push_down(self, elem: str) -> bool:
        return self.down.push(elem)

    def up(self) -> object:
        if self.up:
            return self.up.pop()
        else:
            return None

    def down(self) -> object:
        if self.down:
            return self.down.pop()
        else:
            return None
