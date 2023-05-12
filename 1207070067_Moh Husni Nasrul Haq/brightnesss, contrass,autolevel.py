import numpy as np #memanggil library numpy
import cv2 #memanggil library imageio
import matplotlib.pyplot as plt #memanggil library matplotlib

img = cv2.imread("dinosaurus.jpg") #membaca gambar

#Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0] #memanggil atau mendapatkan resolusi tinnggi
img_width = img.shape[1] #memanggil atau mendapatkan resolusi lebar
img_channel = img.shape[2] #memanggil atau mendapatkan channel/warna
img_type = img.dtype #membaca tipe gambar

#===================Brightness Grayscale===================#
#Membuat variabel img_brightness untuk menampung hasil
img_brightness = np.zeros(img.shape, dtype=np.uint8)

#Melakukan penambahan brightness dengan nilai yg menjadi parameter
def brighter(nilai): #fungsi def untuk brightness
    for y in range(0, img_height):#variable y dalam rentang 0, dan dari resolusi tinggi      
        for x in range(0, img_width): ##variable x dalam rentang 0, dan dari resolusi lebar   
            red = img[y][x][0] #nilai red dari variabel rentang nilai resolusi y,x
            green = img[y][x][1] #nilai green dari variabel rentang nilai resolusi y,x
            blue = img[y][x][2] #nilai blue dari variabel rentang nilai resolusi y,x
            gray = (int(red) + int(green) + int(blue)) / 3 #mengkonversi gambar rgb ke greyscale
            gray += nilai #nilai hasil konversi perhitungan greyscale
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
brighter(-100) #menggelapkan gambar
plt.imshow(img_brightness) #memanggil hasil gambar yang dikonversi
plt.title("Brightness -100") #memberi judul gambar
plt.show() #menampilkan gambar

brighter(100) #mencerahkan gambar
plt.imshow(img_brightness) #memanggil hasil gambar yang dikonversi
plt.title("Brightness 100") #memberi judul gambar
plt.show() #menampilkan gambar

#===================Brightness RGB=====================#
img_rgbbrightness = np.zeros(img.shape, dtype=np.uint8) #Membuat variabel img_rgbbrightness untuk menampung hasil

#Melakukan penambahan brightness dengan nilai yg menjadi parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255 :
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbrightness[y][x] = (red, green, blue)
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100) #menggelapkan gambar RGB
plt.imshow(img_rgbbrightness) #memanggil hasil gambar yang dikonversi
plt.title("Brightness RGB -100") #memberi judul gambar
plt.show() #menampilkan hasil gambar

rgbbrighter(100) #mencerahkan gambar RGB
plt.imshow(img_rgbbrightness) #memanggil hasil gambar yang dikonversi
plt.title("Brightness RGB 100") #memberi judul gambar
plt.show() #menampilkan hasil gambar

#========================Contrass===================#
img_contrass = np.zeros(img.shape, dtype=np.uint8) #variabel img_contrass untuk menampung hasil

#Melakukan penambahan contrass dengan nilai yg menjadi parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray *= nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)
#Menampilkan beberapa hasil dengan nilai contrass 50 dan 100
contrass(2) #perintah untuk kontraskan gambar
plt.imshow(img_contrass) #memanggil hasil gambar yang dikonversi
plt.title("Contrass 2") #memberi judul gambar
plt.show() #menampilkan hasil gambar

contrass(3) #perintah untuk kontraskan gambar
plt.imshow(img_contrass) #memanggil hasil gambar yang dikonversi
plt.title("Contrass 3") #memberi judul gambar
plt.show() #menampilkan hasil gambar

#==========================Contrass Autolevel=========================#
img_autocontrass = np.zeros(img.shape, dtype=np.uint8) #variabel img_contrass untuk menampung hasil

#Melakukan penambahan contrass secara otomatis
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)
#Menampilkan hasil autolevel contrass
autocontrass() #memerintah untuk autolevel contrass gambar
plt.imshow(img_autocontrass) #memanggil hasil gambar yang dikonversi
plt.title("Contrass Autolevel") #memberi judul gambar
plt.show() #menampilkan hasil gambar