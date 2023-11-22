#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ =='__main__':
        word = "иинформаця"
        word_list = list(word)
        i_index = word_list.index('и')
        н_index = word_list.index('н')
        ф_index = word_list.index('ф')
        м_index = word_list.index('м')
        а_index = word_list.index('а')
        ц_index = word_list.index('ц')

        word_list[i_index], word_list[н_index] = word_list[н_index], word_list[i_index]
        word_list[ф_index], word_list[м_index] = word_list[м_index], word_list[ф_index]
        word_list[а_index], word_list[ц_index] = word_list[ц_index], word_list[а_index]

        fixed_word = ''.join(word_list)
        print("Исправленное слово:", fixed_word)