import cv2 
import math
import numpy as np
import random
import Image
im = Image.open('download.jfif')
im.save('download.jpeg')
im2 = Image.open('encrypted_img.jpeg')
im2.save('encryped_img.jfif')


class Affine:
    def __init__(self, a, b, m ):
        self.a = a
        self.b = b
        self.m = m
        while self.IsCoprime() is False:
            print(a,m,)
            a,m = map(int,input(" ").split(" "))
            self.a = a
            self.m = m
        self.inv_a =  self.ModInv()
    def IsCoprime(self):
        if math.gcd(self.a, self.m) == 1:
            return True
        return False
    def ModInv(self):
        for i in range(2,self.m):
            if (self.a * i) % self.m == 1 :
                return i
        return 1
    def E(self, x):       
        return (self.a*x + self.b) % self.m
    def encryption(self, original_img):
        height = img.shape[0]
        width = img.shape[1]
        
        for i in range(0,height):
            for j in range(0,width):
                a = original_img[i][j]      
                r = self.E(a[0])
                g = self.E(a[1])
                b = self.E(a[2])
                original_img[i][j] = [r,g,b]
        cv2.imwrite('encrypted_img.jpeg', img)  
A = Affine(5,8,26)
img=cv2.imread('download.jpeg')
A.encryption(img)