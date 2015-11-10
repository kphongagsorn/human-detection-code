# -*- coding: utf-8 -*-
 
import cv2, sys, datetime, json, io, ast, time, glob, os, shutil 
import numpy as np
from datetime import datetime

#http://groups.inf.ed.ac.uk/vision/CAVIAR/CAVIARDATA1/


#Note: mp4-compatible verfied
#
#cap = cv2.VideoCapture("distant.AVI")
#cap = cv2.VideoCapture("test2.mp4")
#cap = cv2.VideoCapture("test.mp4") 

#cap = cv2.VideoCapture("/Users/kphongagsorn/AI/opencv/ipCamCode/skirtfour.png") 
#imagePath ="/Users/kphongagsorn/AI/opencv/ipCamCode/test_data/*.png"

#rawDataPath="test_data/*.png"
#processingDataPath = "./raw.jpg"   
processingDataPath = "./raw.png"  
#sentDataPath="sent_data/"


files=glob.glob(processingDataPath) 


#call-back
def nothing(x):
    pass

def main():
	try:
    		for file in files:
      			f=open(file, 'r')  
      			#print f.name
      			image = cv2.imread(f.name)
      			height, width, channels = image.shape
      			#print height, width
      
      			#cv2.namedWindow("TEST")
   
      			#cv2.createTrackbar("X","TEST",0,255,nothing)
      			#cv2.createTrackbar("Y","TEST",0,255,nothing)
   
   
      			#cv2.SetTrackbarPos('test','test2',0)

      			#cascade_path = "./model/aGest.xml"
      			#cascade_path = "./model/haarcascade_frontalface_alt2.xml"
      			#cascade_path = "./model/haarcascade_upperbody.xml"
      			#cascade_path = "./model/haarcascade_mcs_upperbody.xml"
      			cascade_path = "./model/haarcascade_fullbody.xml"
   
      			cascade = cv2.CascadeClassifier(cascade_path)
   
      			color = (0, 255, 255)
   
      			#cv2.imwrite('first_frame.png',frame)

      			#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      			gray = cv2.cvtColor(image, cv2.IMREAD_COLOR)
      			#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
      			#distant
      			facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(65, 65))
   
      			if len(facerect) > 0:
         
        			for rect in facerect:
          				cv2.rectangle(gray, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
   
        			for rect in facerect:
          				x = rect[0]
          				y = rect[1]
          				w = rect[2]
          				h = rect[3]
          				x2 = x+ (w-1)
         				y2 = y+ (h-1)
					#print "width, height:" + str(w) + ", " + str(h)
					#print "x2,y2:" + str(x2) + ", " + str(y2)
          				# img[y: y + h, x: x + w]
          				now = datetime.now()
          				filename = now.strftime("%Y%m%d%H%M%S.") + "%04d" % (now.microsecond // 1000)

          				#cv2.putText(gray,"INPUT COORDINATES",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
                 
          				#cv2.imwrite( 'cut_' + str(filename) +  '_.jpg', gray[y:y+h, x:x+w])
          				#cv2.imwrite( './read_images/read_' + str(filename) +  '_.jpg', gray)
          				#cv2.imwrite( './jpg_output/read_' + str(filename) +  '_.jpg', image)
	  				#shutil.move(file, sentDataPath)
	          
          				data = {}
          				data['x'] = x
          				data['y'] = y
          				data['x2'] = x+ (w-1)
          				data['y2'] = y+ (h-1)
          				#data_str = "[{u'x': '%s', u'y': '%s', u'w': '%s', u'h': '%s'}]" % (x, y, w, h)
          				data_str =f.name + "," + str(width) + "," + str(height) + "," + str(x) + "," + str(y) + "," + str(x2) + "," + str(y2)
          				#data_str_w_quotes = ast.literal_eval(data_str)
          				#print json.dumps(data_str)
          				#print data_str
					#print str(rect[0])
          				with open('./csv/image_list.csv', 'w') as outfile:
            					outfile.write("image,width,height,hx1,hy1,hx2,hy2"+"\n")
	    					outfile.write(data_str+"\n")
            					#json.dump(data_str, outfile)
   					
					with open('./csv_backup/image_list_'+str(datetime.now())+'.csv', 'w') as outfile:
                                                outfile.write("image,width,height,hx1,hy1,hx2,hy2"+"\n")
                                                outfile.write(data_str+"\n")
                                                #json.dump(data_str, outfile)

          				#im = np.zeros((480,600,3), np.uint8)
   
          				x = cv2.getTrackbarPos("X","TEST")
          				y = cv2.getTrackbarPos("Y","TEST")


				#shutil.move(file, sentDataPath)
        			#time.sleep(1)
        			#cv2.imshow('frame',gray)
				#print "detected person"
				print "success"
	
      			else:
        			print "unable to detect person"
      
      			#shutil.move(file, sentDataPath)
      			#print "done"

	except:
  		print sys.exc_info()
	#finally:
 
	#cv2.waitKey(0)
	cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()

