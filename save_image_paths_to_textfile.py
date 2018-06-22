import os
import cv2
#import xml.etree.ElementTree as ET
import numpy as np
import glob
import fnmatch


def create_train_and_test_list(mode,root_path):
	Train_list = []
	Test_list = []
	mode = mode
	for root, dirnames, filenames in os.walk(root_path):
	    for filename in fnmatch.filter(filenames, '*.jpg'):
	    	 
	    	if mode == "Train":
	    		set_num = ['00','01','02','03','04','05','06']
	    		if "visible" in root:
		    		for i in set_num:
		    		    if "set" + i in root:
		    		    	#print "set" + i
		    		    	#print "set" + i in root
		    		    	print os.path.join(root, filename)
		    		    	#raw_input("first stop")
		    		    	
		    		    	Train_list.append(os.path.join(root, filename))
	
		if mode == "Test":
			set_num = ['07','08','09','10','11']
		    	if "visible" in root:
		    		for i in set_num:
		    		    if "set" + i in root:
		    		    	#print "set" + i
		    		    	#print "set" + i in root
		    		    	print os.path.join(root, filename)
		    		    	#raw_input("first stop")
		    		    	
		    		    	Test_list.append(os.path.join(root, filename))	
	if mode == "Train":
		print len(Train_list)
		return Train_list
	if mode == "Test":
		print len(Test_list)
		return Test_list
	     			    	
			
	
def save_as_text_file(list_to_save,dest_dir,mode):
	with open(dest_dir + mode + ".txt", 'w') as fn:
		for item in list_to_save:
  			fn.write("%s\n" % item)
	


if __name__ == "__main__":
	root_path = "/home/kishan/Documents/Connor-Code/keras-frcnn/kaist-rgbt/"
	mode = "Train"
	dest_dir = "/home/kishan/Documents/Connor-Code/keras-frcnn/kaist-rgbt/"
	list_to_save = create_train_and_test_list(mode,root_path)
	save_as_text_file(list_to_save,dest_dir,mode)
	print "Complete"



