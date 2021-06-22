from PIL import Image, ImageGrab
from pyautogui import press
import time

import os

# book_length = 160  # How many pages is your book   # ***
book_length = 160 #3  # DEBUG PURPOSE
# cover_location = "Cover.png"  # Specify the name of the cover picture (make sure it is a .png)
cover_location = os.getcwd()+"/Cover.png" #"/Users/zrhun/vitalsource-printer/Pirate_Activist/Cover.png"   # DEBUG PURPOSE
print(cover_location)

# IMPORTANT: Manually specify the dimensions for your screenshot   # ***
"""
X1 = 488
Y1 = 87
X2 = 950
Y2 = 800
"""
X1 = 396*2 #396, 294, 471, 379
Y1 = 128*2 #128, 280, 431, 128
X2 = 886*1.91 #886, 456, 416
Y2 = 761*2 #761, 634, 575

# Replace the X1, Y1 values with the coordinates of the top left of the ebook and the X2, Y2 with the coordinates of the bottom right.


# You have 5 seconds to switch to the textbook. Make sure you start on the cover page
time.sleep(5)

box = (X1, Y1, X2, Y2)
im_list = []
cover = Image.open(cover_location).convert("RGB")

for i in range(0, book_length):
    # press("down")  # Assuming the down arrow key switches between pages
    press("right")  # DEBUG PURPOSE
    # Change to press("right") if right arrow key works instead, and so on.

    time.sleep(1)  # arbitrary delay between screenshots
    im = ImageGrab.grab(bbox=box).convert('RGB')
    im_list.append(im)

cover.save("Textbook.pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list)


# Reference: https://www.reddit.com/r/Piracy/comments/cym1x4/a_quickanddirty_python_script_to_convert_any/