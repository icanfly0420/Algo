#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian

# !/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian


def bubble_sort(a):
    n = len(a)
    if n <= 1:
        return
    i = 0
    while i < n:
        j = 0
        flag = False
        while j < n - i - 1:
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                flag = True
            j += 1
        if not flag:
            break
        i += 1


def insertion_sort(a):
    n = len(a)
    if n <= 1:
        return
    i = 1
    while i < n:
        value = a[i]
        j = i - 1
        while j >= 0:
            if a[j] > value:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = value
        i += 1


def selection_sort(a):
    n = len(a)
    if n <= 1:
        return
    i = 0
    while i < n:
        min = None
        index = None
        j = i
        while j < n:
            if min:
                if min > a[j]:
                    min = a[j]
                    index = j
            else:
                min = a[j]
                index = j
            j += 1
            print(min, 'and', j, 'and', i)
        a[index] = a[i]
        a[i] = min
        i += 1


def climb_stairs(n):
    """recursion"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)


if __name__ == '__main__':
    a = [12, 34, 53, 11, 23, 13, 2, 4, 9, 88]
    selection_sort(a)
    print(a)
