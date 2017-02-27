#this program will take video feed,the feed will consist of huge number of frames
#from each frame 28*28 sized 289 image chunks will be cut off by sliding window
#the chunks will be stored into a python list in order to be further used by other programs

import cv2
import numpy as np

#slider function
def cut_image(img,y,bucket):
	image = img
	index = y
	bkt = bucket
	i = 0
	j = 0

	height = np.size(image, 0)
	width = np.size(image, 1)

	#z is row
	#x is column

	#the slider takes the first row, then slides through it, after 
	#that, it goes to the next row and does its thing.
	for z in range(0,int(height/28)):
		j = 0;
		for x in range(0,int(width/28)):
			#cv2.imwrite('./images/x'+str(index)+str(z)+str(x)+'.png',image[i:i+28,j:j+28])

			#checking if the current piece/frame/chunk is all zero or not.if not, then take it
			if(np.all(image[i:i+28,j:j+28]!=0)):
				bkt.append(image[i:i+28,j:j+28])
			#increment j in order to move the slide right by 28 pixels. going to the next '28 fat' column	
			j = j+28
		#increment i in order to move slide down by 28 pixels. going to the next '28 high' row 	
		i = i+28
	return bkt	



cap = cv2.VideoCapture()
cap.open(0)
y = 0
bucket = []


while True:

	ret,frame = cap.read()
	
	#whatever the camera resolution is, the camera size has to be of multiple of 28
	height = int((np.size(frame, 1))/28)
	width = int((np.size(frame, 0))/28)

	#take the minimum of the two, otherwise it will go out of bound
	size = min([width,height])

	#make new camera-frame size
	new_frame = frame[0:28*size,0:28*size]

	#show, not necessary
	cv2.imshow('frame',new_frame)

	#getting all the 'slided' pieces into a list i.e Bucket
	bucket = cut_image(new_frame,y,bucket)
	y = y+1

	#press 'q' to stop the video feed!!!!!!!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

# accessing 300th 'frame' gotten from sliding window which is a box of 3 dimension 
# then accessing 20th row of that
#print(bucket[300][20])


