import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio
import os

file_path = 'tiles'
filenames = os.listdir(file_path)
tileset = {}
dimensions = [6,6]

for filename in filenames:
    #print(filename[:-4])
    image = imageio.imread(file_path + '/' + filename)
    tileset[filename[:-4]]=image

keys = list(tileset.keys())
#all combinations
print(keys)
plot = np.chararray(dimensions, itemsize=4)

start = np.random.randint(0,11)
'''0-2, 2-0,1-3,3-1'''
plot[:] = keys[start]
print(str(plot))



def chose_tile(x,y):
    variants = []

    for key in keys:
        if x==0 and y==0:

            return  plot[0,0]
        if y>0 and x>0 and chr(plot[y,x-1][2])==key[0] and chr(plot[y-1,x][3])==key[1]:
            variants.append(key)

        elif y == 0 and x!=0 and chr(plot[y,x-1][2])==key[0]:
            variants.append(key)

        elif x==0 and y!=0 and chr(plot[y-1,x][3])==key[1]:
            variants.append(key)



    if len(variants)>1:
        #print('res',variants[np.random.randint(0,len(variants)-1)])
        return variants[np.random.randint(0,len(variants)-1)]
    elif len(variants)==1:

        return variants[0]
    else:

        return 'none'

def generate_plot(k):
    for y,rows in enumerate(plot):
        for x,tile in enumerate(rows):
            result =chose_tile(x,y)

            if result != 'none':
                plot[y,x] = result
                k += 1
            else:
                break
    return k
k = 0
i = 0
while k<dimensions[0]*dimensions[1]:
    k = 0
    i+=1
    plot[:] = keys[np.random.randint(0,11)]
    k=generate_plot(k)
    print(k)
    print(i)








print(plot)
imgs = np.zeros((246*dimensions[0],246*dimensions[1],3))

for y,rows in enumerate(plot):
    for x,columns in enumerate(rows):

        imgs[y*246:y*246+246,x*246:x*246+246,:]=np.asarray(tileset[str(plot[y,x])[2:6]])/255

plt.imshow(imgs,cmap="hot")
plt.axis('off')
plt.savefig("test.png", bbox_inches='tight')
plt.show()