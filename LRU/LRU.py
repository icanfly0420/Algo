#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian

class LNode:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = _next


class LList:
    def __init__(self):
        self.head = None
        self.len = 0

    def _add(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            self.len += 1
            return
        node._next = self.head
        self.head = node
        self.len += 1

    def _put(self):
        if self.head is None:
            return "ERROR, Empty LList!"
        if self.head._next is None:
            self.head = None
            self.len -= 1
            return
        i = self.head
        while i._next._next is not None:
            i = i._next
        i._next = None
        self.len -= 1
        return

    def _delete(self, elem):
        if self.head is None:
            return "ERROR, Empty SLlist!"
        i = self.head
        if self.head.elem == elem:
            self.head = None
            return
        while i._next.elem != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        i._next = i._next._next
        return

    def _query(self, elem):
        if self.head is None:
            return False
        if self.head.elem == elem:
            return True
        i = self.head
        while i._next.elem != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return False
        return True


class LRU:
    def __init__(self, maxsize):
        self.cache = LList()
        self.maxsize = maxsize

    def run(self, elem):
        if self.cache.len < self.maxsize:
            if self.cache._query(elem):
                self.cache._delete(elem)
                self.cache._add(elem)
            else:
                self.cache._add(elem)

        else:
            if self.cache._query(elem):
                self.cache._delete(elem)
                self.cache._add(elem)
            else:
                self.cache._put()
                self.cache._add(elem)
