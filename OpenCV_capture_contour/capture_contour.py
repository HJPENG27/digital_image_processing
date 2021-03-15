import cv2
import numpy as np

p1 = cv2.VideoCapture("h3.mp4")
while p1.isOpened() ==True:  
	ret, m1 = p1.read()
	if ret ==True:
		
		# 將藍色通道取出, 去掉其它背景值與通道
		m2 = m1.copy()
		m2[:,:,0] = cv2.subtract(m2[:,:,0], m2[:,:,1])
		m2[:,:,0] = cv2.subtract(m2[:,:,0], m2[:,:,2])
		m2 = cv2.bitwise_not(m2[:,:,0])
		th, m2 = cv2.threshold(m2, 230, 255 , cv2.THRESH_BINARY_INV)
		m2 = cv2.dilate(m2, np.ones((10, 30)))
		cv2.imshow("M2", m2) # m2只剩黑底白筆
		

		# 取出m2的輪廓:
		a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		print(b) 
		m3 = m1.copy()     
		for i in range(0, len(a)):						 
			x, y, w, h = cv2.boundingRect(a[i])			
			cv2.rectangle(m3, (x,y), (x+w, y+h), (0, 0, 255), 2)
			cv2.imshow("video", m3)
	       
		if cv2.waitKey(42) != -1:
			break
	else:
		break
p1.release()
cv2.destroyAllWindows()



 