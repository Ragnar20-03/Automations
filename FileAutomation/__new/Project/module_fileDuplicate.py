import os 
from sys import * 
from module_Hashing import hashfile

def findDuplicates(path):
    exists = os.path.isdir(path)
    dups = {}
    if exists :
        print("Scanning Files ......")
        for dirName  , subdirs  , fileList in os.walk(path):
            # print("Current Folder is : " , dirName , "***********")
            for file in fileList :
                path = os.path.join(dirName , file)
                print("File Name : : \t\t" , path)
                file_hash = hashfile(path)
                if file_hash in dups :
                    dups[file_hash].append(path)
                else : 
                    dups[file_hash] = [path]
    
    return dups