# -*- coding: utf-8 -*-
import math

def create_list(q_color):
    color_step = math.floor(16777215 / (65536 * q_color))
    symb_sequence = tuple(map(chr, list(range(0, 65536))))
    #symb_sequence = symb_sequence[step:] + symb_sequence[:step]
    color_sequence = tuple(range(0x000001, 0xffffff + 1, color_step))
    let_color = []
    i = 0
    while i < len(color_sequence):
        q = 0
        grouped_colors = []
        while q < q_color:
            if i == len(color_sequence):
                break
            grouped_colors.append('{0:06X}'.format(color_sequence[i]))
            q += 1
            i += 1
        let_color.append(grouped_colors)
    color_let = dict(zip(symb_sequence, let_color))
    return color_let

def list_creator(q_color, step, cord):
    if cord == 1:
        list_cr = open("unicode_list.py", "w")
        list_cr.write("color_let = " + str(create_list(q_color)))
        list_cr.close()
    else:
        
        color_let_decrypt = {}
        for k, v in create_list().items():
            for v_v in v:
                color_let_decrypt[v_v] = k

        list_decrypt = open("unicode_list.py", "w")
        list_decrypt.write("color_let = " + str(color_let_decrypt))
        list_decrypt.close()
