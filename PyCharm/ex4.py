#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ =='__main__':
    sentence = input("Введите предложение: ")
    words = sentence.split()
    for word in words:
        if word != "привет":
            print(word)
