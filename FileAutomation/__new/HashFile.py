
# Requiring Modules

import os 
from sys import * 
import hashlib


def removeDuplicates(dict1):
    duplicates = list(filter(lambda x : len(x) > 1 , dict1.values()))

    iCnt = 0 
    if (len(duplicates )> 0):
        for result in duplicates:
            for subresult in result :
                iCnt = iCnt + 1 
                if iCnt > 1 :
                    print("Removing :: " , subresult)
            iCnt = 0 
    else :
        print("No Duplicates Found :")

# ////////////////////////////////////////////
#   
#   Function Name : hasfile 
#   Usage : to hash file in hesadecimal number to uniquely identify the file
#   input : path of file , blocksize to read file 
#   output : return hexadecimal number of file
#   Author : Roshan Patil 
#   Date : 29 Oct 2023
# ////////////////////////////////////////////

def hashfile(path , blocksize = 4096):
    afile = open (path , 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    # print("--------------------------" , hasher.hexdigest )
    return hasher.hexdigest()

# ////////////////////////////////////////////
#   
#   Function Name : treavelDirectory 
#   Usage : To travel firectory , sub directory in it to hash file 
#   input : abs path of file 
#   output : return list of hashdecimal value of files
#   Author : Roshan Patil 
#   Date : 29 Oct 2023
# ////////////////////////////////////////////

def travelDirectory(path):
    exists = os.path.isdir(path)
    dups = {}
    if exists :
        for dirName  , subdirs  , fileList in os.walk(path):
            # print("Current Folder is : " , dirName , "***********")
            for file in fileList :
                path = os.path.join(dirName , file)
                file_hash = hashfile(path)

                if file_hash in dups :
                    dups[file_hash].append(path)
                else : 
                    dups[file_hash] = [path]
    
    return dups


def printResults (dict1):
    dulplicateList = list(filter(lambda x : len(x) > 1 , dict1.values()))
    if(len(dulplicateList) > 0):
        print("Duplcaite File Are  ")
        for result in dulplicateList:
            for subresult in result : 
                print(subresult)
# Stater Function


def main():
    print("*"*10)
    dict1 = travelDirectory(argv[1])
    printResults(dict1)
    removeDuplicates(dict1)

if __name__ == "__main__":
    main()