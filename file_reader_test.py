import cv2, sys, datetime, json, io, ast, time, glob, os, csv, matplotlib 
import numpy as np
from datetime import datetime

path = 'csv_output/test_output.csv' 
#path = 'csv_output/image_list_test_output.csv'
#cascade_path = "./model/haarcascade_fullbody.xml"
color = (0, 255, 255)

files=glob.glob(path)
data={}


class Image(object):

    def __init__(self, absolutePath, imageWidth, imageHeight, x1, y1, x2, y2, prob0, prob1):
        self.absolutePath = absolutePath
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
	self.prob0 = prob0
	self.prob1 = prob1

    def getAbsolutePath(self):
        return self.absolutePath

    def getImageWidth(self):
        return self.imageWidth

    def getImageHeight(self):
        return self.imageHeight

    def getX1(self):
        return self.x1

    def getX2(self):
        return self.x2

    def getY1(self):
        return self.y1

    def getY2(self):
        return self.y2
    
    def getProb0(self):
	return self.prob0
    
    def getProb1(self):
	return self.prob1

    def __str__(self):
        return "%s, %s" % (self.absolutePath, self.imageWidth)



def main():
	for file in files:     
    		f=open(file)
    		csv_f=csv.reader(f) 
    		#print f
   		#skip headers
    		csv_f.next()
    		for row in csv_f:
    			imgObj = Image(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
    			data[row[0]+row[6]]=imgObj
    			#print Image.getY1(imgObj)
    			#print row
			with open('./csv_output_backup/image_list_'+str(datetime.now())+'.csv', 'w') as outfile:
                		outfile.write("image,width,height,hx1,hy1,hx2,hy2,prob0,prob1"+"\n")
                        	outfile.write(str(row)+"\n")
                        #json.dump(data_str, outfile)

    		f.close()

	#print len(data)
	counter=0;
	for key in data:
		imagePath = Image.getAbsolutePath(data[key])
		#print imagePath
		image = cv2.imread(imagePath)
		height, width, channels = image.shape
		attribute = "Attribute Here"
		readSuccessfully="bad"
		probZero = "-1"
                probOne = "-1"
		gray = cv2.cvtColor(image, cv2.IMREAD_COLOR)
		if 0.7 <= float(Image.getProb1(data[key])) <=1.00:
			readSuccessfully="ok"
			#print readSuccessfully
			#probZero = "0.00"
			#attribute = "Phone"
			#cv2.putText(gray, attribute  + ":" + Image.getProb1(data[key]),(int(Image.getX1(data[key])),int(Image.getY1(data[key]))), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
		else:
			readSuccessfully="bad"
			#probZero = "%.2f" % float(Image.getProb0(data[key]))
		#if  Image.getProb1(data[key]).find("e"):
			#probOne = "0.00"
		#else:
			#probZero = "%.2f" % float(Image.getProb0(data[key]))
			#probOne = "%.2f" % float(Image.getProb1(data[key]))
			#attribute = "Not Phone"
			#cv2.putText(gray, attribute  + ":" + Image.getProb0(data[key]),(int(Image.getX1(data[key])),int(Image.getY1(data[key]))), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
		#gray = cv2.cvtColor(image, cv2.IMREAD_COLOR)
		cv2.imwrite( '/var/www/html/attr_poc_scripts/test-folder/before/before_' + str(datetime.now()) +  '.jpg', gray)
	        cv2.imwrite( '/var/www/html/attr_poc_scripts/test-folder/static/before' + str(counter) +  '.jpg', gray)

		#print Image.getX1(data[key]) + ", " + Image.getY1(data[key])
		#print Image.getX2(data[key]) + ", " + Image.getY2(data[key])
		cv2.rectangle(gray, (int(Image.getX1(data[key])),int(Image.getY1(data[key]))), (int(Image.getX2(data[key])),int(Image.getY2(data[key]))),color, thickness=2)
		#cv2.putText(gray, "Phone", int(Image.getY1(data[key])), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
		#probZero = float(Image.getProb0(data[key]))
		#probOne = float(Image.getProb1(data[key]))
		cv2.putText(gray, "Phone: "+ Image.getProb0(data[key]) + ", " + Image.getProb1(data[key]),(0,int(Image.getImageHeight(data[key]))-10), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
		#cv2.putText(gray, "Prob 0: "+ str(float("%2.f" % probZero))+" Prob1:"+ str(float("%2.f" % probOne)),(int(Image.getX2(data[key])),int(Image.getY2(data[key]))), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
		#cv2.imwrite( './output/output_' + str(counter) +  '_.jpg', gray)
		
		cv2.imwrite( '/var/www/html/attr_poc_scripts/test-folder/after/after_' + str(datetime.now()) +  '.jpg', gray)
		cv2.imwrite( '/var/www/html/attr_poc_scripts/test-folder/static/output_' + str(counter) +  '_.jpg', gray)
	
		if readSuccessfully=="ok":	
			grayBorder = cv2.copyMakeBorder(gray,10,10,10,10,cv2.BORDER_CONSTANT, value=[0,0,255])
			cv2.imshow('Result',grayBorder)
		else:
			cv2.imshow('Result',gray)
		
		counter+=1
		#print Image.getY1(data[key])
		#print "outputting image.."
		UpOnvifCoordX = float(Image.getX1(data[key]))/float(Image.getImageWidth(data[key]))
		imageCenterX = float(Image.getImageWidth(data[key]))/2.0 
		imageCenterY = float(Image.getImageHeight(data[key]))/2.0
		onvifX = imageCenterX
		onvifY = imageCenterY
		#print "prob0: " + str(Image.getProb0(data[key])) + " prob1: " + str(Image.getProb1(data[key]))
		#print "prob0: " + probZero + " prob1: " + probOne
		print readSuccessfully
		onvifWidth = float(Image.getX2(data[key]))-(float(Image.getX1(data[key]))+1.0)
		onvifHeight = float(Image.getY2(data[key]))-(float(Image.getY1(data[key]))+1.0)
		
		onvifWidthCoord = float(Image.getX1(data[key]))+(onvifWidth/2.0)
		onvifHeightCoord = float(Image.getY1(data[key]))+(onvifHeight/2.0)

		#print str(onvifWidthCoord)
		#print str(onvifHeightCoord)


		if onvifWidthCoord < imageCenterX:
			#zoomHalfWidth = (float(Image.getImageWidth(data[key]))/2.0)/imageCenterX
			#onvifXFromL = float(Image.getX1(data[key]))/imageCenterX
			#onvifX = (1.0-onvifXFromL) * -1.0
			
			#zoomHalfWidth = (float(Image.getImageWidth(data[key]))/2.0)/imageCenterX
			#print "onvifXFromL:" + str(onvifXFromL)
			
			onvifXFromL = onvifWidthCoord/float(Image.getImageWidth(data[key]))
			onvifX = (1.0-onvifXFromL) * -1.0
			print onvifX
		elif onvifWidthCoord > imageCenterX:
			#onvifXFromL = float(Image.getX1(data[key]))/(float(Image.getImageWidth(data[key]))/2.0)
			#onvifX = onvifXFromL
			
			onvifXFromL = onvifWidthCoord/float(Image.getImageWidth(data[key]))
			onvifX = onvifXFromL
			print onvifX
		else:
		        onvifX = (imageCenterX/float(Image.getImageWidth(data[key]))) 
			print onvifX
		if onvifHeightCoord < imageCenterY:
			#onvifYFromL = float(Image.getY1(data[key]))/imageCenterY
                        #onvifY = (1.0-onvifYFromL)
                        #print "onvifYFromL:" + str(onvifYFromL)

			onvifYFromL = onvifHeightCoord/float(Image.getImageHeight(data[key]))
			onvifY = (1.0-onvifYFromL)
                        print onvifY
		elif onvifHeightCoord > imageCenterY:
			#onvifYFromL = float(Image.getY1(data[key]))/(float(Image.getImageHeight(data[key]))/2.0)
			#onvifY = (1.0-(onvifYFromL) * -1.0

			onvifYFromL = onvifHeightCoord/float(Image.getImageHeight(data[key]))
			onvifY = (1.0-onvifYFromL) * -1.0
			print onvifY
		else:
			onvifY = (imageCenterY/float(Image.getImageHeight(data[key]))+(float(Image.getImageWidth(data[key]))/2.0))
			print onvifY	
		
		cv2.waitKey(5000)
		cv2.destroyAllWindows()
		#print imageCenterX
                #print "prob0: " + str(Image.getProb0(data[key])) + "prob1: " + str(Image.getProb1(data[key]))
	#print len(data)
	#print "done"
	

if __name__ == "__main__":
    main()
