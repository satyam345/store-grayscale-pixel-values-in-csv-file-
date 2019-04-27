import cv2
import numpy as np
img = cv2.imread('C:/Users/SATYAM/Desktop/28x28/M/image/4D_00002.png')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
npArray = np.array([ elem for singleList in grayscaled for elem in singleList])
np.savetxt('C:/Users/SATYAM/Desktop/28x28/M/csv/4D_00002.csv', npArray, delimiter=",")
cv2.waitKey(0)
cv2.destroyAllWindows()