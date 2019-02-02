
# coding: utf-8

# In[27]:


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2


# In[28]:


#read image #not a change
img = cv2.imread('C:/Users/Aaliyah Ahmed/Desktop/IBMHACK/Baner Gaon.png')


# In[29]:


#show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[30]:


#separate the greens
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green=np.array([36,0,0])
upper_green=np.array([86,255,255])


mask=cv2.inRange(img,lower_green,upper_green)
res=cv2.bitwise_and(img,img,mask=mask)

cv2.imwrite("IMAGE_NAME.png", res)

#slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

#show changes in images
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[55]:


green_min = np.array([35, 68, 8], np.uint8) #BGR 55,88,28
green_max = np.array([85,150,28], np.uint8) #18,72,77)

dst = cv2.inRange(img, green_min, green_max)
num_green = cv2.countNonZero(dst)
#print('The number of green pixels is ' + str(num_green))


# In[56]:


green_area=num_green*15^2
#print ('The green coverage area is: '+ str(green_area)+' sq. metres' )


# In[58]:


carbonemissions=(green_area*100)/(4046.86*350*(2.13)*44)
#print (carbonemissions)



'''

