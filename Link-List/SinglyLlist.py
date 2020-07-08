#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian
from PublicAttribute import PLlist, LNode


class SList(PLlist):

    def _add(self, elem):
        node = LNode(elem)
        if self.head is None:
            self.head = node
            return "SUCCESS, Add Complete!"
        i = self.head
        while i._next is not None:
            i = i._next
        i._next = node
        return "SUCCESS, Add Complete!"

    def _delete(self, elem):
        if self.head is None:
            return "ERROR, Empty SLlist!"
        i = self.head
        if self.head.elem == elem:
            self.head = None
            return "SUCCESS, Delete Complete!"
        while i._next.elem != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        i._next = i._next._next
        return "SUCCESS, Delete Complete!"

    def _modify(self, elem, newelem):
        if self.head is None:
            return "ERROR, Empty SLlist!"
        i = self.head
        if self.head.elem == elem:
            self.head.elem = newelem
            return "SUCCESS, Modify Complete!"
        while i._next.elem != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        i._next.elem = newelem
        return "SUCCESS, Modify Complete!"

    def _query(self, elem):
        if self.head is None:
            return "ERROR, Empty SLlist!"
        if self.head.elem == elem:
            return "SUCCESS，There Are Nodes That Contain Elements!"
        i = self.head
        while i._next.elem != elem or i._next is not None:
            i = i._next
        if i._next is None:
            return "ERROR, No Such Element!"
        return "SUCCESS，There Are Nodes That Contain Elements!"
