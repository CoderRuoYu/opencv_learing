import cv2
from PIL import Image

import matplotlib.pyplot as plt
cv2.namedWindow('Cat', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Cat', 400, 200)
img = cv2.imread('./123.jpg',0)
cv2.imshow('Cat',img)
tem = cv2.waitKey(0)
if tem == ord('q'):
    cv2.destroyAllWindows()
