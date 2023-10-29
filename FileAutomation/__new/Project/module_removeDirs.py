import os 
from sys import * 

# ////////////////////////////////////////////
#   
#   Function Name : reoveEmptyDirs 
#   Usage : To Remove All empty Directoies
#   input : path_of_directory 
#   output : remove empty directories
#   Author : Roshan Patil 
#   Date : 29 Oct 2023
# 
# ////////////////////////////////////////////

def removeEmptyDirs(path):
    for dirName , subdirs , fileList in os.walk(path):
        print(dirName , " -----")
        for subdir in subdirs:
            path = os.path.join(dirName , subdir)
            lenX = os.listdir(path)
            print("Length is  : " , lenX)
            if (len(lenX) == 0 ):
                print("path is : " ,path)
                os.rmdir(path)