#import sys, os
#sys.path.insert(0, '/usr/local/lib')
#sys.path.insert(0, os.path.expanduser('~/lib'))

import cv2, urllib, threading, time
import numpy as np
from datetime import datetime

#camera IP Addresses: 172.16.1.{130,140,134,1337}
camIpAddress='172.16.1.130'

#stream=urllib.urlopen('http://root:33IoxkAwZ4R@172.16.1.129/mjpg/video.mjpg')
#stream=urllib.urlopen('http://root:33IoxkAwZ4R@'+camIpAddress+'/mjpg/video.mjpg')
stream=urllib.urlopen('http://root:33IoxkAwZ4R@'+camIpAddress+'/mjpg/video.mjpg')

#for reading IP camera stream
#bytes=''

#for photos
#counter=0

def main():
	#for reading IP camera stream
	bytes=''
	#for photos
	counter=0
	while True:
    		bytes+=stream.read(1024)
    		a = bytes.find('\xff\xd8')
    		b = bytes.find('\xff\xd9')
    		jpg = bytes[a:b+2]
    		bytes= bytes[b+2:]
    		image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
    		if image is not None:
        		#save photo name format is: photoCounter_cameraIpAddress_dateTime.png
        		#cv2.imwrite(str(counter)+"_"+camIpAddress+"_"+str(datetime.now())+".png", image)
        		#print str(counter)+", "+ camIpAddress+ ", " + "time stamp:" + str(datetime.now())
        		cv2.imwrite("./raw/raw_"+str(datetime.now())+".png", image)
			cv2.imwrite("./raw.png", image)
			cv2.imwrite("/var/www/html/attr_poc_scripts/test-folder/static/raw.jpg", image)
			print "success"
			counter+= 1
        		break
        		#cv2.imwrite(str(counter)+"_"+camIpAddress+"_"+str(datetime.now())+".png", image)
        		#print str(counter)+", "+ camIpAddress+ ", " + "time stamp:" + str(datetime.now())
        		#counter+= 1
        		#cv2.imwrite(str(counter)+"_"+camIpAddress+"_"+str(datetime.now())+".png", image)
        		#print str(counter)+", "+ camIpAddress+ ", " + "time stamp:" + str(datetime.now())
        		#cv2.imwrite("testImage"+str(counter)+".png",i)
        		#print "print testImage" + str(counter) + "time stamp:" + str(datetime.now())
        		#counter+= 1
       		 	#time.sleep(1)
        		#time.sleep(0.0001)
        		#cv2.imshow('Image from 16E Camera:',i)

if __name__ == "__main__":
    main()
