import cv2
import numpy as np

m1 = cv2.imread("./h2.png", 1)
m2 = np.full(m1.shape, (0, 0, 255), np.uint8)
m3 = cv2.absdiff(m1, m2) # 減去紅色, 紅色地方變黑字
# m3 = cv2.subtract(m1, m2) -> 奇怪的顏色, 所有小於0等於0, 背景也變0

# 以下m4, m5留有黑字, 但背景白底仍有黃斑.
m4 = np.full(m1.shape, (255, 255, 255), np.uint8)
m5 = cv2.multiply(m3, m4)
m6 = m5[:,:,1]

'''
# 以下為條件測試
m4 = m3 * 100 # m4背景變馬賽克
m5 = np.full(m1.shape, (255, 255, 255), np.uint8)
m6 = cv2.multiply(m4, m5)  # 背景仍有很重馬賽克
'''

# cv2.imshow("M2", m2)
# cv2.imshow("M3", m3)
# cv2.imshow("M4", m4) 
# cv2.imshow("M5", m5)
cv2.imshow("M6", m6)

cv2.waitKey(0)
cv2.destroyAllWindows()