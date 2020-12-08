#! /usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
"""
Find the monomials involved in the SOS decomposition

Part of the following project:
http://www-ljk.imag.fr/membres/Roland.Hildebrand/emo/project_description.pdf from a MSIAM course.

- *Date:* Tuesday, December the 8th, 2020
- *Author:* Sofiane Tanji, for the MSIAM Master
- *Licence:* GNU GPL3 Licence
"""
# Libraries
import numpy as np
import matplotlib.pyplot as plt

def fill_ind(indexes):
    """
    input : list of tuples (i, j)
    output : same list + all the non-present (i, i) tuples
    """
    output = [elt for elt in indexes]
    for i in range(56):
        if (i, i) not in output:
            output.append((i, i))
    output.sort()
    return output

fam1 = [(2, 2), (5, 5), (6, 6), (7, 7), (8, 8), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (18, 18), (20, 20), (21, 21), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (25, 22), (25, 23), (25, 24), (25, 25), (25, 26), (25, 27), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (26, 27), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (31, 31), (31, 32), (31, 33), (31, 34), (31, 35), (31, 36), (32, 31), (32, 32), (32, 33), (32, 34), (32, 35), (32, 36), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (34, 31), (34, 32), (34, 33), (34, 34), (34, 35), (34, 36), (35, 31), (35, 32), (35, 33), (35, 34), (35, 35), (35, 36), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), (36, 36), (38, 38), (38, 39), (38, 40), (38, 41), (38, 42), (38, 43), (39, 38), (39, 39), (39, 40), (39, 41), (39, 42), (39, 43), (40, 38), (40, 39), (40, 40), (40, 41), (40, 42), (40, 43), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (44, 44), (44, 45), (44, 46), (44, 47), (44, 48), (44, 49), (45, 44), (45, 45), (45, 46), (45, 47), (45, 48), (45, 49), (46, 44), (46, 45), (46, 46), (46, 47), (46, 48), (46, 49), (47, 44), (47, 45), (47, 46), (47, 47), (47, 48), (47, 49), (48, 44), (48, 45), (48, 46), (48, 47), (48, 48), (48, 49), (49, 44), (49, 45), (49, 46), (49, 47), (49, 48), (49, 49), (50, 50), (50, 51), (50, 52), (50, 53), (50, 54), (50, 55), (51, 50), (51, 51), (51, 52), (51, 53), (51, 54), (51, 55), (52, 50), (52, 51), (52, 52), (52, 53), (52, 54), (52, 55), (53, 50), (53, 51), (53, 52), (53, 53), (53, 54), (53, 55), (54, 50), (54, 51), (54, 52), (54, 53), (54, 54), (54, 55), (55, 50), (55, 51), (55, 52), (55, 53), (55, 54), (55, 55)]
fam2 = [(1, 1), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (17, 17), (18, 18), (19, 19), (20, 20), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (25, 22), (25, 23), (25, 24), (25, 25), (25, 26), (25, 27), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (26, 27), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (31, 31), (31, 32), (31, 33), (31, 34), (31, 35), (31, 36), (32, 31), (32, 32), (32, 33), (32, 34), (32, 35), (32, 36), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (34, 31), (34, 32), (34, 33), (34, 34), (34, 35), (34, 36), (35, 31), (35, 32), (35, 33), (35, 34), (35, 35), (35, 36), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), (36, 36), (38, 38), (38, 39), (38, 40), (38, 41), (38, 42), (38, 43), (39, 38), (39, 39), (39, 40), (39, 41), (39, 42), (39, 43), (40, 38), (40, 39), (40, 40), (40, 41), (40, 42), (40, 43), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (44, 44), (44, 45), (44, 46), (44, 47), (44, 48), (44, 49), (45, 44), (45, 45), (45, 46), (45, 47), (45, 48), (45, 49), (46, 44), (46, 45), (46, 46), (46, 47), (46, 48), (46, 49), (47, 44), (47, 45), (47, 46), (47, 47), (47, 48), (47, 49), (48, 44), (48, 45), (48, 46), (48, 47), (48, 48), (48, 49), (49, 44), (49, 45), (49, 46), (49, 47), (49, 48), (49, 49), (50, 50), (50, 51), (50, 52), (50, 53), (50, 54), (50, 55), (51, 50), (51, 51), (51, 52), (51, 53), (51, 54), (51, 55), (52, 50), (52, 51), (52, 52), (52, 53), (52, 54), (52, 55), (53, 50), (53, 51), (53, 52), (53, 53), (53, 54), (53, 55), (54, 50), (54, 51), (54, 52), (54, 53), (54, 54), (54, 55), (55, 50), (55, 51), (55, 52), (55, 53), (55, 54), (55, 55)]
fam3 = [(3, 3), (4, 4), (5, 5), (7, 7), (8, 8), (9, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (21, 21), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (25, 22), (25, 23), (25, 24), (25, 25), (25, 26), (25, 27), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (26, 27), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (31, 31), (31, 32), (31, 33), (31, 34), (31, 35), (31, 36), (32, 31), (32, 32), (32, 33), (32, 34), (32, 35), (32, 36), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (34, 31), (34, 32), (34, 33), (34, 34), (34, 35), (34, 36), (35, 31), (35, 32), (35, 33), (35, 34), (35, 35), (35, 36), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), (36, 36), (38, 38), (38, 39), (38, 40), (38, 41), (38, 42), (38, 43), (39, 38), (39, 39), (39, 40), (39, 41), (39, 42), (39, 43), (40, 38), (40, 39), (40, 40), (40, 41), (40, 42), (40, 43), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (44, 44), (44, 45), (44, 46), (44, 47), (44, 48), (44, 49), (45, 44), (45, 45), (45, 46), (45, 47), (45, 48), (45, 49), (46, 44), (46, 45), (46, 46), (46, 47), (46, 48), (46, 49), (47, 44), (47, 45), (47, 46), (47, 47), (47, 48), (47, 49), (48, 44), (48, 45), (48, 46), (48, 47), (48, 48), (48, 49), (49, 44), (49, 45), (49, 46), (49, 47), (49, 48), (49, 49), (50, 50), (50, 51), (50, 52), (50, 53), (50, 54), (50, 55), (51, 50), (51, 51), (51, 52), (51, 53), (51, 54), (51, 55), (52, 50), (52, 51), (52, 52), (52, 53), (52, 54), (52, 55), (53, 50), (53, 51), (53, 52), (53, 53), (53, 54), (53, 55), (54, 50), (54, 51), (54, 52), (54, 53), (54, 54), (54, 55), (55, 50), (55, 51), (55, 52), (55, 53), (55, 54), (55, 55)]
fam4 = [(1, 1), (3, 3), (4, 4), (5, 5), (6, 6), (8, 8), (9, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (25, 22), (25, 23), (25, 24), (25, 25), (25, 26), (25, 27), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (26, 27), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (31, 32), (31, 33), (31, 34), (31, 35), (31, 36), (32, 31), (32, 32), (32, 33), (32, 34), (32, 35), (32, 36), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (34, 31), (34, 32), (34, 33), (34, 34), (34, 35), (34, 36), (35, 31), (35, 32), (35, 33), (35, 34), (35, 35), (35, 36), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), (36, 36), (37, 37), (38, 38), (38, 39), (38, 40), (38, 41), (38, 42), (38, 43), (39, 38), (39, 39), (39, 40), (39, 41), (39, 42), (39, 43), (40, 38), (40, 39), (40, 40), (40, 41), (40, 42), (40, 43), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (44, 44), (44, 45), (44, 46), (44, 47), (44, 48), (44, 49), (45, 44), (45, 45), (45, 46), (45, 47), (45, 48), (45, 49), (46, 44), (46, 45), (46, 46), (46, 47), (46, 48), (46, 49), (47, 44), (47, 45), (47, 46), (47, 47), (47, 48), (47, 49), (48, 44), (48, 45), (48, 46), (48, 47), (48, 48), (48, 49), (49, 44), (49, 45), (49, 46), (49, 47), (49, 48), (49, 49), (50, 50), (50, 51), (50, 52), (50, 53), (50, 54), (50, 55), (51, 50), (51, 51), (51, 52), (51, 53), (51, 54), (51, 55), (52, 50), (52, 51), (52, 52), (52, 53), (52, 54), (52, 55), (53, 50), (53, 51), (53, 52), (53, 53), (53, 54), (53, 55), (54, 50), (54, 51), (54, 52), (54, 53), (54, 54), (54, 55), (55, 50), (55, 51), (55, 52), (55, 53), (55, 54), (55, 55)]
fam5 = [(3, 3), (4, 4), (5, 5), (7, 7), (8, 8), (9, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (21, 21), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (25, 22), (25, 23), (25, 24), (25, 25), (25, 26), (25, 27), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (26, 27), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (31, 31), (31, 32), (31, 33), (31, 34), (31, 35), (31, 36), (32, 31), (32, 32), (32, 33), (32, 34), (32, 35), (32, 36), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (34, 31), (34, 32), (34, 33), (34, 34), (34, 35), (34, 36), (35, 31), (35, 32), (35, 33), (35, 34), (35, 35), (35, 36), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), (36, 36), (38, 38), (38, 39), (38, 40), (38, 41), (38, 42), (38, 43), (39, 38), (39, 39), (39, 40), (39, 41), (39, 42), (39, 43), (40, 38), (40, 39), (40, 40), (40, 41), (40, 42), (40, 43), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (44, 44), (44, 45), (44, 46), (44, 47), (44, 48), (44, 49), (45, 44), (45, 45), (45, 46), (45, 47), (45, 48), (45, 49), (46, 44), (46, 45), (46, 46), (46, 47), (46, 48), (46, 49), (47, 44), (47, 45), (47, 46), (47, 47), (47, 48), (47, 49), (48, 44), (48, 45), (48, 46), (48, 47), (48, 48), (48, 49), (49, 44), (49, 45), (49, 46), (49, 47), (49, 48), (49, 49), (50, 50), (50, 51), (50, 52), (50, 53), (50, 54), (50, 55), (51, 50), (51, 51), (51, 52), (51, 53), (51, 54), (51, 55), (52, 50), (52, 51), (52, 52), (52, 53), (52, 54), (52, 55), (53, 50), (53, 51), (53, 52), (53, 53), (53, 54), (53, 55), (54, 50), (54, 51), (54, 52), (54, 53), (54, 54), (54, 55), (55, 50), (55, 51), (55, 52), (55, 53), (55, 54), (55, 55)]

print("---------------------------------------------------------------")
print("For any family, the C matrix is built using the same monomials: ")
print(fill_ind(fam1) == fill_ind(fam2) == fill_ind(fam3) == fill_ind(fam4) == fill_ind(fam5))
print("---------------------------------------------------------------")

fam1 = fill_ind(fam1)
fam2, fam3, fam4, fam5 = fam1, fam1, fam1, fam1

perm = [48, 47, 46, 45, 43, 42, 41, 39, 38, 36, 55, 49, 44, 40, 35, 37, 28, 27, 26, 24, 23, 21, 29, 25, 22, 54, 34, 20, 14, 13, 11, 53, 19, 15, 12, 33, 10, 5, 52, 18, 9, 6, 32, 4, 31, 51, 17, 8, 1, 3, 30, 50, 16, 7, 0, 2]

def mapping(indexes, permutation):
    """
    Given indexes in the re-ordered matrix and the permutation used,
    find the corresponding indexes in the original matrix.
    """
    output = []
    for i, j in indexes:
        output.append((permutation[i], permutation[j]))
    return output

def build_mats(indexes):
    blockd = np.zeros((56, 56))
    ori_built = np.zeros((56, 56))
    mapp = mapping(indexes, perm)
    for i,j in indexes:
        blockd[i][j] = 5
    for i,j in mapp:
        ori_built[i][j] = 5
    return blockd, ori_built

def plotting(indexes):
    """test
    """
    blockd, ori_built = build_mats(indexes)
    fig, axes = plt.subplots(ncols=2, figsize=(12, 6))
    ax1, ax2 = axes
    ax1.grid(False)
    ax2.grid(False)
    im1 = ax1.imshow(blockd, interpolation = 'nearest',
    cmap = plt.get_cmap("Spectral"))
    ax1.title.set_text('Block-diagonal matrix')
    im2 = ax2.imshow(ori_built, interpolation = 'nearest',
    cmap = plt.get_cmap("Spectral"))
    ax2.title.set_text('Reconstructed original matrix')
    fig.colorbar(im1, ax = ax1)
    fig.colorbar(im2, ax = ax2)
    plt.show()
print("Checking it with matplotlib")
plotting(fam1)
print("---------------------------------------------------------------")
