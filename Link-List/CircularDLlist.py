#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
from PublicAttribute import PLlist, LNode


class CDLNode(LNode):
    def __init__(self, _prev=None):
        super(CDLNode, self).__init__()
        self._prev = _prev


class CDLlist(PLlist):
    def __init__(self):
        super(CDLlist, self).__init__()
        self.tail = None

    def _add(self, elem):
        node = CDLNode(elem)
        if self.head is None:
            self.head = self.tail = node
            node._next = node
            node._prev = node
            return "SUCCESS, Add Complete!"
        node._prev = self.tail
        node._next = self.head
        self.tail._next = node
        self.head._prev = node
        self.head = node
        return "SUCCESS, Add Complete!"

    def _delete(self, elem):
        if self.head is None:
            return "ERROR, Empty CDLlist!"
        i = self.head
        while i.elem != elem or i._next != self.head._next:
            i = i._next
        if i._next == self.head._next:
            return "ERROR, No Such Element!"
        i._prev._next = i._next
        i._next._prev = i._prev
        return "SUCCESS, Delete Complete!"

    def _modify(self, elem, newelem):
        if self.head is None:
            return "ERROR, Empty CDLlist!"
        i = self.head
        while i.elem != elem or i._next != self.head._next:
            i = i._next
        if i._next == self.head._next:
            return "ERROR, No Such Element!"
        i.elem = newelem
        return "SUCCESS, Modify Complete!"

    def _query(self, elem):
        if self.head is None:
            return "ERROR, Empty CDLlist!"
        i = self.head
        while i.elem != elem or i._next != self.head._next:
            i = i._next
        if i._next == self.head._next:
            return "ERROR, No Such Element!"
        return "SUCCESS，There Are Nodes That Contain Elements!"
