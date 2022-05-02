import numpy as np

def c1(img, tons):
    matriz = np.zeros(4*tons*tons).reshape(4, tons, tons)
    for pixel_x in range(len(img)):
        for pixel_y in range(len(img[0])):
            if (pixel_x + 0 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[0][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ 1]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[1][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ 0]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[2][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ 0]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[3][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ -1]]] += 1
    return matriz

def c2(img, tons):
    matriz = np.zeros(12*tons*tons).reshape(12, tons, tons)
    for pixel_x in range(len(img)):
        for pixel_y in range(len(img[0])):
            if (pixel_x + 2 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[0][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ -1]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[1][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ 2]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[2][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ -2]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[3][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ 1]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[4][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ -1]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[5][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ 1]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[6][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ 0]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[7][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ -2]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[8][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ 0]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[9][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ 2]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[10][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ 2]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[11][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ -2]]] += 1
    return matriz

def c4(img, tons):
    matriz = np.zeros(24*tons*tons).reshape(24, tons, tons)
    for pixel_x in range(len(img)):
        for pixel_y in range(len(img[0])):
            if (pixel_x + 4 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[0][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ 0]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[1][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ -2]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[2][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ -3]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[3][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ -4]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[4][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ 3]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[5][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ -1]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[6][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ 1]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[7][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ 4]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[8][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ -3]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[9][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ 3]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[10][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ 2]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[11][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ -4]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[12][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ 4]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[13][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ 0]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[14][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ -3]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[15][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ 3]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[16][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ -1]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[17][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ 2]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[18][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ 1]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[19][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ -2]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[20][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ -3]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[21][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ 4]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[22][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ 3]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[23][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ -4]]] += 1
    return matriz

def c8(img, tons):
    matriz = np.zeros(44*tons*tons).reshape(44, tons, tons)
    for pixel_x in range(len(img)):
        for pixel_y in range(len(img[0])):
            if (pixel_x + -1 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[0][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ 8]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[1][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ 8]]] += 1
            if (pixel_x + -6 < len(img)) and (pixel_y + -5 < len(img[0])):
                matriz[2][img[pixel_x][pixel_y]][img[pixel_x + -6][img[pixel_y+ -5]]] += 1
            if (pixel_x + -5 < len(img)) and (pixel_y + -6 < len(img[0])):
                matriz[3][img[pixel_x][pixel_y]][img[pixel_x + -5][img[pixel_y+ -6]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[4][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ 7]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[5][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ 0]]] += 1
            if (pixel_x + -5 < len(img)) and (pixel_y + 6 < len(img[0])):
                matriz[6][img[pixel_x][pixel_y]][img[pixel_x + -5][img[pixel_y+ 6]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[7][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ -1]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[8][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ -2]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[9][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ 1]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[10][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ 8]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[11][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ -4]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[12][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ -8]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[13][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ -8]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[14][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ 8]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[15][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ 4]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[16][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ 7]]] += 1
            if (pixel_x + 6 < len(img)) and (pixel_y + 5 < len(img[0])):
                matriz[17][img[pixel_x][pixel_y]][img[pixel_x + 6][img[pixel_y+ 5]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[18][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ -7]]] += 1
            if (pixel_x + 5 < len(img)) and (pixel_y + -6 < len(img[0])):
                matriz[19][img[pixel_x][pixel_y]][img[pixel_x + 5][img[pixel_y+ -6]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[20][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ -7]]] += 1
            if (pixel_x + 5 < len(img)) and (pixel_y + 6 < len(img[0])):
                matriz[21][img[pixel_x][pixel_y]][img[pixel_x + 5][img[pixel_y+ 6]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[22][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ -8]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[23][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ 2]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[24][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ -8]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[25][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ 0]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[26][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ -3]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[27][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ 4]]] += 1
            if (pixel_x + 6 < len(img)) and (pixel_y + -5 < len(img[0])):
                matriz[28][img[pixel_x][pixel_y]][img[pixel_x + 6][img[pixel_y+ -5]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[29][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ 8]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[30][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ 3]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[31][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ -7]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[32][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ 7]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[33][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ -1]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[34][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ -2]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[35][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ -8]]] += 1
            if (pixel_x + -6 < len(img)) and (pixel_y + 5 < len(img[0])):
                matriz[36][img[pixel_x][pixel_y]][img[pixel_x + -6][img[pixel_y+ 5]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[37][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ 1]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[38][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ 7]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[39][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ 2]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[40][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ -3]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[41][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ -7]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[42][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ 3]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[43][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ -4]]] += 1
    return matriz

def c16(img, tons):
    matriz = np.zeros(92*tons*tons).reshape(92, tons, tons)
    for pixel_x in range(len(img)):
        for pixel_y in range(len(img[0])):
            if (pixel_x + 10 < len(img)) and (pixel_y + -12 < len(img[0])):
                matriz[0][img[pixel_x][pixel_y]][img[pixel_x + 10][img[pixel_y+ -12]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[1][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ -16]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + -5 < len(img[0])):
                matriz[2][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ -5]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[3][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ -4]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[4][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ 4]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + 5 < len(img[0])):
                matriz[5][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ 5]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[6][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ 16]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[7][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ 16]]] += 1
            if (pixel_x + -10 < len(img)) and (pixel_y + 12 < len(img[0])):
                matriz[8][img[pixel_x][pixel_y]][img[pixel_x + -10][img[pixel_y+ 12]]] += 1
            if (pixel_x + -14 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[9][img[pixel_x][pixel_y]][img[pixel_x + -14][img[pixel_y+ 8]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[10][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ 16]]] += 1
            if (pixel_x + -13 < len(img)) and (pixel_y + -9 < len(img[0])):
                matriz[11][img[pixel_x][pixel_y]][img[pixel_x + -13][img[pixel_y+ -9]]] += 1
            if (pixel_x + 12 < len(img)) and (pixel_y + -10 < len(img[0])):
                matriz[12][img[pixel_x][pixel_y]][img[pixel_x + 12][img[pixel_y+ -10]]] += 1
            if (pixel_x + -12 < len(img)) and (pixel_y + -10 < len(img[0])):
                matriz[13][img[pixel_x][pixel_y]][img[pixel_x + -12][img[pixel_y+ -10]]] += 1
            if (pixel_x + -11 < len(img)) and (pixel_y + -12 < len(img[0])):
                matriz[14][img[pixel_x][pixel_y]][img[pixel_x + -11][img[pixel_y+ -12]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[15][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ 1]]] += 1
            if (pixel_x + -13 < len(img)) and (pixel_y + 9 < len(img[0])):
                matriz[16][img[pixel_x][pixel_y]][img[pixel_x + -13][img[pixel_y+ 9]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + -14 < len(img[0])):
                matriz[17][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ -14]]] += 1
            if (pixel_x + -14 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[18][img[pixel_x][pixel_y]][img[pixel_x + -14][img[pixel_y+ -8]]] += 1
            if (pixel_x + 14 < len(img)) and (pixel_y + 8 < len(img[0])):
                matriz[19][img[pixel_x][pixel_y]][img[pixel_x + 14][img[pixel_y+ 8]]] += 1
            if (pixel_x + -1 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[20][img[pixel_x][pixel_y]][img[pixel_x + -1][img[pixel_y+ -16]]] += 1
            if (pixel_x + -2 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[21][img[pixel_x][pixel_y]][img[pixel_x + -2][img[pixel_y+ -16]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + 14 < len(img[0])):
                matriz[22][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ 14]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[23][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ 3]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + 14 < len(img[0])):
                matriz[24][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ 14]]] += 1
            if (pixel_x + -12 < len(img)) and (pixel_y + 10 < len(img[0])):
                matriz[25][img[pixel_x][pixel_y]][img[pixel_x + -12][img[pixel_y+ 10]]] += 1
            if (pixel_x + 9 < len(img)) and (pixel_y + -13 < len(img[0])):
                matriz[26][img[pixel_x][pixel_y]][img[pixel_x + 9][img[pixel_y+ -13]]] += 1
            if (pixel_x + 0 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[27][img[pixel_x][pixel_y]][img[pixel_x + 0][img[pixel_y+ -16]]] += 1
            if (pixel_x + -5 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[28][img[pixel_x][pixel_y]][img[pixel_x + -5][img[pixel_y+ 15]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + 1 < len(img[0])):
                matriz[29][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ 1]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + -5 < len(img[0])):
                matriz[30][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ -5]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + 4 < len(img[0])):
                matriz[31][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ 4]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + 3 < len(img[0])):
                matriz[32][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ 3]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[33][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ -1]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[34][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ -2]]] += 1
            if (pixel_x + -9 < len(img)) and (pixel_y + 13 < len(img[0])):
                matriz[35][img[pixel_x][pixel_y]][img[pixel_x + -9][img[pixel_y+ 13]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + 6 < len(img[0])):
                matriz[36][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ 6]]] += 1
            if (pixel_x + 11 < len(img)) and (pixel_y + -12 < len(img[0])):
                matriz[37][img[pixel_x][pixel_y]][img[pixel_x + 11][img[pixel_y+ -12]]] += 1
            if (pixel_x + -14 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[38][img[pixel_x][pixel_y]][img[pixel_x + -14][img[pixel_y+ 7]]] += 1
            if (pixel_x + 13 < len(img)) and (pixel_y + -9 < len(img[0])):
                matriz[39][img[pixel_x][pixel_y]][img[pixel_x + 13][img[pixel_y+ -9]]] += 1
            if (pixel_x + 6 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[40][img[pixel_x][pixel_y]][img[pixel_x + 6][img[pixel_y+ -15]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[41][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ 16]]] += 1
            if (pixel_x + 13 < len(img)) and (pixel_y + 9 < len(img[0])):
                matriz[42][img[pixel_x][pixel_y]][img[pixel_x + 13][img[pixel_y+ 9]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + 6 < len(img[0])):
                matriz[43][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ 6]]] += 1
            if (pixel_x + -12 < len(img)) and (pixel_y + -11 < len(img[0])):
                matriz[44][img[pixel_x][pixel_y]][img[pixel_x + -12][img[pixel_y+ -11]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[45][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ 0]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[46][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ 16]]] += 1
            if (pixel_x + -5 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[47][img[pixel_x][pixel_y]][img[pixel_x + -5][img[pixel_y+ -15]]] += 1
            if (pixel_x + 6 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[48][img[pixel_x][pixel_y]][img[pixel_x + 6][img[pixel_y+ 15]]] += 1
            if (pixel_x + 12 < len(img)) and (pixel_y + 10 < len(img[0])):
                matriz[49][img[pixel_x][pixel_y]][img[pixel_x + 12][img[pixel_y+ 10]]] += 1
            if (pixel_x + 14 < len(img)) and (pixel_y + 7 < len(img[0])):
                matriz[50][img[pixel_x][pixel_y]][img[pixel_x + 14][img[pixel_y+ 7]]] += 1
            if (pixel_x + -8 < len(img)) and (pixel_y + -14 < len(img[0])):
                matriz[51][img[pixel_x][pixel_y]][img[pixel_x + -8][img[pixel_y+ -14]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[52][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ 16]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[53][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ 15]]] += 1
            if (pixel_x + 7 < len(img)) and (pixel_y + -14 < len(img[0])):
                matriz[54][img[pixel_x][pixel_y]][img[pixel_x + 7][img[pixel_y+ -14]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + -2 < len(img[0])):
                matriz[55][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ -2]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + -1 < len(img[0])):
                matriz[56][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ -1]]] += 1
            if (pixel_x + 10 < len(img)) and (pixel_y + 12 < len(img[0])):
                matriz[57][img[pixel_x][pixel_y]][img[pixel_x + 10][img[pixel_y+ 12]]] += 1
            if (pixel_x + -10 < len(img)) and (pixel_y + -12 < len(img[0])):
                matriz[58][img[pixel_x][pixel_y]][img[pixel_x + -10][img[pixel_y+ -12]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[59][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ 2]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + 14 < len(img[0])):
                matriz[60][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ 14]]] += 1
            if (pixel_x + -3 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[61][img[pixel_x][pixel_y]][img[pixel_x + -3][img[pixel_y+ -16]]] += 1
            if (pixel_x + -14 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[62][img[pixel_x][pixel_y]][img[pixel_x + -14][img[pixel_y+ -7]]] += 1
            if (pixel_x + 1 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[63][img[pixel_x][pixel_y]][img[pixel_x + 1][img[pixel_y+ -16]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + 0 < len(img[0])):
                matriz[64][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ 0]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + -6 < len(img[0])):
                matriz[65][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ -6]]] += 1
            if (pixel_x + 3 < len(img)) and (pixel_y + -16 < len(img[0])):
                matriz[66][img[pixel_x][pixel_y]][img[pixel_x + 3][img[pixel_y+ -16]]] += 1
            if (pixel_x + 14 < len(img)) and (pixel_y + -7 < len(img[0])):
                matriz[67][img[pixel_x][pixel_y]][img[pixel_x + 14][img[pixel_y+ -7]]] += 1
            if (pixel_x + -11 < len(img)) and (pixel_y + 12 < len(img[0])):
                matriz[68][img[pixel_x][pixel_y]][img[pixel_x + -11][img[pixel_y+ 12]]] += 1
            if (pixel_x + 15 < len(img)) and (pixel_y + -6 < len(img[0])):
                matriz[69][img[pixel_x][pixel_y]][img[pixel_x + 15][img[pixel_y+ -6]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + 2 < len(img[0])):
                matriz[70][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ 2]]] += 1
            if (pixel_x + -16 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[71][img[pixel_x][pixel_y]][img[pixel_x + -16][img[pixel_y+ -3]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + -4 < len(img[0])):
                matriz[72][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ -4]]] += 1
            if (pixel_x + -15 < len(img)) and (pixel_y + 5 < len(img[0])):
                matriz[73][img[pixel_x][pixel_y]][img[pixel_x + -15][img[pixel_y+ 5]]] += 1
            if (pixel_x + 12 < len(img)) and (pixel_y + -11 < len(img[0])):
                matriz[74][img[pixel_x][pixel_y]][img[pixel_x + 12][img[pixel_y+ -11]]] += 1
            if (pixel_x + 4 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[75][img[pixel_x][pixel_y]][img[pixel_x + 4][img[pixel_y+ -15]]] += 1
            if (pixel_x + -9 < len(img)) and (pixel_y + -13 < len(img[0])):
                matriz[76][img[pixel_x][pixel_y]][img[pixel_x + -9][img[pixel_y+ -13]]] += 1
            if (pixel_x + 5 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[77][img[pixel_x][pixel_y]][img[pixel_x + 5][img[pixel_y+ -15]]] += 1
            if (pixel_x + -6 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[78][img[pixel_x][pixel_y]][img[pixel_x + -6][img[pixel_y+ -15]]] += 1
            if (pixel_x + -7 < len(img)) and (pixel_y + -14 < len(img[0])):
                matriz[79][img[pixel_x][pixel_y]][img[pixel_x + -7][img[pixel_y+ -14]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + -15 < len(img[0])):
                matriz[80][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ -15]]] += 1
            if (pixel_x + 5 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[81][img[pixel_x][pixel_y]][img[pixel_x + 5][img[pixel_y+ 15]]] += 1
            if (pixel_x + 16 < len(img)) and (pixel_y + -3 < len(img[0])):
                matriz[82][img[pixel_x][pixel_y]][img[pixel_x + 16][img[pixel_y+ -3]]] += 1
            if (pixel_x + -6 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[83][img[pixel_x][pixel_y]][img[pixel_x + -6][img[pixel_y+ 15]]] += 1
            if (pixel_x + 9 < len(img)) and (pixel_y + 13 < len(img[0])):
                matriz[84][img[pixel_x][pixel_y]][img[pixel_x + 9][img[pixel_y+ 13]]] += 1
            if (pixel_x + 8 < len(img)) and (pixel_y + 14 < len(img[0])):
                matriz[85][img[pixel_x][pixel_y]][img[pixel_x + 8][img[pixel_y+ 14]]] += 1
            if (pixel_x + 2 < len(img)) and (pixel_y + 16 < len(img[0])):
                matriz[86][img[pixel_x][pixel_y]][img[pixel_x + 2][img[pixel_y+ 16]]] += 1
            if (pixel_x + -4 < len(img)) and (pixel_y + 15 < len(img[0])):
                matriz[87][img[pixel_x][pixel_y]][img[pixel_x + -4][img[pixel_y+ 15]]] += 1
            if (pixel_x + 12 < len(img)) and (pixel_y + 11 < len(img[0])):
                matriz[88][img[pixel_x][pixel_y]][img[pixel_x + 12][img[pixel_y+ 11]]] += 1
            if (pixel_x + -12 < len(img)) and (pixel_y + 11 < len(img[0])):
                matriz[89][img[pixel_x][pixel_y]][img[pixel_x + -12][img[pixel_y+ 11]]] += 1
            if (pixel_x + 11 < len(img)) and (pixel_y + 12 < len(img[0])):
                matriz[90][img[pixel_x][pixel_y]][img[pixel_x + 11][img[pixel_y+ 12]]] += 1
            if (pixel_x + 14 < len(img)) and (pixel_y + -8 < len(img[0])):
                matriz[91][img[pixel_x][pixel_y]][img[pixel_x + 14][img[pixel_y+ -8]]] += 1
    return matriz


print(c16([], 8))