# ////////////////////////////////////////////
#   
#   Function Name : printSize 
#   Usage : To Print Duplicate file sizes
#   input : Size , Count 
#   output : Display File Count and size
#   Author : Roshan Patil 
#   Date : 29 Oct 2023
# 
# ////////////////////////////////////////////


def printSize(iSize , iCount):
        print("\n")
        print("Duplicate Files Count is : " , iCount)
        print("Duplicate Files Data Size : " ,( iSize /1024/1024/1024), "GB")
        print("Duplicate Files Data Size : " ,( iSize /1024/1024), "MB")

        print("\n")
