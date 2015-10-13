import os, os.path, subprocess
import urllib
import urllib2
import pycurl

url = 'http://192.168.1.8:8000/api/vcpe/1/bandwidth'
#data ='{"url":"172.16.1.140","username":"onvif","password":"33IoxkAwZ4R","pan":"0.0","tilt":"0.0","zoom":"0.0"}'

#data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()

def main():
	#procFR = subprocess.Popen(["python", "-c", "import file_reader_test; file_reader_test.main()"], stdout=subprocess.PIPE)
	#fileRead= procFR.communicate()[0]
	#print fileRead.split("\n")
	#fileReadArr=fileRead.split("\n")
	#onvifX = fileReadArr[0]
	#onvifY = fileReadArr[1]
	data = "camera_ip=172.16.1.130&qos=high"
	#print "curl request:\n"+ data
	print "activating boost.."
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	req = urllib2.Request(url, data)
	req.get_method = lambda: 'PUT'
	response = urllib2.urlopen(req)
	print response.read()

if __name__ == "__main__":
    main()

#c = pycurl.Curl()
#c.setopt(pycurl.URL, url)
#c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
#c.setopt(pycurl.POST, 1)
#c.setopt(pycurl.POSTFIELDS, data)
#c.perform()
#print "done"




