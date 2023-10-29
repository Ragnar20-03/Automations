import os 
import hashlib
from sys import * 

# ////////////////////////////////////////////
#   
#   Function Name : hasfile 
#   Usage : to hash file in hesadecimal number to uniquely identify the file
#   input : path of file , blocksize to read file 
#   output : return hexadecimal number of file
#   Author : Roshan Prashant Patil 
#   Date : 29 Oct 2023
#
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