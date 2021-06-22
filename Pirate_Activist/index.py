from PIL import Image, ImageGrab
from pyautogui import press
import time

import os


# How many pages is your book
book_length = 3 #OPTION: 160   # ***

# Specify the name of the cover picture (make sure it is a .png)
cover_location = os.getcwd()+"/cover.png" # == "/Users/zrhun/vitalsource-printer/Pirate_Activist/Cover.png"   

# IMPORTANT: Manually specify the dimensions for your screenshot   # ***
X1 = 396*2 #OPTION: 396, 294, 471, 379, 488
Y1 = 128*2 #OPTION: 128, 280, 431, 128, 87
X2 = 886*1.91 #OPTION: 886, 456, 416, 950
Y2 = 761*2 #OPTION: 761, 634, 575, 800
# ***   # Replace the X1, Y1 values with the coordinates of the top left of the ebook and the X2, Y2 with the coordinates of the bottom right.


# You have 5 seconds to switch to the textbook. Make sure you start on the cover page
time.sleep(5)

box = (X1, Y1, X2, Y2)
im_list = []
cover = Image.open(cover_location).convert("RGB")

for i in range(0, book_length):
    # Assuming the right (/down) arrow key switches between pages
    press("right") #OPTION: down
    # Change to press("right") if right arrow key works instead, and so on.

    time.sleep(1)   # arbitrary delay between screenshots
    im = ImageGrab.grab(bbox=box).convert('RGB')
    im_list.append(im)

cover.save("Textbook.pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list)
