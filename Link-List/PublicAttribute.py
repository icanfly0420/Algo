#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


class PNode:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = _next


class PLlist:
    def __init__(self):
        self.head = None
