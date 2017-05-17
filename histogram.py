import cv2
import numpy as np
from matplotlib import pyplot as plt
#untuk mengimport modul atau library

gray_img = cv2.imread('Pot Bunga.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Pot Bunga', gray_img)
#untuk inisialisasi gambar dan mengubah ke skala keabuan

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
#fungsi histogram

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram Skala Keabuan')
plt.show()
#menampilkan gambar dalam bingkai dengan nama "Histogram Skala Keabuan"

while True:
     k = cv2.waitKey(0) & 0xFF
     if k == 27 : break           
cv2.destroyAllWindows()
#untuk menutup bingkai jika tombol ESC ditekan