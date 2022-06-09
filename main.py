import sys
import time
from traceback import print_tb

import numpy as np
from sympy import hermite
def clear():
    import os
    os.system('cls')
dw = 25
dh = 8
width = dw + 120 + 10
height = dh + 25 + 10
from PIL import Image, ImageDraw, ImageFont
img = Image.new("L", size = (width, height), color = 255)
draw = ImageDraw.Draw(img)

text = "毕业快乐！"
coordinates = (dw, dh)
color = 0

font = ImageFont.truetype('simhei', 25)
draw.text(coordinates, text, color, font = font)

img_array = np.array(img)
# img.show()

# 从上往下
clear()
for i in range(height):
    for j in range(width):
        if img_array[i][j] != 255:   
            print('/', end='')  # / ? \ @ # *< > 
        else:   print(' ', end='')
        sys.stdout.flush()
    time.sleep(0.1)
    print()

# 从左往右
# img_list = img_array.tolist()
# # clear()
# for now_w in range(width):
#     clear()
#     # sys.stdout.flush()    
#     # file = open('text.txt', "w+")
#     for i in range(height):
#         for j in range(now_w):
#             if img_list[i][j] != 255: 
#                 # file.write('@')  
#                 print('/', end='')
#             else:   
#                 print(' ', end='')
#                 # file.write(' ')  
#             # sys.stdout.flush()
#         # file.write('\n')  
#         print()
#     # time.sleep(0.1)
#     # print('\n' * 2)
#     # file.close()
