#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
from PublicAttribute import PLlist, LNode


class DLNode(LNode):
    def __init__(self, _prev):
        super(DLNode, self).__init__()
        self._prev = _prev


class DLlist(PLlist):
    def __init__(self):
        PLlist.__init__()
        self.tail = None

    def _add(self, elem):
        node = DLNode(elem)
        if self.head is None:
            self.head = self.tail = node
        else:
            node._next = self.head
            self.head._prev = node
            self.head = node
        return "SUCCESS, Add Complete!"

    def _delete(self, elem):
        if self.head is None:
            return "ERROR, Empty DLlist!"
        i = self.head
        while i._next != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        i._next = i._next._next
        i._next._prev = i
        return "SUCCESS, Delete Complete!"

    def _modify(self, elem, newelem):
        if self.head is None:
            return "ERROR, Empty DLlist!"
        if self.head.elem == elem:
            self.head.elem = newelem
            return "SUCCESS, Modify Complete!"
        i = self.head
        while i._next != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        i._next.elem = newelem
        return "SUCCESS, Modify Complete!"

    def _query(self, elem):
        if self.head is None:
            return "ERROR, Empty DLlist!"
        if self.head.elem == elem:
            return "SUCCESS，There Are Nodes That Contain Elements!"
        i = self.head
        while i._next != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        return "SUCCESS，There Are Nodes That Contain Elements!"
