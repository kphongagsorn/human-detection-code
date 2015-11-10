import os

caffePath = "/home/k.phongagsorn/pichai/xci/attribute"
attrScrPath= "/var/www/html/attr_poc_scripts/test-folder"
#bashCommandExeScr = "./exe/classify_image_list_kevin2.sh"
bashCommandExeScr = "./exe/classify_image_list_kevin2_old.sh"
bashCommandTest = "pwd"


def main():
	#print "classifying image.."
	os.chdir(caffePath)
	os.system(bashCommandExeScr)
	os.chdir(attrScrPath)
	os.system(bashCommandTest)

if __name__ == "__main__":
    main()
