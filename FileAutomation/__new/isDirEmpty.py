import os 
import time 
from sys import * 

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

def main():
    removeEmptyDirs(argv[1])


if __name__=="__main__":
    main()