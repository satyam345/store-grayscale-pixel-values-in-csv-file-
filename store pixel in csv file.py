import cv2
import numpy as np
img = cv2.imread('location of the image')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
npArray = np.array([ elem for singleList in grayscaled for elem in singleList])
np.savetxt('location of the csv file', npArray, delimiter=",")
cv2.waitKey(0)
cv2.destroyAllWindows()
