import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load an color image in grayscale
    img = cv2.imread('D:/sohaib/sohaib/1.jpg')
    print(img.shape)
    cv2.imshow('orig-image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('bgrToGray-image',gray)

    print("blue", img.item(10,10,0))
    print("green", img.item(10,10,1))
    print("red", img.item(10,10,2))

    # swap blue with green
    temp=np.copy(img[:,:,0])
    img[:,:,0]=np.copy(img[:,:,1])
    img[:,:,1]=np.copy(temp)
    cv2.imshow('swapped-image',img)

    print("swapped-blue", img[10,10,0])
    print("swapped-green", img.item(10,10,1))
    print("swapped-red", img.item(10,10,2))

    ## access specific pixel

    # set specific pixel
    img.itemset((10,10,2),100)
    img[10,10,2] = 100

    #set whole rectangular region to a particular value
    img[100:250, 300:350] = 0

   # using matplotlib
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

    x = np.uint8([250])
    y = np.uint8([10])  
    print("numpy", x+y)  # 250+10 = 260 % 256 = 4 
    print("openCV", cv2.add(x,y)) # 250+10 = 260 => 255

    cv2.waitKey(0)
    cv2.destroyAllWindows()