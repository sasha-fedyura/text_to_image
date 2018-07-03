# -*- coding: utf-8 -*-
import math
import time
import key_decrypt
from PIL import Image

import main

def decrypt_text(path, key, step):
    import unicode_list
    image = Image.open(path)
    text = ""
    obj = image.load()
    width = image.size[0]
    height = image.size[1]
    key_decrypt.decrypt(key, width, height, obj, step)
    i = 0
    while i < height:
        j = 0
        while j < width:
            hex_color = '%02x%02x%02x' % obj[j, i]
            if obj[j, i] != (0, 0, 0) and hex_color.upper() in unicode_list.color_let:
                text += unicode_list.color_let[hex_color.upper()]
            j += 1
        i += 1
    f = open("result/decrypt.txt", "w+")
    f.write(text)
    f.close()
