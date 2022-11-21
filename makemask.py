import numpy as np
import cv2
import os 

path_mask = 'E:/Bill-Codes/19NOV2022/slide31/_mask/'

x = [item for item in os.listdir(path_mask) if item.endswith('.tiff')]
path_blue = 'E:/Bill-Codes/19NOV2022/slide31/_blue/'


def blackandwhite(path, thresh = 1):
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresh = 10
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    return im_bw

def blackandwhite1(path, thresh = 1):
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresh = 1
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    return im_bw

def blackandwhite2(path, thresh = 1):
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresh = 1
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    return im_bw
    
def blackandwhite3(path, thresh = 1):
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresh = 1
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    return im_bw
    
A = []
B = ['red','blue','yellow','green']
for i in range(len(x)):
    if i%4 == 0:
        A.append(x[i].split('u')[0])
        
for i in range(len(A)):
    red = blackandwhite2(path_mask+A[i]+'u'+'red.tiff')
    blue = blackandwhite(path_mask+A[i]+'u'+'blue.tiff')
    green = blackandwhite3(path_mask+A[i]+'u'+'green.tiff')
    yellow = blackandwhite1(path_mask+A[i]+'u'+'yellow.tiff')
    
    

    
    
    blue = cv2.bitwise_or(red, blue)
    
    #yellow3 = cv2.bitwise_xor(yellow, yellow2)
    
    blue4 = cv2.bitwise_and(yellow, blue)
    blue5 = cv2.bitwise_xor(blue4, blue)
    cv2.imwrite(path_blue+A[i]+'_M'+'.png', blue5)    
    green4 = cv2.bitwise_and(green, blue5)
    green5 = cv2.bitwise_xor(green4, green)
    cv2.imwrite(path_blue+A[i]+'_2'+'.png', green5)

'''        

blue = blackandwhite
red = cv2.imread('003_+0_red.png', cv2.IMREAD_UNCHANGED)
red1 = cv2.bitwise_or(blue, red)
#red2 = cv2.bitwise_xor(red1, red)

cv2.imwrite('blueandred.png', red1)



blue = cv2.imread('blueandred.png', cv2.IMREAD_UNCHANGED)
red = cv2.imread('003_+0_yello.png', cv2.IMREAD_UNCHANGED)
red1 = cv2.bitwise_and(blue, red)
red2 = cv2.bitwise_xor(blue, red1)

cv2.imwrite('final003003.png', red2)
'''