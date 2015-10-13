import os, os.path, subprocess
import axis_photo_extractor_non_repeating
import image_recg_file
import classify_image_script_caller
import file_reader_test
import call_onvif_api
import call_onvif_jar
import call_nfv_api

#execfile("axis_photo_extractor_non_repeating.py")
#execfile("image_recg_file2.py")
#execfile("classify_image_script_caller.py")
#execfile("file_reader_test.py")

def detectPerson():
    proc = subprocess.Popen(["python", "-c", "import axis_photo_extractor_non_repeating; axis_photo_extractor_non_repeating.main()"], stdout=subprocess.PIPE)
    proc = subprocess.Popen(["python", "-c", "import image_recg_file; image_recg_file.main()"], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    #print out
    #print len(out)
    checkStr = 'success\n'
    #print len(checkStr)
    #count = 8
    if out !=  checkStr:
	print "unable to detect person"
        detectPerson()
    else:
        print 'detectPerson ok'
	#do nothing

def main():
    #print "start"
    cleanUpBashCmd = "rm -f csv/image_list.csv output/output_0_.jpg csv_output/test_output.csv"
    os.system(cleanUpBashCmd)

    #print "removing old previous csv input and output"
    detectPerson()
    classify_image_script_caller.main()

    procFR = subprocess.Popen(["python", "-c", "import file_reader_test; file_reader_test.main()"], stdout=subprocess.PIPE)
    fileRead= procFR.communicate()[0]
    print fileRead
    
    #call_onvif_api.main()
    
    #includes nfv api call
    call_onvif_jar.main()
    
    #call_nfv_api.main()
    #file_reader_test.main()
    #execfile("file_reader_test.py")
    #axis_photo_extractor_non_repeating.main()
    #image_recg_file2.main()
    print "cycle complete"	

if __name__ == "__main__":
    main()
