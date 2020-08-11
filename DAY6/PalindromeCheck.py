#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


def reversed(head):
    reverse_node = None
    while head:
        next_node = head.next
        head.next = reverse_node
        reverse_node = head
        head = next_node
    return reverse_node


def is_palindrome_str(l):
    slow = l.head
    quick = l.head
    while quick and quick.next:
        slow = slow.next
        quick = quick.next.next

    reverse_node = reversed(slow)
    head = l.head
    while head and reverse_node:
        if head.elem != reverse_node.elem:
            print('No')
        else:
            head = head.next
            reverse_node = reverse_node.next
    print("Yes")