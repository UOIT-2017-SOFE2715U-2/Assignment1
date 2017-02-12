#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
import numpy as np
from PIL import Image
import os

def DrawNQueensSolution(dimentions, sol_list, solutionNumber):
    path = "../solutions/" + str(dimentions) + "-Queens Solutions/"
    if not os.path.exists(path):
        os.makedirs(path)

    img_Dark_queen = '../img/dark_queen.png'
    img_light_queen = '../img/light_queen.png'
    img_Dark_tile = '../img/dark_tile.png'
    img_light_tile = '../img/light_tile.png'
    list_im = []
    vlist_im = []

    for row in range(0,dimentions):
        for column in range(0, dimentions):
            if (row + column) % 2 == 0: #light
                if sol_list[row] == column:
                    list_im.append(img_light_queen)
                else:
                    list_im.append((img_light_tile))
            else:
                if sol_list[row] == column:
                    list_im.append(img_Dark_queen)
                else:
                    list_im.append((img_Dark_tile))
        imgs = [Image.open(i) for i in list_im]
        min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
        imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
        imgs_comb = Image.fromarray(imgs_comb)
        vlist_im.append(imgs_comb)
        list_im = []
    imgs_comb = np.vstack(vlist_im)
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(path + str(solutionNumber) + ".png")

#DrawNQueensSolution(5,[0,2,4,1,3])