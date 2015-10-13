import os, os.path, subprocess
import urllib
import urllib2
import pycurl

url = 'http://127.0.0.1:8888/v1/camera/ptz'
#data ='{"url":"172.16.1.140","username":"onvif","password":"33IoxkAwZ4R","pan":"0.0","tilt":"0.0","zoom":"0.0"}'

#data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()

def main():
	procFR = subprocess.Popen(["python", "-c", "import file_reader_test; file_reader_test.main()"], stdout=subprocess.PIPE)
	fileRead= procFR.communicate()[0]
	#print fileRead.split("\n")
	fileReadArr=fileRead.split("\n")
	readSuccessfully = fileReadArr[0]
	onvifX = fileReadArr[1]
	onvifY = fileReadArr[2]
	data = '{"url":"172.16.1.129","username":"onvif","password":"33IoxkAwZ4R","pan":"'+ onvifX + '","tilt":"' + onvifY +'","zoom":"2.0"}'
	#print "curl request:\n"+ data
	print "moving camera.."
	if readSuccessfully == "ok":
		req = urllib2.Request(url, data, headers = {"Content-Type": "application/json"})
		response = urllib2.urlopen(req)
		print response.read()
	else:
		print "positive probability too low"

if __name__ == "__main__":
    main()

#c = pycurl.Curl()
#c.setopt(pycurl.URL, url)
#c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
#c.setopt(pycurl.POST, 1)
#c.setopt(pycurl.POSTFIELDS, data)
#c.perform()
#print "done"




