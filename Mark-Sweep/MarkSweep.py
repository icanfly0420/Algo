#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: QianTian

RAM = [88]
label_space = [88]


def append(i):
    if len(RAM) < 88:
        RAM.append(i)
    else:
        while label_space:
            one = label_space.pop()
            RAM.remove(one)
        RAM.append(i)


def delete(i):
    label_space.append(i)
