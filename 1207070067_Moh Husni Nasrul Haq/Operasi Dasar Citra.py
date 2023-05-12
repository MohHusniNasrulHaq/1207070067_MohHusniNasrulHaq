import matplotlib.pyplot as plt #memanggil library matplotlib
#matplotlib inline
#memanggil library skimage
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
from skimage.util import invert
from skimage import io

import numpy as np #memanggil library numpy

#==============================Cropping Image========================#
dino = io.imread ("dino.jpg") #membaca gambar yang diinputkan dengan library dari skimage io
dinosaurus = io.imread("dinosaurus.jpg") #membaca gambar yang diinputkan dengan library dari skimage io

dino_Cropped = dino.copy() #mengcrop dan copy gambar pada indeks pixel untuk mendapatkan bagian dari citra yang diinginkan dalam gambar1
dino_Cropped = dino_Cropped[0:256,64:300]

dinosaurus_Cropped = dinosaurus.copy() #mengcrop dan copy gambar pada indeks pixel untuk mendapatkan bagian dari citra yang diinginkan dalam gambar2
dinosaurus_Cropped = dinosaurus_Cropped[64:256,128:320]

print('Dino Ori Shape : ',dino.shape) #menampilkan citra asli dengan fungsi shape
print('Dino Crop Shape : ',dino.shape) #menampilkan citra hasil crop dengan fungsi shape

print('Dinosaurus Ori Shape : ',dinosaurus.shape) #menampilkan citra asli dengan fungsi shape
print('Dinosaurus Crop Shape : ',dinosaurus.shape) #menampilkan citra hasil crop dengan fungsi shape

fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #ngplot citra dengan subplot ukuran 2x2
ax = axes.ravel()

ax[0].imshow(dino)
ax[0].set_title("Citra Input 1")

ax[1].imshow(dinosaurus, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(dino_Cropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(dinosaurus_Cropped, cmap='gray')
ax[3].set_title('Citra Output 2')
plt.show() #menampilkan citra hasil

#=========================== Citra Negative ================================#
inv = invert(dino_Cropped)
print('Shape Input : ', dino_Cropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #ngplot citra dengan subplot ukuran 2x2
ax = axes.ravel()

ax[0].imshow(dino_Cropped)
ax[0].set_title("Citra Input") #membuat judul

ax[1].hist(dino_Cropped.ravel(), bins=256) 
ax[1].set_title('Histogram Input') #membuat judul

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)') #membuat judul

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output') #membuat judul

copyFoto = dinosaurus_Cropped.copy().astype(float)

shape = copyFoto.shape
output1 = np.empty(shape)

for baris in range(0, shape[0]): #mendapat koordinat baris atau rentang pixel pada gambar yang diubah nilai
    for kolom in range(0, shape[1]): #mendapat koordinat kolom atau rentang pixel pada gambar yang diubah nilai
        a1 = baris #variable a1 untuk baris
        b1 = kolom #variable b1 untuk kolom
        output1[a1, b1] = copyFoto[baris, kolom] + 100 #menghitung nilai brightness baru

#menampilkan citra input,histogram input,citra brightness output dan histogram input
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #ngplot citra dengan subplot ukuran 2x2
ax = axes.ravel()

ax[0].imshow(dinosaurus_Cropped, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(dino_Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')

plt.show() #menampilkan hasil gambarnya