#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__=='__main__':
    r=input("введите предложение:")
    m=""
    for i in range(len(r)):
        if i%2==1:
            m+=r[i]
        else:
            m+="ы"
    print("исходное предложение",r)
    print("изменённое предложение",m)