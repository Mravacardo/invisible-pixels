# replace the red pixels ( or undesired area ) with 
# background pixels to generate the invisibility feature. 
  
## 1. Hue: This channel encodes color information. Hue can be 
# thought of an angle where 0 degree corresponds to the red color,  
# 120 degrees corresponds to the green color, and 240 degrees  
# corresponds to the blue color. 
  
## 2. Saturation: This channel encodes the intensity/purity of color. 
# For example, pink is less saturated than red. 
  
## 3. Value: This channel encodes the brightness of color. 
# Shading and gloss components of an image appear in this

import cv2
import numpy as np
import time

print(cv2.__version__)

capture_video = cv2.VideoCapture("video1.mp4")

time.sleep(1)
count = 0
background = 0

for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

background = np.flip(background, axis = 1)
