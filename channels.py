from tifffile import imread
from PIL import Image, ImageOps
import os

path = 'E:/Bill-Codes/19NOV2022/slide31/'
os.mkdir(path+'_mask/')
os.mkdir(path+'_blue/')
path_mask = path+'_mask/'
x = [item for item in os.listdir(path) if item.endswith('.tiff')]
A = ['red','blue','yellow','green']
for i in range(len(x)):
    image_stack = imread(path+'/'+x[i])
    num,_,_ = image_stack.shape

    for j in range(num):
        L = image_stack[j]
       # L = ImageOps.autocontrast(L, cutoff = 2, ignore = 2)
        im = Image.fromarray(L)
        im.save(path_mask+f'{x[i].replace(".tiff","")}u{A[j]}.tiff')


