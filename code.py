#Code Here
import numpy as np
import matplotlib.pyplot as plt
photo_data=plt.imread(r"C:\Users\Subham Sarkar\Desktop\Python Scripts\Week1_Assignment\Milky_way.jpg")
img_GB=photo_data.copy()
img_GB[:,:,0]=0
plt.imshow(img_GB)
