from sys import *
import os
import time


def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)
    count = 0 

    flag = os.path.isabs(DirName)
    if (flag == False):
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername , subfoldername , filename in os.walk(DirName):
            print("Current Directory Name : " , foldername )

            for subname in subfoldername:
                print("Sub Folder name is : " , subname)

            for fname in filename : 
                # print(fname , "  : " , os.path.getsize(foldername+"/"+fname))
                print(os.path.abspath(fname))

        count = count +1
        print("Count is : ::: " , count)
        
    else:
        print("Invalid Path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument")
        print("Example : Demo.py Marvellous")
        exit()

    else:
        startTime = time.time()
        DirectoryTravel(argv[1])
        endTime = time.time()

        print("FileSystem Scan Completed in : " , (endTime -startTime))

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name