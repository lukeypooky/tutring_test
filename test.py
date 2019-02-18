import cv2

ing = cv2.imread('./data/temp.png',cv2.IMREAD_COLOR)

gray = cv2.imread('./data/temp.png', cv2.IMREAD_GRAYSCALE)

unchange = cv2.imread('./data/temp.png', cv2.IMREAD_UNCHANGED)


cv2.imwrite('gray.png',gray)

#a = input()
#b = input()

small = cv2.resize(ing, None,fx = 0.5, fy = 0.5, interpolation=cv2.INTER_AREA)

#zoom = cv2.resize(ing, (a,b), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('shrink', small)
#cv2.imshow('zoooooo', zoom)

rows,cols = ing.shape[:2]
m = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.5)

dst = cv2.warpAffine(ing,m,(cols,rows))

cv2.imshow("rotation",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()