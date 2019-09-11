import scipy.io.wavfile
import numpy as np
import math
import matplotlib.pyplot as plotagem #Plotagem de gráficos
import cv2
from PIL import Image

pixels = []
h = 0
w = 0
matrizPixels = []

def dct1D(vector):
    N = len(vector)
    print(N)
    X = np.zeros(N)
    for k in range(N):
        if(k == 0):
            CK = math.sqrt(1.0/N)
        else:
            CK = math.sqrt(2.0/N)

        sum = 0
        for n in range(N):
            dct1 = vector[n] * math.cos(((2*k+1)*n*math.pi/(2*N)))
            sum += dct1

        X[k] = CK * sum
        print("Nível DC --> "+X[0])

    return X

def compactadorExpansor(vector, c):
    N = len(vector)
    print(N)
    X = np.zeros(N)
    for k in range(N):
        if(k == 0):
            CK = math.sqrt(1.0/N)
        else:
            CK = math.sqrt(2.0/N)

        sum = 0
        for n in range(N):
            dct1 = vector[n] * math.cos(((2*k+1)*n*math.pi/(2*N)))
            sum += dct1

        X[math.round(k*c)] = CK * sum

    return X

def preservarCoeficientes(vector, coef):
    N = len(vector)
    print(N)
    X = np.zeros(N)
    for k in range(N):
        if(k == 0):
            CK = math.sqrt(1.0/N)
        else:
            CK = math.sqrt(2.0/N)

        lista = []
        sum = 0
        for n in range(N):
            dct1 = vector[n] * math.cos(((2*k+1)*n*math.pi/(2*N)))
            lista.append(dct1)

        lista.sort(reverse=True)
        for a in range(coef):
            sum+=lista[a]
        X[k] = CK * sum
    return X


def captaImagem(path):
    imagem = cv2.imread(path)
    #cv2.imshow("Original", imagem)
    h = imagem.shape[0]
    w = imagem.shape[1]
    for i in range(h):
        for j in range(w):
            pixels.append((int(imagem[i, j][0])+int(imagem[i, j][1])+int(imagem[i, j][2]))/3)
    geraMatrizPixels(h, w)
    cv2.waitKey(0)
    return [h, w]

def geraMatrizPixels(h, w):
    for i in range(h):
        matrizPixels.append([])
        for j in range(w):
            matrizPixels[i].append(pixels[i*w+j])

def dct2d(matriz, path):
    lista = captaImagem(path)
    h = lista[0]
    w = lista[1]
    dct = []
    for i in range(1, h, 1):
        dct.append([])
        for j in range(w):
            if(i==0):
                ci = 1/math.sqrt(h)
            else:
                ci = math.sqrt(2)/math.sqrt(h)
            if(j==0):
                cj = 1/math.sqrt(h)
            else:
                cj = math.sqrt(2)/math.sqrt(h)

            soma = 0
            for k in range(h):
                for l in range(w):
                    dct1 = matriz[k][l]*math.cos((2*k+1)*i*math.pi/(2*h))*math.cos((2*l+1)*j*math.pi/(2*w))
                    soma+=dct1
            dct[i].append(ci*cj*soma)
    return dct

def preservarCoeficientes2(matriz, path, coef):
    lista = captaImagem(path)
    h = lista[0]
    w = lista[1]
    dct = []
    for i in range(1, h, 1):
        dct.append([])
        for j in range(w):
            if(i==0):
                ci = 1/math.sqrt(h)
            else:
                ci = math.sqrt(2)/math.sqrt(h)
            if(j==0):
                cj = 1/math.sqrt(h)
            else:
                cj = math.sqrt(2)/math.sqrt(h)

            lista = []
            soma = 0
            for k in range(h):
                for l in range(w):
                    dct1 = matriz[k][l]*math.cos((2*k+1)*i*math.pi/(2*h))*math.cos((2*l+1)*j*math.pi/(2*w))
                    lista.append(dct1)
            lista.sort(reverse=True)
            for a in range(coef):
                soma+=lista[a]
            dct[i].append(ci*cj*soma)
    return dct

def desenhaGrafico (data):
    plotagem.figure('Data')
    plotagem.plot(data, linewidth=0.1, alpha=1,color='red')
    plotagem.ylabel('Amplitude')
    plotagem.show()

def plotaDCTs(dct):
	plotagem.figure('Domínio da Frequência')
	plotagem.subplot(211)
	plotagem.plot(dct, linewidth=0.1, alpha=1.0, color='blue')
	plotagem.ylabel('Frequencia')
	plotagem.show()

	'''plotagem.subplot(212)
	plotagem.plot(dctFiltrada, linewidth=0.1, alpha=1.0, color='blue')
	plotagem.ylabel('Frequencia')
	plotagem.show()'''

rate, audioData = scipy.io.wavfile.read ("MaisUmaSemana.wav")

lista = dct2d(matrizPixels,"lena.bmp")
#print("AA")
#desenhaGrafico (audioData)
#DCT = dct1D(audioData)
c_array = np.asarray(lista)

im = Image.fromarray(c_array)

im.show()
#plotaDCTs(DCT)
