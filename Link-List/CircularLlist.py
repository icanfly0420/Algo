#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
from PublicAttribute import PLlist, LNode


class CLlist(PLlist):
    def __init__(self):
        super(CLlist, self).__init__()

    def _add(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            node._next = node
            return "SUCCESS, Add Complete!"
        i = self.head
        while i._next != self.head:
            i = i._next
        i._next = node
        node._next = self.head
        return "SUCCESS, Add Complete!"

    def _delete(self, elem):
        if self.head is None:
            return "ERROR, Empty CLlist!"
        i = self.head
        while i._next.elem != elem or i._next != self.head._next._next:
            i = i._next
        if i._next == self.head._next._next:
            return "ERROR, No Such Element!"
        i._next = i._next._next
        return "SUCCESS, Delete Complete!"

    def _modify(self, elem, newelem):
        if self.head is None:
            return "ERROR, Empty CLlist!"
        i = self.head
        while i._next.elem != elem or i._next != self.head._next._next:
            i = i._next
        if i._next == self.head._next._next:
            return "ERROR, No Such Element!"
        i._next.elem = newelem
        return "SUCCESS, Modify Complete!"

    def _query(self, elem):
        if self.head is None:
            return "ERROR, No Such Element!"
        i = self.head
        while i._next.elem != elem or i._next != self.head._next._next:
            i = i._next
        if i._next == self.head._next._next:
            return "ERROR, No Such Element!"
        return "SUCCESS，There Are Nodes That Contain Elements!"
