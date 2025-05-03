import numpy as np
import cv2
import math

image = np.zeros((28, 28, 3), dtype=np.uint8)

image[10, 15] = [0, 0, 255]
image[21, 23] = [0, 255, 0]

cv2.imwrite('2.png', image)

x1, y1 = 15, 10
x2, y2 = 23, 21

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)
