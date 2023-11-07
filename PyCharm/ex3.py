#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ =='__main__':
    s = "иинформаця"
    for i in range(0, len(s), 2):
        j = 1
    p1 = s[i:i + j]
    p2 = s[j:j + i]
    s = p1 + p2 + p1
    print(s)