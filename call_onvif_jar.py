from subprocess import *
import subprocess, time
import call_nfv_api
import reset_onvif_jar


def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret

def main():
        procFR = subprocess.Popen(["python", "-c", "import file_reader_test; file_reader_test.main()"], stdout=subprocess.PIPE)
        fileRead= procFR.communicate()[0]
        #print fileRead.split("\n")
        fileReadArr=fileRead.split("\n")
	readSuccessfully = fileReadArr[0]
        onvifX = fileReadArr[1]
        onvifY = fileReadArr[2]
	#print str(onvifX)
	#print str(onvifY)
	#args = ['onvif.jar', '172.16.1.129', 'onvif', '33IoxkAwZ4R', onvifX, onvifY, '2.0'] # Any number of args to be passed to the jar file
	args = ['onvif.jar', '172.16.1.130', 'onvif', '33IoxkAwZ4R', onvifX, onvifY, '1.0']
	#print "moving camera.."
	#print "from onvif caller; " + readSuccessfully
	if readSuccessfully == "ok":
		response = jarWrapper(*args)
		#print response
		call_nfv_api.main()
		print 'nfvOK'
		time.sleep(10)
		reset_onvif_jar.main()
	else:
		print ''
		#print "positive probability too low"

if __name__ == "__main__":
    main()

