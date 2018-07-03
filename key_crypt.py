# -*- coding: utf-8 -*-
import math
import re
from hashlib import md5
from itertools import groupby


def caesar_cipher(color_sequence, step):
    mass_sequence = list(map(chr, list(range(ord('a'), ord('g'))))) + list(map(chr, list(range(ord('0'), ord('9') + 1))))
    sequence = ''.join(mass_sequence)
    return color_sequence.translate(str.maketrans(sequence, sequence[step:] + sequence[:step]))


def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def encrypt(key, width, height, obj, step):
    md5_key = list(make_md5(key))

#     for s in range(len(md5_key)):
#         if s+1 < len(md5_key):
#             if md5_key[s] == md5_key[s+1]:
#                 del md5_key[s]
    distortion = 0
    is_apply = 0
    for a in md5_key:
        l = int(a) if a.isdigit() else a
        if str(l).isdigit():
            for i in range(height):
                for j in range(width):
                    if l == 0:
                        is_apply += 1
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (int(math.fabs(r-distortion)), int(math.fabs(g-distortion)), int(math.fabs(b-distortion)))
                        continue

                    if j == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - b, 255 - r, 255 - g)
                        continue

                    if j % 2 == 0 and l % 2 == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - r, 255 - g, 255 - b)
                        continue

                    if j % 2 == 0 and l % 3 == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - g, 255 - b, 255 - r)
                        continue

                    if j % 3 == 0 and l % 2 == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - b, 255 - g, 255 - r)
                        continue

                    if j % 3 == 0 and l % 3 == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - g, 255 - r, 255 - b)
                        continue

                    if j % j == 0 and l % l == 0:
                        r = obj[j, i][0]
                        g = obj[j, i][1]
                        b = obj[j, i][2]
                        obj[j, i] = (255 - r, 255 - b, 255 - g)
                        continue
        else:
            if l == "a":
                i = 0
                while i < height:
                    j = 0
                    while j < width:
                        if j + 1 < width:
                            obj[j, i], obj[j + 1, i] = obj[j + 1, i], obj[j, i]
                        j += 2
                    i += 1
            if l == "b":
                i = 0
                while i < height:
                    j = 0
                    while j < width:
                        if j < width/2:
                            obj[j, i], obj[width - 1 - j,
                                           i] = obj[width - 1 - j, i], obj[j, i]
                        j += 2
                    i += 1
            if l == "c":
                i = 0
                while i < height:
                    j = 0
                    while j < width:
                        if i + 1 < height:
                            obj[j, i], obj[j, i + 1] = obj[j, i + 1], obj[j, i]
                        j += 1
                    i += 2
            if l == "d":
                i = 0
                while i < height:
                    j = 0
                    while j < width:
                        if i < height / 2:
                            obj[j, i], obj[j, height - 1 -
                                           i] = obj[j, height - 1 - i], obj[j, i]
                        j += 1
                    i += 2
            if l == "e":
                for i in range(height):
                    for j in range(width):
                        color_sequence = '%02x%02x%02x' % obj[j, i]
                        obj[j, i] = hex_to_rgb(caesar_cipher(color_sequence, step))
            if l == "f":
                i = 0
                while i < height:
                    j = i
                    while j < width:
                        obj[j, i], obj[i, j] = obj[i, j], obj[j, i]
                        j += 1
                    i += 1

        if is_apply > 0:
            distortion += 1
            is_apply = 0
