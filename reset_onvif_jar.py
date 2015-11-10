from subprocess import *
import subprocess
import call_nfv_api, reset_nfv_api

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
        #procFR = subprocess.Popen(["python", "-c", "import file_reader_test; file_reader_test.main()"], stdout=subprocess.PIPE)
        #fileRead= procFR.communicate()[0]
        #print fileRead.split("\n")
        #fileReadArr=fileRead.split("\n")
	#readSuccessfully = fileReadArr[0]
        #onvifX = fileReadArr[1]
        #onvifY = fileReadArr[2]
	#print str(onvifX)
	#print str(onvifY)
	#args = ['onvif.jar', '172.16.1.129', 'onvif', '33IoxkAwZ4R', onvifX, onvifY, '2.0'] # Any number of args to be passed to the jar file
	args = ['onvif.jar', '172.16.1.130', 'onvif', '33IoxkAwZ4R', '0.0', '0.0', '0.0']
	
	#print "resetting camera.."
	response = jarWrapper(*args)
	#print response
	
	#deactivate boost
	reset_nfv_api.main()




if __name__ == "__main__":
    main()

