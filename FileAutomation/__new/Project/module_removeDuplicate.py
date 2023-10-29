# Requiring Modules

import os 
from sys import * 


# ////////////////////////////////////////////
#   
#   Function Name : removeDuplicates 
#   Usage  :   remove duplicate files by skipping original Files 
#   input  :   Dictionary which contain {key : [hashcode] , value : [path_of_a_file]}
#   output :   Delete Duplicate Files Completely
#   Author : Roshan Prashant  Patil 
#   Date : 29 Oct 2023
#
# ////////////////////////////////////////////

def removeDuplicates(dict1):
    duplicates = list(filter(lambda x : len(x) > 1 , dict1.values()))

    iCnt = 0 
    if (len(duplicates )> 0):
        for result in duplicates:
            for subresult in result :
                iCnt = iCnt + 1 

                # For Skipping 1 iteration i.e . Skipping original File : 
                if iCnt > 1 :
                    print("Removing :: " , subresult)
                    os.remove(subresult)
            iCnt = 0 
    else :
        print("No Duplicates Found :")