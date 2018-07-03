# -*- coding: utf-8 -*-
import math

import os
import random
import time

import key_crypt
from PIL import Image, ImageDraw 


def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def crypt_text(text, key, list_cr, step):
    import unicode_list
    length = len(text)
    sqrt = math.sqrt(length)
    width = 0
    height = 0
    if sqrt.is_integer():
        width = int(sqrt)
        height = int(sqrt)
    else:
        width = int(math.ceil(sqrt))
        height = int(math.ceil(sqrt))
        
    colour = (0, 0, 0)
    image = Image.new("RGB", (width, height), colour)
    draw = ImageDraw.Draw(image)
    obj = image.load()
    l = 0
    i = 0
    time_time = time.time()
    while i < height:
        j = 0
        while j < width:
            if l < length:
                obj[j, i] = hex_to_rgb(
                    unicode_list.color_let[text[l]][random.randint(0, list_cr - 1)])
                l += 1
            else:
                break
            j += 1
        i += 1

    key_crypt.encrypt(key, width, height, obj, step)

    image.save("result/crypt.png")
    del draw
