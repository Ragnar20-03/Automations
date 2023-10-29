
# Requiring Modules

from sys import * 
import time 

from module_fileDuplicate import findDuplicates
from module_printDuplicate import printDuplicate
from module_printSize import printSize
from module_removeDirs import removeEmptyDirs
from module_removeDuplicate import removeDuplicates



# Starter Function

def main():
    print ("\n\n#################################################################")
    print("------ Duplicate File Removal -----  ")
    print ("################################################################# \n\n")

    if len(argv)!= 2 :
        print("Invalid Number of Arguments : ")
        exit()
    
    if (argv[1] == '-h') or (argv[1] == '-H'):
        print("This Script is used to Detect Dulicate Files And remove them From System...\n\n")
        exit()
    
    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("Uasge : ApllicationName Abs_Path_of_Directory\n\n")
        exit()

    try: 
        dict1 = {}
        startTime = time.time()   
        #  Finf Similar Files in Dictionary 
        dict1 = findDuplicates(argv[1])
        #  print Duplicate Files
        iSize , iCount = printDuplicate(dict1)
        if (iCount == 0 ):
            print("No Duplicates Found :: \n\n")
            exit()
        # Print Size 
        printSize(iSize , iCount)

        #  Removing Similar files
        removeDuplicates(dict1)
        
        # Removing Empty Directories
        removeEmptyDirs(argv[1])

        endTime = time.time()

        print("\n\nTook %s seconds to execute ... \n\n" %(endTime - startTime))
    
    except ValueError:
        print("Invalid DataType of input : ")
    except Exception as E :
        print("Unknown Error Occured : " , E)


# Stater Function call:
if __name__ == "__main__":
    main()

