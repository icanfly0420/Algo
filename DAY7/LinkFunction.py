#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian

from typing import Optional


def revesed(ll) -> object:
    revers_node = None
    head = ll.head
    while head:
        next_node = head.next
        head.next = revers_node
        revers_node = head
        head = next_node
    return revers_node


def is_ring(ll) -> bool:
    slow = ll.head
    fast = ll.head
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


def merge(l1, l2) -> object:
    l1_node = l1.head
    l2_node = l2.head
    fake_head = None
    current = fake_head
    while l1_node and l2_node:
        if l1_node <= l2_node:
            current.next = l1_node
            l1_node = l1_node.next
        else:
            current.next = l2_node
            l2_node = l2_node.next
        current = current.next
    if l1_node:
        current.next = l1_node
    else:
        current.next = l2_node
    return fake_head


def del_tailN(ll, index: int) -> object:
    fast = ll.head
    count = 0
    if fast:
        while fast and count < index:
            fast = fast.next
            count += 1
        if not fast and count < index:
            return None
        if not fast and count == index:
            return None

        slow = ll.head
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow


def get_mid(ll) -> object:
    slow = ll.head
    fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow