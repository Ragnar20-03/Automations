import os 
from sys import * 

# ////////////////////////////////////////////
#   
#   Function Name : printDuplicate 
#   Usage : to hash file in hesadecimal number to uniquely identify the file
#   input : path of file , blocksize to read file 
#   output : return hexadecimal number of file
#   Author : Roshan Patil 
#   Date : 29 Oct 2023
# 
# ////////////////////////////////////////////

def printDuplicate (dict1):
    iSize = 0 
    iCount = 0 
    dulplicateList = list(filter(lambda x : len(x) > 1 , dict1.values()))
    if(len(dulplicateList) > 0):
        print("Duplcaite File Are  ")
        for result in dulplicateList:
            for subresult in result : 
                iSize = iSize + os.path.getsize(subresult)
                iCount = 1 +  iCount
                print(subresult)

    return iSize,iCount