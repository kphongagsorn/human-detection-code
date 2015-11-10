import time
import os, os.path, subprocess
import iteration_whole_process
import reset_onvif_jar

def cycleWholeProcess():
	print "running.."
        #iteration_whole_process.main()
        #time.sleep(10)
        proc = subprocess.Popen(["python", "-c", "import iteration_whole_process; iteration_whole_process.main()"], stdout=subprocess.PIPE) 
        out = proc.communicate()[0]
	#print out
        checkStr = 'nfvOK'
        #print len(out)
	#print len(checkStr)
        #fileRead= proc.communicate()[0]
	fileReadArr=out.split("\n")
	#print fileReadArr
	#if any(checkStr in s for s in fileReadArr):
	if checkStr in fileReadArr:
		print "positive probability above 0.7, stopping cycle.."
		#break
		#print "whole cycle completed, resetting camera..."
		#reset_onvif_jar.main()
                #print "reset complete"
	else:
		#time.sleep(3)
		print "positive probability below 0.7, resuming cycle.."
                cycleWholeProcess()

        #count = 8
        #if out !=  checkStr:
        #	time.sleep(3)
	#	cycleWholeProcess()
		#time.sleep(3)
		#print "bad"               
        #else:
	#	print "whole cycle completed, resetting camera..."
	#	reset_ovif_jar.main()
	#	print "reset complete"
                #break


def main():
	cycleWholeProcess()
	#proc = subprocess.Popen(["python", "-c", "import iteration_whole_process; iteration_whole_process.main()"], stdout=subprocess.PIPE)
        #out = proc.communicate()[0]
        #print out


if __name__ == "__main__":
	main()

#while True:
#	proc = subprocess.Popen(["python", "-c", "import iteration_whole_process; iteration_whole_process.main()"], stdout=subprocess.PIPE)
#        out = proc.communicate()[0]
        #print out
	#print len(out)
#	if out != 'nfvOk\n':
#		print out
#		cycleWholeProcess()
#	else:
#		break	
	#iteration_whole_process.main()
	#result = cycleWholeProcess()
	#print result
	#if result == "ok":
	#	break
	#else:
	#	print "continue loop"
	
