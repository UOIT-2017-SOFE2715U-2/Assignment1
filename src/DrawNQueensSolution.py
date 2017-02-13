# the images of the tiles and the queens were taken from:
#   https://en.wikipedia.org/wiki/Eight_queens_puzzle
#   Licence: By en:User:Cburnett - Own workThis vector image was created with Inkscape., CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1496714
#   the images files were renamed to make the code more readable.
#   one image, namely light_queen.png was converted from RBG 24 bits to RGBA 32 bits to match other images.
# This code needs numpy and Pillow packages.

import numpy as np
from PIL import Image
import os


def DrawNQueensSolution(numberOfQueens, sol_list, solutionNumber):
    path = "../solutions/" + str(numberOfQueens) + "-Queens Solutions/"
    if not os.path.exists(path):
        os.makedirs(path)

    img_Dark_queen = '../img/dark_queen.png'
    img_light_queen = '../img/light_queen.png'
    img_Dark_tile = '../img/dark_tile.png'
    img_light_tile = '../img/light_tile.png'
    list_im = []
    vlist_im = []

    for row in range(0,numberOfQueens):
        for column in range(0, numberOfQueens):
            if (row + column) % 2 == 0: #light
                if sol_list[row] == column:
                    list_im.append(img_light_queen)
                else:
                    list_im.append((img_light_tile))
            else: #dark
                if sol_list[row] == column:
                    list_im.append(img_Dark_queen)
                else:
                    list_im.append((img_Dark_tile))
        imgs = [Image.open(i) for i in list_im]
        imgs_comb = np.hstack(imgs)
        imgs_comb = Image.fromarray(imgs_comb)
        vlist_im.append(imgs_comb)
        list_im = []
    imgs_comb = np.vstack(vlist_im)
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(path + str(solutionNumber) + ".png")
