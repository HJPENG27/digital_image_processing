import cv2
import numpy as np

left = (0, 200)
right = (100, 100)
bd = True

i = 0
while True:
	m1 = np.full((300, 500, 3), (255, 255, 255), np.uint8)
	cv2.rectangle(m1, (left[0]+i, left[1]), (right[0]+i, right[1]), (255, 0, 0), -1) 
	if bd == True:
		i = i + 1
	else: 
		i = i -1

	if right[0] + i > 500:
		bd = False
		
	if left[0] + i < 0:
		bd = True
	
	cv2.imshow("M1", m1)

	if cv2.waitKey(5) != -1:  
			break
cv2.destroyAllWindows() 