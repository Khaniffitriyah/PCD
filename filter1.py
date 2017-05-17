import cv2
import numpy as np
from matplotlib import pyplot as plt
#untuk mengimport modul atau library

img = cv2.imread('Kamboja.jpg')
#untuk inisialisasi gambar

blur = cv2.blur(img,(5,5))
#memberikan efek blur

blur2 = cv2.GaussianBlur(img,(5,5),0)
#memberikan efek gaussian blur

plt.subplot(2,2,1),plt.imshow(img),plt.title('Gambar Asli')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(blur),plt.title('Blured')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(blur2),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()
#menampilkan gambar dalam satu bingkai