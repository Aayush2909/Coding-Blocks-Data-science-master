import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import cv2    #module to work on images


#Loading images for different parts of collage
center = cv2.imread("C:/Users/ImageCollage dataset/center.jpeg") 
center = cv2.cvtColor(center, cv2.COLOR_BGR2RGB) 
center = cv2.resize(center, (100,100))

top_left = cv2.imread("C:/Users/ImageCollage dataset/top_left.jpg") 
top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB) 
top_left = cv2.resize(top_left, (200,200))

top_right = cv2.imread("C:/Users/ImageCollage dataset/top_right.jpg") 
top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB) 
top_right = cv2.resize(top_right, (200,200))

bottom_left = cv2.imread("C:/Users/ImageCollage dataset/bottom_left.jpg") 
bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB) 
bottom_left = cv2.resize(bottom_left, (200,200))

bottom_right = cv2.imread("C:/Users/ImageCollage dataset/bottom_right.jpg") 
bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB) 
bottom_right = cv2.resize(bottom_right, (200,200))


#Providing Borders
top_left = cv2.copyMakeBorder(top_left, 10, 5, 10, 5, cv2.BORDER_CONSTANT, None, 0) 
top_right = cv2.copyMakeBorder(top_right, 10, 5, 5, 10, cv2.BORDER_CONSTANT, None, 0)

bottom_left = cv2.copyMakeBorder(bottom_left, 5, 10, 10, 5, cv2.BORDER_CONSTANT, None, 0) 
bottom_right = cv2.copyMakeBorder(bottom_right, 5, 10, 5, 10, cv2.BORDER_CONSTANT, None, 0)


part1 = np.concatenate((top_left,top_right), axis=1)     #Joining two images(upper part)
part2 = np.concatenate((bottom_left, bottom_right), axis=1)    #Joining two images(lower part)
bg_part = np.concatenate((part1, part2), axis=0)    #Joining both parts

center = cv2.copyMakeBorder(center, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, 0)


bg_part[156:276, 156:276, :] = center    #changing values of the center as same as of the center image 
plt.imshow(bg_part)

red = [bg_part[i][j][0] for i in range(0,430) for j in range(0,430)]
green = [bg_part[i][j][1] for i in range(0,430) for j in range(0,430)]
blue = [bg_part[i][j][2] for i in range(0,430) for j in range(0,430)]

res = {'r':red,
       'g':green,
       'b':blue}
    
df = pd.DataFrame(res)
df.to_csv("C:/Users/ImageCollage dataset/result.csv", index=None)    #Store the result in a CSV file
